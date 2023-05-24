from pydantic import BaseSettings

# Create a settings class that inherits from BaseSettings provided by Pydantic
class Settings(BaseSettings):
    # Define the configuration settings as class attributes
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        # Set the environment file to be used for loading the configuration settings
        env_file = ".env"

# The settings will be loaded from the environment variables defined in the .env file
settings = Settings()