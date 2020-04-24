# Firefly Health Take Home Interview

Hello and welcome to Firefly Health's Take Home Interview!

In this repo is the scaffolding to a simple system for patients to book appointments with clinicians.

Here's what is currently in the repo

**Back End**

- A working Django / Django Rest Framework server, with storage in SQLite3
- A Clinician Django Model, for tracking clinicans
- An Availability Django Model, for tracking available time slots for a specific clinician
- An endpoint for listing all of the clinicians

**Front End**

- A working create-react-app server with axios

You can find detailed READMEs for the back end and front end codebases within their respective subdirectories: [backend](/backend/README.md) and [frontend](/frontend/README.md)

---

Unfortunately, it's not complete, and there are some features that need to be added.

Specifically:

- The user should be able to see which availability slots are open for booking
- The user should then be able to book a slot for an appointment
- The user should be able to see which appointments they have booked
- Finally, the user should be able to cancel a booked appointment.

This challenge will require creating new Django Models, creating new React Components, and creating new endpoints, among other things.

Good luck!
