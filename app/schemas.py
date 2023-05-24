from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Union, Optional

class CrimeBase(BaseModel):
    dr_no: int
    date_rptd: datetime
    date_occ: datetime 
    time_occ: int
    area: int
    area_name: str
    rpt_dist_no: int 
    part_1_2: int 
    crm_cd: int
    crm_cd_desc: str 
    mocodes: Union[str, None]
    vict_age: int 
    vict_sex: Union[str, None] 
    vict_descent: Union[str, None]
    premis_cd: Union[float, None]
    premis_desc: Union[str, None]
    weapon_used_cd: Union[float, None]
    weapon_desc: Union[str, None]
    status: str
    status_desc: str
    crm_cd_1: Union[float, None]
    crm_cd_2: Union[float, None]
    crm_cd_3: Union[float, None]
    crm_cd_4: Union[float, None]
    location: str
    cross_street: Union[str, None]
    lat: float
    lon: float
    
class CrimeCreate(CrimeBase):
    pass

class Crime(CrimeCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr
    

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None