# Instructions

For this project, you'll be building a simple system which allows patients to book appointments with clinicians.

After following the setup instructions, you'll be able to see a very simple view of appointment slots in your browser.

To complete this project, you'll add a few more features:

- The user should be able to see which availability slots are available for booking
- The user should be able to book an available slot for an appointment
- The user should be able to see which appointments they have booked
- Finally, the user should be able to cancel a booked appointment.


Here's what is currently in the repo:

**Back-end**

The [/backend](/backend/README.md) subdirectory contains:

- A working Django / Django REST Framework server
- A Clinician model, which represents a member of the Firefly clinical team
- An Availability model, which represents an individual clinician's availability time slots
- An endpoint for listing all of the clinicians

**Front-end**

The [/frontend](/frontend/README.md) subdirectory contains:


- A working create-react-app server with axios
- A React component which displays a simple view of all availabilities


Both subdirectories contain a README with more detailed instructions for getting the server and front-end UI up and running.

Good luck!