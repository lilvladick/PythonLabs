from pydantic import BaseModel

class Advertisements(BaseModel):
    id: int
    title: str
    description: str | None = None
    price: float
    category: str
    images: list[str] = []
    seller_contacts: str