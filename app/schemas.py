from pydantic import BaseModel


class EventData(BaseModel):

    latitude: float
    longitude: float

    event_type: str
    event_cause: str

    authenticated: str
    veh_type: str

    police_station: str
    zone: str
    junction: str
    corridor: str

    requires_road_closure: bool

    hour: int

    day_of_week: str
    month: str

    is_weekend: bool
    is_peak_hour: bool

    event_category: str