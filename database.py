from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///jobs.db")
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class JobModel(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    job_type = Column(String)
    status = Column(String)

Base.metadata.create_all(engine)
