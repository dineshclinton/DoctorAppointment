import { useState, useEffect } from "react";
import { API_BASE_URL } from "../App";
import axios from "axios";
import DateTimePicker from "react-datetime-picker";

const createAppointment = async (startTime, endTime, patient, docAvail) => {
  try {
    debugger
    const result = await axios.post(API_BASE_URL + "/appointments/", {
      start_time: startTime,
      end_time: endTime,
      patient: patient,
      doctor_availability: docAvail,
    });
    return result.data;
  } catch (e) {
    console.error(e);
    return e.response;
  }
};

const CreateAppointment = ({ refetchAppointments }) => {
  const [docAvail, setDocAvail] = useState([]);
  const [docAvailValue, setDocAvailValue] = useState();
  const [patient, setPatient] = useState([]);
  const [patientValue, setPatientValue] = useState();
  const [startTime, setStartTime] = useState(new Date());
  const [endTime, setEndTime] = useState(new Date());
  const [isLoading, setIsLoading] = useState(false);
  const [submitMessage, setSubmitMessage] = useState("");

  useEffect(() => {
    function docAvailLabel(obj) {
      return "Time Slot: " + new Date(obj.start_time).toLocaleString('en-US')
        + " - " + new Date(obj.end_time).toLocaleString('en-US')
        + ", Hospital: " + obj.doctor_hospital.hospital.hospital_name
        + ", Doctor: " + obj.doctor_hospital.doctor.first_name + " " + obj.doctor_hospital.doctor.last_name
        + ", Available: " + ((obj.is_available === true) ? "Yes" : "No");
    }

    async function populateDocAvail() {
      const resultdocAvails = await fetch(API_BASE_URL + "/doctoravailabilities/details/");    
      const bodyDocAvails = await resultdocAvails.json();
      const resultPatients = await fetch(API_BASE_URL + "/patients/");    
      const bodyPatients = await resultPatients.json();
      setDocAvail(bodyDocAvails.map((obj) => ({label: docAvailLabel(obj), value: obj.pk })));
      setPatient(bodyPatients.map((obj) => ({label: obj.first_name + " " + obj.last_name, value: obj.pk })));
    }
    populateDocAvail();
  }, []);

  const handleSubmit = async (event) => {
    setIsLoading(true);
    event.preventDefault();
    setSubmitMessage("");
    if (patientValue === undefined || docAvailValue === undefined) {
      setSubmitMessage("Please select a Patient and Doctor Availability Time Slot");
      setIsLoading(false);
      return
    }
    const result = await createAppointment(startTime, endTime, patientValue, docAvailValue);
    debugger
    if (result.status !== undefined && result.status !== 200) {
      setSubmitMessage("Unable to create Appointment" + JSON.stringify(result.data));
      setIsLoading(false);
      return;
    }
    await refetchAppointments();
    setSubmitMessage("Created Appointment: " + JSON.stringify(result));
    setIsLoading(false);
  };

  return (
    <>
      <h2>Create a new Appointment</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="patientSelec">Choose Patient:</label>
        <br />
        <select id="patientSelec" disabled={isLoading} onChange={(event) => setPatientValue(event.target.value)}>
            <option>Choose Patient</option>
            {patient.map((d) => <option key={d.label} value={d.value}>{d.label}</option>)}
        </select>        
        <br />        
        <label htmlFor="doctor-availabilities">Choose Doctor Availability:</label>
        <br />
        <select id="doctor-availabilities" disabled={isLoading} onChange={(event) => setDocAvailValue(event.target.value)}>
            <option>Choose Doctor Availability Slot</option>
            {docAvail.map((d) => <option key={d.label} value={d.value}>{d.label}</option>)}
        </select>        
        <br />
        <label htmlFor="start-time">Starts at:</label>
        <br />
        <DateTimePicker
          id="start-time"
          onChange={(val) => setStartTime(val)}
          value={startTime}
        />
        <br />
        <label htmlFor="end-time">Ends at:</label>
        <br />
        <DateTimePicker
          id="end-time"
          onChange={(val) => setEndTime(val)}
          value={endTime}
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

export default CreateAppointment;
