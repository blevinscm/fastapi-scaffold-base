from pydantic import BaseSettings
class Settings(BaseSettings):
    uri: MONGO_URL
    


settings = Settings()