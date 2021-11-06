const AppointmentsList = ({ appointments }) => {
  return (
    <>
      <h2>Appointments</h2>
      <p>{appointments.length} appointment(s)</p>
        <ul>
          {appointments.map((patient) => {
            return <li key={patient.pk}><b>Patient :</b> <b>{patient.patient.first_name} {patient.patient.last_name}</b>
            <br/><b>Slot :</b> <i>{new Date(patient.start_time).toLocaleString('en-US')}</i> to <i>{new Date(patient.end_time).toLocaleString('en-US')}</i>
            <br/><b>Doctor :</b> <i>{patient.doctor_availability.doctor_hospital.doctor.first_name} {patient.doctor_availability.doctor_hospital.doctor.last_name}</i>
            <br/><b>Hospital :</b> <i>{patient.doctor_availability.doctor_hospital.hospital.hospital_name}</i></li>;
          })}
        </ul>
    </>
  );
};

export default AppointmentsList;
