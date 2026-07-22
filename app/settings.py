from app.exceptions import ConfigurationError

MODEL_NAME = "gpt-5.5"

TEMPERATURE = 0.7

MAX_OUTPUT_TOKENS = 500

def validate_settings():

    if not MODEL_NAME.strip():
        raise ConfigurationError(
            "MODEL_NAME cannot be empty."
        )

    if not 0 <= TEMPERATURE <= 2:
        raise ConfigurationError(
            "TEMPERATURE must be between 0 and 2."
        )

    if MAX_OUTPUT_TOKENS <= 0:
        raise ConfigurationError(
            "MAX_OUTPUT_TOKENS must be greater than 0."
        )