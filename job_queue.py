import json
import time

class Job:
    def __init__(self, job_id, job_type):
        self.id = job_id
        self.type = job_type
        self.status = "PENDING"

    def run(self):
        
        try:
            self.status = "RUNNING"
            print(f"Job {self.id} ({self.type}) is RUNNING")

            time.sleep(2)  
            self.status = "DONE"
            print(f"Job {self.id} ({self.type}) is DONE")

        except Exception:
            self.status = "FAILED"
            print(f"Job {self.id} ({self.type}) FAILED")

with open("jobs.json") as f:
    jobs_data = json.load(f)

jobs = [Job(j["id"], j["type"]) for j in jobs_data]

for job in jobs:                                   
    job.run()                                                                                                       
