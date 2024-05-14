from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Skin(BaseModel):
    name: str
    image_url: str
    price_idr: int

# Mocked data for CS:GO skins
mocked_skins = [
    Skin(name="AK-47 | Redline", image_url="howl.png", price_idr=250000),
    Skin(name="AWP | Dragon Lore", image_url="dragonlore.png", price_idr=1500000),
    Skin(name="Deagle | Hypnotic", image_url="hypnotic.png", price_idr=50000),
    Skin(name="AWP | Lighting Strike", image_url="lightingstrike.png", price_idr=100000),
    Skin(name="AK-47 | Case Hardened", image_url="casehardened.png", price_idr=120000),
    Skin(name="GLOCK | Dragon Tatto", image_url="dragontatto.png", price_idr=70000),
    Skin(name="USP | Dark Water", image_url="darkwater.png", price_idr=75000),
    Skin(name="AUG | Wings", image_url="wings.png", price_idr=90000),
    Skin(name="M4A4 | Jungle Tiger", image_url="jungletiger.png", price_idr=40000),
    Skin(name="AK-47 | Blood Sport", image_url="bloodsport.png", price_idr=600000),
    Skin(name="AK-47 | Red Laminate ", image_url="redlaminate.png", price_idr=300000),
    Skin(name="AWP | Gungnir ", image_url="gungnir.png", price_idr=500000),
    Skin(name="AK-47 | Wild Lotus", image_url="wildlotus.png", price_idr=125000),
    Skin(name="AK-47 | Phantom Disruptor", image_url="phantomdiruptor.png", price_idr=95000),
    Skin(name="AK-47 | Night Wish", image_url="nightwish.png", price_idr=110000),
    Skin(name="M4A1-S | Decimator", image_url="decimator.png", price_idr=440000),
    # Add more skins here
]

@app.get("/")
def read_root():
    return {"message": "CS:GO Skin API"}

@app.get("/skins/", response_model=List[Skin])
def get_skins():
    return mocked_skins

@app.get("/skins/{skin_id}", response_model=Skin)
def get_skin(skin_id: int):
    if 0 <= skin_id < len(mocked_skins):
        return mocked_skins[skin_id]
    else:
        return {"error": "Skin not found"}
