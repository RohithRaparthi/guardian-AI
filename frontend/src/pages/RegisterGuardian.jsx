import { useState } from "react";
import Navbar from "../components/Navbar";
import axios from "axios";

export default function RegisterGuardian() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const handleSubmit = async () => {
    if (!name || !email) {
      alert("Fill all fields");
      return;
    }

    try {
      await axios.post("http://127.0.0.1:8000/api/guardians", {
        name,
        email,
      });

      alert("Guardian Registered Successfully!");
      setName("");
      setEmail("");
    } catch (err) {
      alert("Backend Error");
    }
  };

  return (
    <div>
      <Navbar />

      <div className="register-wrapper">
        <div className="register-card">
          <h2>Register Guardian</h2>

          <input
            placeholder="Guardian Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />

          <input
            placeholder="Guardian Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <button onClick={handleSubmit}>
            Register Guardian
          </button>
        </div>
      </div>
    </div>
  );
}