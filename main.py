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
    Skin(name="AK-47 | Redline", image_url="dragonlore.png", price_idr=250000),
    Skin(name="AWP | Dragon Lore", image_url="howl.png", price_idr=1500000),
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
