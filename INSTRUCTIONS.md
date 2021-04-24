# Instructions

For this project, you'll be building a simple system which allows patients to book appointments with clinicians.

After following the setup instructions, you'll be able to see a very simple view of appointment slots in your browser.

Here's what is currently in the repo:

**Back-end**

The [/backend](/backend/README.md) subdirectory contains:

- A working Django / Django REST Framework server
- A Clinician model, which represents a member of the Firefly clinical team
- An Availability model, which represents availability time slots
- An Appointment model, which represents availability time slots for a clinician which is either already booked
  or is available for booking
- Endpoints for listing all of the clinicians, availabilities and appointments

**Front-end**

The [/frontend](/frontend/README.md) subdirectory contains:


- A working create-react-app server with axios
- A React component which displays a simple view of all availabilities


Both subdirectories contain a README with more detailed instructions for getting the server and front-end UI up and running.

To complete this project, you'll add a few more features:
- Booked Appointments need to be associated with a patient
- The user should be able to see which availability slots are available for booking
- The user should be able to book an available appointment slot for a patient and clinician combination
- The user should be able to see booked appointments for a given clinician, date and patient combination
- Finally, the user should be able to cancel a booked appointment.



Good luck!
