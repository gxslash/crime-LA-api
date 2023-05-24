# Importing Modules
from .. import schemas, crud
from ..database import get_db
from ..filter import CrimeFilter
from ..oauth2 import get_current_user
from typing import List
from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from datetime import datetime

# Creating API Router
router = APIRouter(prefix='/crimes', tags=['Crimes'])

now = datetime.now()

# Handling GET request to '/crimes'
@router.get('/', response_model=List[schemas.Crime])
def get_crimes(
    db: Session = Depends(get_db),
    limit: int = 25,
    after: int = 0,
    area: int = None,
    area_name: str = None,
    start_day: int = 1,
    start_month: int = 1,
    start_year: int = 2019,
    end_day: int = now.day,
    end_month: int = now.month,
    end_year: int = now.year,
    crm_cd: int = None,
    crm_cd_desc: str = None,
    mocodes: str = None,
    vict_age: int = None,
    vict_start_age: int = 0,
    vict_end_age: int = 99,
    vict_descent: str = None,
    vict_sex: str = None,
    weapon_used_cd: str = None,
    weapon_desc: int = None,
    north: float = 42.081696,
    east: float = -109.762266,
    south: float = 31.353709,
    west: float = -124.345182,
):
    params = CrimeFilter(limit=limit,
                         after=after,
                         area=area,
                         area_name=area_name,
                         start_day=start_day,
                         start_month=start_month,
                         start_year=start_year,
                         end_day=end_day,
                         end_month=end_month,
                         end_year=end_year,
                         crm_cd=crm_cd,
                         crm_cd_desc=crm_cd_desc,
                         mocodes=mocodes,
                         vict_age=vict_age,
                         vict_start_age=vict_start_age,
                         vict_end_age=vict_end_age,
                         vict_sex=vict_sex,
                         vict_descent=vict_descent,
                         weapon_used_cd=weapon_used_cd,
                         weapon_desc=weapon_desc,
                         north_frontier=north,
                         east_frontier=east,
                         south_frontier=south,
                         west_frontier=west
                         )
    crimes = crud.get_crimes(db, params)
    return crimes

# Handling GET request to '/crimes/crm_cd'
@router.get('/crm_cd')
def get_crime_codes(db: Session = Depends(get_db)):
    return crud.get_crime_codes(db)

# Handling GET request to '/crimes/areas'
@router.get('/areas')
def get_areas(db: Session = Depends(get_db)):
    return crud.get_areas(db)

# Handling GET request to '/crimes/premis'
@router.get('/premis')
def get_premis_codes(db: Session = Depends(get_db)):
    return crud.get_premis_codes(db)

# Handling GET request to '/crimes/weapons'
@router.get('/weapons')
def get_weapons(db: Session = Depends(get_db)):
    return crud.get_weapon_codes(db)

# Handling POST request to '/crimes' with user authentication
@router.post('/',
             response_model=schemas.Crime,
             status_code=status.HTTP_201_CREATED)
def create_crimes(crime: schemas.CrimeCreate, db: Session = Depends(get_db), curr_user: schemas.UserOut = Depends(get_current_user)):
    return crud.create_crime(db=db, crime=crime)
