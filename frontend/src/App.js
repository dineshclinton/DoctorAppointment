import React, { useState, useEffect } from "react";
import "./App.css";
import logo from "./logo.svg";

import { fetchClinicians } from "./requests";

function App() {
  const [clinicians, setClinicians] = useState(null);
  useEffect(() => {
    async function getClinicians() {
      const clinicianData = await fetchClinicians();
      setClinicians(clinicianData);
    }

    getClinicians();
  }, []);
  return (
    <div className="App">
      <div className="logo-wrapper">
        <img src={logo} className="logo" alt="logo" />
      </div>
      <div className="instructions">
        <h2>Welcome to Firefly's Take Home Interview</h2>
        <p>For the front-end portion, please implement two components</p>
        <ul>
          <li>
            A component that lets you book an appointment, based on clinician
            availability.
          </li>
          <li>
            A component that displays the appointments that are currently
            scheduled. This should also allow scheduled appointments to be
            cancelled.
          </li>
        </ul>
      </div>
      <pre className="response">{JSON.stringify(clinicians, null, 2)}</pre>
    </div>
  );
}

export default App;
