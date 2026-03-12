import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/dashboard.css";

export default function Dashboard() {
  const [guardians, setGuardians] = useState([]);
  const [selectedGuardian, setSelectedGuardian] = useState("");
  const [status, setStatus] = useState({
    posture: "Loading...",
    fall_detected: false,
    last_fall_time: null
  });

  // Fetch guardians
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/guardians/")
      .then(res => setGuardians(res.data))
      .catch(err => console.log(err));
  }, []);

  // Poll monitoring status
  useEffect(() => {
    const interval = setInterval(() => {
      axios.get("http://127.0.0.1:8000/api/monitoring/status")
        .then(res => setStatus(res.data))
        .catch(() => console.log("Backend not reachable"));
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  const handleSelectGuardian = (email) => {
    setSelectedGuardian(email);

    axios.post("http://127.0.0.1:8000/api/monitoring/select-guardian", {
      email: email
    }).then(() => {
      alert("Guardian selected successfully");
    });
  };

  return (
    <div className="dashboard-container">
      <div className="sidebar">
        <h2>Monitoring Controls</h2>

        <label>Select Guardian</label>
        <select
          value={selectedGuardian}
          onChange={(e) => handleSelectGuardian(e.target.value)}
        >
          <option value="">-- Select Guardian --</option>
          {guardians.map((g) => (
            <option key={g.id} value={g.email}>
              {g.name}
            </option>
          ))}
        </select>

        <div className="status-box">
          <p><strong>Posture:</strong> {status.posture}</p>
          <p>
            <strong>Fall Detected:</strong>{" "}
            {status.fall_detected ? "YES ⚠️" : "No"}
          </p>
          <p>
            <strong>Last Fall Time:</strong>{" "}
            {status.last_fall_time || "No fall yet"}
          </p>
        </div>
      </div>

      <div className="monitoring-area">
        <img
          src="http://127.0.0.1:8000/api/monitoring/video-feed"
          alt="Monitoring Feed"
        />
      </div>
    </div>
  );
}