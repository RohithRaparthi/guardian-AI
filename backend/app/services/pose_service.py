import cv2
import mediapipe as mp
import math
import threading
import os
from datetime import datetime

from playsound import playsound

from app.services import monitoring_state
from app.services.email_service import send_fall_email

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Control repeated alarm trigger
fall_active = False


def play_alarm():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        alarm_path = os.path.join(base_dir, "assets", "alarm.mp3")

        if os.path.exists(alarm_path):
            playsound(alarm_path)
        else:
            print("Alarm file not found at:", alarm_path)

    except Exception as e:
        print("Alarm error:", e)


def calculate_angle(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    angle = math.degrees(math.atan2(dx, dy))
    return abs(angle)


def detect_pose(frame):
    global fall_active

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    # If no person detected
    if not results.pose_landmarks:
        monitoring_state.posture_status = "No Person"
        monitoring_state.fall_detected = False
        fall_active = False
        return frame, {
            "posture": "No Person",
            "fall_detected": False
        }

    landmarks = results.pose_landmarks.landmark

    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]

    shoulder_x = (left_shoulder.x + right_shoulder.x) / 2
    shoulder_y = (left_shoulder.y + right_shoulder.y) / 2

    hip_x = (left_hip.x + right_hip.x) / 2
    hip_y = (left_hip.y + right_hip.y) / 2

    angle = calculate_angle((shoulder_x, shoulder_y), (hip_x, hip_y))

    posture = "Standing"
    fall_detected = False

    # 🔥 ULTRA SENSITIVE FALL DETECTION
    if angle > 20:
        posture = "Falling"
        fall_detected = True

        if not fall_active:
            fall_active = True

            # Store fall time
            monitoring_state.last_fall_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Play alarm in background
            threading.Thread(target=play_alarm, daemon=True).start()

            # Send email in background
            threading.Thread(target=send_fall_email, daemon=True).start()
    else:
        fall_active = False

    # Update global state
    monitoring_state.posture_status = posture
    monitoring_state.fall_detected = fall_detected

    # Draw on frame
    cv2.putText(frame, f"Posture: {posture}", (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, f"Angle: {int(angle)}", (30, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    if fall_detected:
        cv2.putText(frame, "FALL DETECTED!", (30, 130),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    return frame, {
        "posture": posture,
        "fall_detected": fall_detected
    }