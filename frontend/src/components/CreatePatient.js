import { useState } from "react";
import { API_BASE_URL } from "../App";
import axios from "axios";

const createPatient = async (firstName, lastName, ssnId) => {
  try {
    const result = await axios.post(API_BASE_URL + "/patients/", {
        first_name: firstName,
        last_name: lastName,
        ssn_id: ssnId,
    });
    return result.data;
  } catch (e) {
    console.error(e);
    return e;
  }
};

const CreatePatient = ({ refetchPatients }) => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setSecondName] = useState("");
  const [ssnId, setSsnId] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [submitMessage, setSubmitMessage] = useState("");

  const handleSubmit = async (event) => {
    setIsLoading(true);
    event.preventDefault();
    setSubmitMessage("");
    const result = await createPatient(firstName, lastName, ssnId);
    if (!result) {
      setSubmitMessage("Unable to create Patient");
      setIsLoading(false);
      return;
    }
    await refetchPatients();
    setSubmitMessage("Created Patient: " + JSON.stringify(result));
    setIsLoading(false);
  };

  return (
    <>
      <h2>Create a new Patient</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="first-name">First Name:</label>
        <br />
        <input type="text"
          id="first-name"          
          onChange={(event) => setFirstName(event.target.value)}
          value={firstName}
        />
        <br />
        <label htmlFor="second-name">Last Name:</label>
        <br />
        <input type="text"
          id="second-name"
          onChange={(event) => setSecondName(event.target.value)}
          value={lastName}
        />        
        <br />
        <label htmlFor="ssn-id">SSN ID:</label>
        <br />
        <input type="number"
          id="ssn-id"
          onChange={(event) => setSsnId(event.target.value)}
          value={ssnId}
        />        
        <br />
        <button type="submit" disabled={isLoading}>
          Submit
        </button>
      </form>
      {submitMessage && (
        <p>
          <i>{submitMessage}</i>
        </p>
      )}
    </>
  );
};

export default CreatePatient;
