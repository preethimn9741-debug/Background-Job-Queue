# background-job-queue
## Project Description

This project simulates a **basic job queue system** using Python.
It reads a list of jobs from a JSON file and executes them one by one, updating and printing their status.

---

## Files
- `job_queue.py` – Main job processing script
- `jobs.json` – Input file containing job details
- `README.md` – Project documentation

---

## How the Script Works

1. Loads job data from `jobs.json`
2. Creates a Job object for each entry
3. Each job starts with status `PENDING`
4. Jobs are executed sequentially
5. During execution, job status changes to:
   - `RUNNING`
   - `DONE` (after completion)
6. Job status is printed to the console

---

## Job Structure
Each job in `jobs.json` contains:
- `id` – Job identifier
- `type` – Type of job (example: email, report, cleanup)

---

## How to Run

python job_queue.py

Output

Job 1 (email) is RUNNING
Job 1 (email) is DONE





