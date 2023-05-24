from . import schemas, utils
from .filter import CrimeFilter
from .models import Crime, User
from sqlalchemy import func
from sqlalchemy.orm import Session

LIMIT = 25

def get_crimes(db: Session, params: CrimeFilter):
    query = db.query(Crime)
    if params.area is not None:
        query = query.filter(Crime.area == params.area)
    if params.area_name is not None:
        query = query.filter(Crime.area_name == params.area_name)
    if params.crm_cd is not None:
        query = query.filter(Crime.crm_cd == params.crm_cd)
    if params.crm_cd_desc is not None:
        query = query.filter(Crime.crm_cd_desc.contains(params.crm_cd_desc))
    if params.mocodes is not None:
        query = query.filter(Crime.mocodes.contains(params.mocodes))
    if params.vict_age is not None:
        query = query.filter(Crime.vict_age == params.vict_age)
    else:
        query = query.filter(Crime.vict_age.between(params.vict_start_age, params.vict_end_age))
    if params.vict_sex is not None:
        query = query.filter(Crime.vict_sex == params.vict_sex)
    if params.vict_descent is not None:
        query = query.filter(Crime.vict_descent == params.vict_descent)
    if params.weapon_used_cd is not None:
        query = query.filter(Crime.weapon_used_cd == params.weapon_used_cd)
    if params.weapon_desc is not None:
        query = query.filter(Crime.weapon_desc.contains(params.weapon_used_cd))
    if params.limit > 25:
        params.limit = 25
    query = query.filter(Crime.lat.between(params.south_frontier, params.north_frontier)
                        ).filter(Crime.lon.between(params.west_frontier, params.east_frontier)
                        ).filter(Crime.date_rptd.between(params.start_date(), params.end_date())
                        ).order_by(Crime.id
                        ).offset(params.after
                        ).limit(params.limit)
    return query.all()

def get_crime_codes(db: Session):
    return db.query(Crime.crm_cd, Crime.crm_cd_desc).group_by(Crime.crm_cd)

def get_areas(db: Session):
    return db.query(Crime.area, Crime.area_name).group_by(Crime.area)

def get_premis_codes(db: Session):
    return db.query(Crime.premis_cd, Crime.premis_desc).group_by(Crime.premis_cd)

def get_weapon_codes(db: Session):
    return db.query(Crime.weapon_used_cd, Crime.weapon_desc).group_by(Crime.weapon_desc)

def get_mocodes(db: Session):
    pass

def create_crime(db: Session, crime: schemas.CrimeCreate):
    db_crime = Crime(**crime.dict())
    db.add(db_crime)
    db.commit()
    db.refresh(db_crime)
    return db_crime

def create_user(db: Session, user: schemas.UserCreate):
    user.password = utils.hash(user.password)
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def login(db: Session, user_credentials: schemas.UserLogin):
    return db.query(User).filter(User.email == user_credentials.email).first()

"""Below part is not done yet"""

def get_crime_map(db: Session):
    return db.query(Crime).all()

def get_most_guilty_area(db: Session):
    return None

def get_sex_distribution(db: Session, area):
    return None

