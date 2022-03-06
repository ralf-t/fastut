from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

# shared props


class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# data valdiation
class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


# response model
class ShowJob(JobBase):
    title: str
    company: str
    company_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]

    # to convert non dict obj to json
    class Config:
        orm_mode = True
