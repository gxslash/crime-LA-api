import pathlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a directory named 'data' if it doesn't already exist
pathlib.Path("../data").mkdir(exist_ok=True)

# Define the URL for the database connection
# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
# In this example, an SQLite database is used, and the database file is located at './data/sql_app.db'
SQLALCHEMY_DATABASE_URL = 'sqlite:///./data/sql_app.db'

# Create an engine for connecting to the database
# In this case, 'check_same_thread' is set to False for SQLite to allow multiple threads to access the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Create a sessionmaker for the database session
# 'bind=engine' specifies that the session should be bound to the engine created earlier
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

def get_db():
    """
    Returns a database session. The function is a generator that yields the session.
    
    Yield:
        db (SessionLocal): database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()