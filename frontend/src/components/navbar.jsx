import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        <span className="shield">🛡</span>
        SafeGuard AI
      </div>

      <div className="nav-links">
        <a href="#">Features</a>
        <a href="#">How it Works</a>
        <a href="#">Pricing</a>
        <a href="#">Support</a>
      </div>

      <button className="launch-btn">Launch System</button>
    </nav>
  );
}