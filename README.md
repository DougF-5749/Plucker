# 🐦 Plucker 🐦
A comedic bird identification app (with a twist) created as a **two-week**, **choose-anything** project during the final phase of **Makers Academy bootcamp**. Our group wanted to **consolidate our learnings**, especially around back-end/ front-end integration and asynchronous Python.

 ⚠️ _**The creators of this app do not actually condone cooking random birds (no matter how tasty they look). Read on for more context...**_ ⚠️

## Table of Contents
1. [Overview](#overview)
2. [Context and Motivation](#context-and-motivation)
3. [Features](#features)
4. [Tech Stack](#tech-stack)
5. [Installation & Setup](#installation-and-setup)
6. [Impactful Commits](#impactful-commits)
7. [Contributors](#contributors)

## Overview
Plucker allows users to upload photos of birds, record sightings (species, location), and provides a randonly selected recipe for that bird. 

This project helped us bridge the gap between frontend and backend, practice asynchronous Flask usage, and experiment with building a more robust application than our previous bootcamp projects.

## Context and Motivation
- We had **two weeks** to create _anything_ we wanted.
  
- As a group, we decided to **focus on technologies** or concepts we felt we **hadn’t fully mastered** (e.g., concurrency, async in Python).
  
- Our **original plan** included uploading images to a Google Image API for auto-identification, plus using GPS services for location data.
  - **MVP Approach**: For this two-week sprint, we scaled back: the user manually enters the bird’s name and location.
  - **Tasty Feature**: Generates a “recipe” (again, do not condone...) for the bird every time a new sighting is recorded.

- **Async & Concurrency**: We wanted to adapt our Flask app (originally a WSGI) to handle **async requests** from the JavaScript frontend by using Hypercorn (an ASGI server) and asyncio.
  - This was **challenging** since Flask itself is not inherently ASGI, but I **learned a lot** about **WSGI vs. ASGI frameworks**.
  
- My frontend involvement was relatively light as I was the main contributor for the backend of the app.
  
- We prioritised learning asynchronous back-end techniques and ensuring some test coverage.
  
- **Test coverage** is decent on the backend, though not 100%. That’s an area for future improvement.

## Features
- **Bird Sighting Recording**: Users can create new sightings, specifying the bird species and location.
  
- **Random Recipe Generato**r: On each upload, the app returns a comedic “recipe” (do not try at home!).
  
- **Frontend / Backend Integration**: With React on the client side and a Python/Flask server, data flows asynchronously.
  
- **Async**: Used Hypercorn and asyncio to handle concurrency, even though Flask is traditionally synchronous.
  
- **PostgreSQL**: Robust relational DB to store sighting data.
  
- **Group Collaboration**: Employed agile methodologies (kanban boards, daily stand-ups, pair programming) over the two-week timeframe.

## Tech Stack

| Technology  | Purpose                                      |
|:------------|:----------------------------------------------|
| Python     | Main programming language (backend)        |
| Flask      | Web framework (adapted for async)          |
| React      | Front-end library for building the UI      |
| PostgreSQL | Database for storing bird sightings       |
| Hypercorn  | ASGI server to run async Flask            |
| asyncio    | Enables concurrency in Python/Flask       |

## Installation and Setup

1️⃣ Clone the repository (your fork):

```bash
git clone https://github.com/<your-username>/plucker.git
cd plucker
```

2️⃣ Set up the backend:

- Install Python 3 and PostgreSQL if you don’t have them already.

- Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```
- Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Configure the database:

- Create a local PostgreSQL DB (e.g., plucker).
- Update config or .env variables to point to your DB (username, password, etc.).

4️⃣ Set up the front-end:

- Navigate to the frontend folder:

```bash
cd client
npm install
```

5️⃣ Run the application:

- Backend:
```bash
hypercorn app:app --reload
```
- Frontend:
```bash
npm start
```
- Access the app in your browser at http://localhost:3000 (or whichever port you configured).

## Impactful Commits
Coming Soon!

## Contributors

- [Doug Fairfield](https://github.com/DougF-5749)
- [Russell Coles](https://github.com/RussellColes)
- [Ben Cole](https://github.com/benawcole)
- [Alberto Tobarra](https://github.com/altota90)
- [Max Joseph](https://github.com/maxjoseph22)
- [John Hertility](https://github.com/JohnHertility)

This was our final group project at Makers Academy—thanks to all contributors, mentors, and the Makers community for the support!

## 📜 Licence 📜

MIT Licence coming soon.

