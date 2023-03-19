import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "9844066"))
    API_HASH = os.environ.get("API_HASH", "0d3f74056f1e60388d3317548799ee17")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5757059757:AAEvjvpv1gmn8xHGAONAiTEjEbN7OaHwka8")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1770455672")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQBjkuJOoou0FaHTDZQOzyumxdBjkCbod-8k8VovcqnOCAzNGmV6rq1Pisl7JyiZFvfcNcM-KSgFjK67M799mLZUzxbSTzd94knCID-2oWd8NUkiuo6cvi1aDCRQmv53gOuLyQ-wdXajPJrmS2YgZLM7M-kkVXHhN2dZB4e6SUSjnkhVCjsfRuzpFArXxwrU5-tPJR77UIdJ5rYGGqoZmzUjWyuSYWF3hWh-tvTQeJb919hPTz6Qfm7LMBlxN54oY4-d5QjaMLQazKeIqjuElAASW6nbLec2L3mJzaakkTc3nGToMWz5sGGk4fGaqL61SrdxGAsUgPcDgvbdoH-EJK6daYcCeAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001809830643"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "TG_fileforward2bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
