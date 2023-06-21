from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Potrawa(BaseModel):
    nazwa: str
    cena: float

class ZamowItem(BaseModel):
    potrawa: Potrawa
    ilosc: int

class Zamowienie(BaseModel):
    items: list[ZamowItem]

zamowienia = []

@app.get("/zamowienia")
def get_zamowienie():
    return zamowienia

@app.post("/zamowienie")
def zloz_zamowienie(zamowienie: Zamowienie):
    total_price = 0.0
    for item in zamowienie.items:
        cena += item.potrawa.cena * item.ilosc

    zamowienie_info = {
        "items": zamowienie.items,
        "total_price": total_price
    }

    zamowienia.append(zamowienie_info)
    return {"message": "Zamówienie złożone"}
