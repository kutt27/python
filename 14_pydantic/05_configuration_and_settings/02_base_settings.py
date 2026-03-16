"""
Topic: BaseSettings.

`BaseSettings` (from `pydantic-settings`) reads configuration values 
from environment variables. It is the gold standard for app config.
"""

from pydantic import Field
import os

try:
    from pydantic_settings import BaseSettings
except ImportError:
    # Fallback for systems without pydantic-settings
    print("WARNING: pydantic-settings not installed.")
    from pydantic import BaseModel as BaseSettings

class AppSettings(BaseSettings):
    """Expects actual environment variables with matching names."""
    app_name: str = "MyApp"
    # The ALIAS indicates the EXPECTED environment variable name
    api_key: str = Field(..., alias="MY_API_KEY") 
    debug: bool = False

if __name__ == "__main__":
    # Simulate loading environment variables before initialization
    os.environ["MY_API_KEY"] = "sk_test_123"
    os.environ["DEBUG"] = "true" # this gets coerced to a boolean True

    try:
        config = AppSettings()
        print(f"App Name: {config.app_name}")
        print(f"API Key: {config.api_key}")
        print(f"Is Debug: {config.debug}")
    except Exception as e:
        print(f"Initialization Error: {e}")
