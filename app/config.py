from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the database URL (use an SQLite database for simplicity)
DATABASE_URL = "sqlite:///hospital_management.db"

# Create the engine and session
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Create all tables in the database (only needs to be run once)
def create_db():
    Base.metadata.create_all(engine)

# Create a session to interact with the database
def get_session():
    return Session()
