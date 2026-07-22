class ConfigurationError(Exception):
    """Raised when application configuration is invalid."""
    pass


class AIServiceError(Exception):
    """Raised when the AI service fails."""
    pass