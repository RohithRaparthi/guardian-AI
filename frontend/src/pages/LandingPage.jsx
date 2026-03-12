import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

export default function LandingPage() {
  return (
    <div>
      <Navbar />

      <section className="hero">
        <div className="hero-left">
          <h1>
            Advanced Protection for <br />
            Your Loved Ones.
          </h1>

          <p>
            Real-time AI monitoring detects falls instantly and alerts guardians immediately.
          </p>

          <div className="hero-buttons">
            <Link to="/dashboard">
              <button className="primary-btn">
                Start Monitoring Now →
              </button>
            </Link>

            <Link to="/register">
              <button className="secondary-btn">
                Register Guardian
              </button>
            </Link>
          </div>
        </div>

        <div className="hero-right">
          <div className="pose-circle">
            <div className="pose-icon">🧍</div>
          </div>
        </div>
      </section>
    </div>
  );
}