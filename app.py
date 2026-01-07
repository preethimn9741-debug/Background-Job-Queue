from flask import Flask, jsonify, request, render_template
from database import SessionLocal, JobModel
import job_queue

app = Flask(__name__)

@app.route("/")
def home():
    return "Job Queue Web App Running"


@app.route("/jobs", methods=["POST"])
def create_job():
    data = request.json
    session = SessionLocal()

    job = JobModel(
        id=data["id"],
        job_type=data["type"],
        status="PENDING"
    )

    session.add(job)
    session.commit()
    return jsonify({"message": "Job created"})


@app.route("/jobs", methods=["GET"])
def get_jobs():
    session = SessionLocal()
    jobs = session.query(JobModel).all()

    return jsonify([
        {"id": j.id, "type": j.job_type, "status": j.status}
        for j in jobs
    ])


@app.route("/jobs/<int:job_id>/run", methods=["POST"])
def run_job(job_id):
    session = SessionLocal()
    db_job = session.query(JobModel).filter_by(id=job_id).first()

    if not db_job:
        return jsonify({"error": "Job not found"}), 404

    job = job_queue.Job(db_job.id, db_job.job_type)
    job.run()

    db_job.status = job.status
    session.commit()

    return jsonify({"status": job.status})


@app.route("/ui")
def ui():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
