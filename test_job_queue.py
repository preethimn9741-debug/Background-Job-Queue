import job_queue
from unittest.mock import patch


def test_job_runs_successfully():
    job = job_queue.Job(1, "EMAIL")

    with patch("job_queue.time.sleep", return_value=None):
        job.run()

    assert job.status == "DONE"


def test_job_initial_status_is_pending():
    job = job_queue.Job(2, "REPORT")

    assert job.status == "PENDING"


def test_job_with_none_id():
    job = job_queue.Job(None, "EMAIL")

    with patch("job_queue.time.sleep", return_value=None):
        job.run()

    assert job.status == "DONE"


def test_job_with_empty_type():
    job = job_queue.Job(3, "")

    with patch("job_queue.time.sleep", return_value=None):
        job.run()

    assert job.status == "DONE"


def test_job_with_numeric_type():
    job = job_queue.Job(4, 123)

    with patch("job_queue.time.sleep", return_value=None):
        job.run()

    assert job.status == "DONE"


def test_job_sleep_failure_sets_failed_status():
    job = job_queue.Job(5, "BACKUP")

    with patch("job_queue.time.sleep", side_effect=Exception("Sleep failed")):
        job.run()

    assert job.status == "FAILED"


def test_job_run_called_multiple_times():
    job = job_queue.Job(6, "EMAIL")

    with patch("job_queue.time.sleep", return_value=None):
        job.run()
        job.run() 

    assert job.status == "DONE"


def test_multiple_jobs_one_fails():
    jobs = [
        job_queue.Job(7, "EMAIL"),
        job_queue.Job(8, "REPORT"),
        job_queue.Job(9, "BACKUP")
    ]

    with patch("job_queue.time.sleep", side_effect=[None, Exception("Fail"), None]):
        jobs[0].run()
        jobs[1].run()
        jobs[2].run()

    assert jobs[0].status == "DONE"
    assert jobs[1].status == "FAILED"
    assert jobs[2].status == "DONE"


def test_job_status_never_remains_running():
    job = job_queue.Job(10, "SYNC")

    with patch("job_queue.time.sleep", return_value=None):
        job.run()

    assert job.status != "RUNNING"


def test_job_object_without_run_call():
    job = job_queue.Job(11, "EMAIL")

    assert job.status == "PENDING"


def test_job_handles_unexpected_exception():
    job = job_queue.Job(12, "UPLOAD")

    with patch("job_queue.time.sleep", side_effect=RuntimeError("Unexpected error")):
        job.run()

    assert job.status == "FAILED"
