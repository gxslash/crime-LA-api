# Importing Modules
from .routers import crime, auth  
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

# Creating the FastAPI Application
app = FastAPI()

# Configuring CORS
origins = ['*']  # Allowing requests from any domain

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allowing credentials (e.g., cookies, authorization headers)
    allow_methods=['*'],  # Allowing all HTTP methods (GET, POST, DELETE, PUT, etc.)
    allow_headers=['*']  # Allowing all headers
)

# Including Routers
app.include_router(crime.router)
app.include_router(auth.router)

# Defining Root Endpoint
@app.get('/')
def root():
    return {'message': 'API for Los Angeles Crime Data Committed Between 2020 and 2023. To use the API, please check out the documentation.'}
    # Returning a JSON response with a message about the purpose of the API
