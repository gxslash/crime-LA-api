from .database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Crime(Base):
    __tablename__ = 'crimes'

    id = Column(Integer, primary_key=True, nullable=False)
    dr_no = Column(Integer, nullable=False)
    date_rptd = Column(TIMESTAMP(timezone=True), nullable=False)
    date_occ = Column(TIMESTAMP(timezone=True), nullable=False) 
    time_occ = Column(Integer,  nullable=False)
    area = Column(Integer,  nullable=False)
    area_name = Column(String,  nullable=False)
    rpt_dist_no = Column(Integer,  nullable=False)
    part_1_2 = Column(Integer,  nullable=False) 
    crm_cd = Column(Integer,  nullable=False)
    crm_cd_desc = Column(String,  nullable=False) 
    mocodes = Column(String,  nullable=True)
    vict_age = Column(Integer,  nullable=False) 
    vict_sex = Column(String,  nullable=True) 
    vict_descent = Column(String,  nullable=True)
    premis_cd = Column(Float,  nullable=True)
    premis_desc = Column(String,  nullable=True)
    weapon_used_cd = Column(Float,  nullable=True)
    weapon_desc = Column(String,  nullable=True)
    status = Column(String,  nullable=False)
    status_desc = Column(String,  nullable=False)
    crm_cd_1 = Column(Float,  nullable=True)
    crm_cd_2 = Column(Float,  nullable=True)
    crm_cd_3 = Column(Float,  nullable=True)
    crm_cd_4 = Column(Float,  nullable=True)
    location = Column(String,  nullable=False)
    cross_street = Column(String,  nullable=True)
    lat = Column(Float,  nullable=False)
    lon = Column(Float,  nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=True, server_default=text('CURRENT_TIMESTAMP'))

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


