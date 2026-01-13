"""Configuration settings for the agent service."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # API Settings
    api_host: str = "127.0.0.1"
    api_port: int = 8000  # Agent service port (separate from UI)
    api_reload: bool = True

    # Agent Settings
    anthropic_api_key: str = ""
    claude_model: str = "claude-sonnet-4-20250514"

    # Claude Agent SDK Settings
    claude_code_path: str = "claude"  # Path to claude-code executable

    model_config = {"env_file": ".env", "case_sensitive": False}


settings = Settings()
