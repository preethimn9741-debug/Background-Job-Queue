# background-job-queue

## Project Description
A simple **Background Job Queue system** built using **Python**, extended into a **Flask web application** with a **database-backed CRUD API** and an **interactive web UI**. 
The project also includes **robust unit tests with multiple negative scenarios**.

## Core Job Queue
- Job lifecycle management (`PENDING → RUNNING → DONE / FAILED`)
- Handles job failures gracefully
- Supports multiple jobs execution
- Extensive **negative test cases**

## Web Application
- Flask-based backend
- REST APIs for job management
- Interactive UI using HTML & JavaScript

## Database Integration
- SQLite database
- Persistent job storage
- CRUD operations:
  - Create Job
  - View Jobs
  - Run Job
  - Update Job Status

 ## Testing
- Pytest-based unit tests
- Mocking (`time.sleep`) for fast execution
- Covers positive & negative scenarios

  ## Project Structure

  background_jobs/
  
│── app.py # Flask web app

│── job_queue.py # Job logic

│── database.py # Database initialization

│── jobs.json # Sample job input

│── requirements.txt

├── templates/

│ └── index.html # UI

├── static/

│ └── script.js # JavaScript

├── tests/

│ └── test_job_queue.py # Unit tests (positive & negative)

└── venv/

## ONE-TERMINAL INSTALLATION & RUN COMMANDS

1. Go to project folder

cd C:\background_jobs

2. Create virtual environment

python -m venv venv

3. Activate virtual environment

venv\Scripts\activate

4. Install required packages

pip install flask sqlalchemy pytest

5. (Optional) Save dependencies

pip freeze > requirements.txt

6. Run unit tests

python -m pytest

7. Run Flask application

python app.py

8. Run Unit Tests (Optional but Recommended)

python -m pytest

## Run the Flask Application

python app.py

## Open in Browser

http://127.0.0.1:5000/ui

## output

Press CTRL+C to quit

 * Restarting with stat
Job 1 (email) is RUNNING
Job 1 (email) is DONE
Job 2 (report) is RUNNING
Job 2 (report) is DONE
Job 3 (cleanup) is RUNNING
Job 3 (cleanup) is DONE
 * Debugger is active!
 * Debugger PIN: 176-985-022

## Terminal output screenshort
<img width="1259" height="493" alt="Screenshot 2026-01-06 155951" src="https://github.com/user-attachments/assets/69e04b7f-6603-4025-8f1a-80320cd3d833" />

## Conclusion

This project implements a background job queue system using Python and Flask.

It includes database-backed CRUD operations and an interactive web interface.

Automated unit tests ensure reliable job execution and error handling.

Overall, the project demonstrates real-world backend development practices.






