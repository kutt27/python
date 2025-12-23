"""
Pydantic: Settings Management
==============================

Topic: BaseSettings (pydantic-settings)

Real-World Applications:
- Loading environment variables (.env)
- Application configuration (DB_HOST, API_KEY)
"""

# Note: Requires `pip install pydantic-settings`
# We simulate it with standard Pydantic for the demo if package missing, 
# but describe the pattern.

from pydantic import Field
import os

try:
    from pydantic_settings import BaseSettings
except ImportError:
    print("Using Mock BaseSettings (pydantic-settings not installed)")
    from pydantic import BaseModel as BaseSettings

class AppSettings(BaseSettings):
    """
    Application Settings.
    Automatically reads from Environment Variables!
    """
    app_name: str = "MyApp"
    api_key: str = Field(..., alias="MY_API_KEY") # Requires MY_API_KEY env var
    debug: bool = False
    
    # In real usage, this loads .env file
    # model_config = SettingsConfigDict(env_file='.env')


def main():
    """Demonstrates settings loading."""
    print("="*70)
    print("SETTINGS MANAGEMENT".center(70))
    print("="*70)
    
    # Simulate Environment Variables
    os.environ["MY_API_KEY"] = "secret-123"
    os.environ["DEBUG"] = "true" # "true" -> True coercion
    
    try:
        settings = AppSettings()
        print(f"App: {settings.app_name}")
        print(f"API Key: {settings.api_key}")
        print(f"Debug Mode: {settings.debug}")
    except Exception as e:
        print(f"Settings Error: {e}")
        
    print("\n" + "="*70)
    print("Key Points:")
    print("• `BaseSettings` reads fields from system environment variables")
    print("• Case-insensitive by default (debug matches DEBUG)")
    print("• Supports .env files (with python-dotenv)")
    print("• The Industry Standard for Python config management")
    print("="*70)


if __name__ == "__main__":
    main()
