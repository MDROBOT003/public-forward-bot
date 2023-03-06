import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "9844066"))
    API_HASH = os.environ.get("API_HASH", "0d3f74056f1e60388d3317548799ee17")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5162572062:AAEvGeB0qoU7y7E7Jei6Ow6Pw4Eq7RsunKs")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1770455672")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQCASQT-Cd6Mku-9UzfinQCP7O5X36Sa7Fr-DImTFV7iXhFY1feE0Jjc84_VEzDpDzaDdQRfB-__KQbSJb2i7lQN3g13bwHbSe0PbmXToPv7SU1x0xUdQWEfUtGtZ-BR9zkCevyNEsjAkEy-6Xe8F9_tW2TeODApQ4RruVv4IuPLUwUCVqmbMUTUVihuGgGyuwXCRxoG2fCFpvkV-9ItypSjp-YEXNdJ_M9MLNV53D4exTNPjuaNjsXr3HY7jJ2nU1_AB7mvL4aD76Dix2YvXG5Cyo3HQ_4fB_Zgx0kX_LhAT-2D2ciNczgW61OMoVeD_DZ0HxpXeMdr7M7bloNOVB-iaYcCeAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001809830643"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "TG_fileforwardbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
