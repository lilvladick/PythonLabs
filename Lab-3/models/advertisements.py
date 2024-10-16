from pydantic import BaseModel

class AdvertisementsRequest(BaseModel):
    title: str
    description: str | None = None
    price: float
    category: str
    seller_contacts: str

class Advertisements:
    title: str
    description: str | None = None
    price: float
    category: str
    seller_contacts: str