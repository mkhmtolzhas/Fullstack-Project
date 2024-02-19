from pydantic import BaseModel


class TourCreate(BaseModel):
    id: int
    user_name: str
    tour_name: str
    price: int