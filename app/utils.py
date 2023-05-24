from passlib.context import CryptContext # pip install passlib[bcrypt]

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(password: str):
    # hash the password - user.password
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)