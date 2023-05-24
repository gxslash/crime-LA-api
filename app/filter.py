from typing import Optional
from datetime import datetime
from dataclasses import dataclass

@dataclass
class CrimeFilter:
    limit: int = 10
    after: int = 0
    area: Optional[int] = None
    area_name: Optional[str] = None
    start_day: Optional[int] = None
    start_month: Optional[int] = None
    start_year: Optional[int] = None
    end_day: Optional[int] = None
    end_month: Optional[int] = None
    end_year: Optional[int] = None
    crm_cd: Optional[int] = None 
    crm_cd_desc: Optional[int] = None
    mocodes: Optional[str] = None
    vict_age: Optional[int] = None
    vict_start_age: Optional[int] = None
    vict_end_age: Optional[int] = None
    vict_descent: Optional[str] = None
    vict_sex: Optional[str] = None
    weapon_used_cd: Optional[str] = None
    weapon_desc: Optional[int] = None
    north_frontier: Optional[float] = None # north
    east_frontier: Optional[float] = None # east
    south_frontier: Optional[float] = None # south
    west_frontier: Optional[float] = None # west

    def start_date(self):
        return datetime(self.start_year, self.start_month, self.start_day)
    
    def end_date(self):
        return datetime(self.end_year, self.end_month, self.end_day)