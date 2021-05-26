from typing import Dict

from pydantic import BaseModel, EmailStr


# Shared properties
class TimeframesBase(BaseModel):
    pass


class TimeframesInDBBase(TimeframesBase):
    pass


# Additional properties to return via API
class Timeframes(TimeframesInDBBase):
    timeframes: Dict = {}
