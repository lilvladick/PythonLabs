from pydantic import BaseModel

class AdvertisementsRequest(BaseModel):
    title: str
    description: str | None = None
    price: float
    category: str
    seller_contacts: str

class Advertisements:
    def __init__(self, title, description, price, category, seller_contacts):
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.seller_contacts = seller_contacts