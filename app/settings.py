from app.exceptions import ConfigurationError

MODEL_NAME = "gpt-5.5"

TEMPERATURE = 0.7

MAX_OUTPUT_TOKENS = 500

def validate_settings():
    if not 0 <= TEMPERATURE <= 2:
        # raise ValueError(
        raise ConfigurationError(    
            "TEMPERATURE must be between 0 and 2."
        )