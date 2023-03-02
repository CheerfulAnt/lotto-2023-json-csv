from dotenv import dotenv_values
from pydantic import BaseModel

config = {
    **dotenv_values('.env.secret'),
    **dotenv_values('.env.shared')
}

# Casting configuration variables from strings.


class ConfigCast(BaseModel):
    # .env.shared
    LOG_SIZE: int
    LOG_COUNT: int
    EXCEPTION_SHOW: bool
    EMAIL_ERROR_LOG: bool
    EMAIL_EVENT_LOG: bool
    # .env.secret
    EMRE_SMTP_PORT: int


config_cast = ConfigCast(**config)

config.update(config_cast)
