import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "9844066"))
    API_HASH = os.environ.get("API_HASH", "0d3f74056f1e60388d3317548799ee17")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5497733823:AAHBv2vxkQzkmgdpH3ylXt9yrXTkzBvWD34")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1770455672")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQC_XBYQP9g0djaM_u1CyQ43Kx_xBaskQ_XuILVDwjH5eGej8qFwC226FvG5jz78RnwbK04-iVTuMTU6OfhBxasJeKgk1GjqHM4GecPiGdBYLjRVnLuiJ1G4PdD_eXQJdrlVNGecdr0431G7PUPgo9q0YdswC9Gg4QYb03fnlB4P9SUpYoOwjC-cS7B96rA7Mg2NMOtPYw9qyUnrkPJYhw9maFRfUouqh2zZfb94LB5krQGoMYbt_S5-pZwCwAYtoInn93nLKI2ApZI9C7tj5ExWLoRLjbRJWDhp6XorNM33vE5KwUkIUmfrtbZXc4uEfLcEJqQNPEjSzUllLxe6fkqHaYcCeAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001809830643"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@TG_fileforward5bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
