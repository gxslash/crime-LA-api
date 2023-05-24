from .. import schemas, crud, utils, oauth2
from ..database import get_db
from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

# Handling POST request to '/auth'
@router.post("/", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Handling GET request to '/auth/<id>'
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id=id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id {id} could not be found')
    return user

# Handling POST request to '/auth/login'
@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    user = crud.login(db, user_credentials.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')
    if utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')
    
    access_token = oauth2.create_access_token(data={'user_id': user.id})
    return {'access_token': access_token, 'token_type': 'bearer'}
