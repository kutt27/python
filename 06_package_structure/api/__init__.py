"""
API Client Package - Package Initialization
============================================

This __init__.py file makes the 'api' directory a Python package and
controls what gets imported when someone does 'from api import *'.

Real-World Application: Package organization, public API definition
"""

# Import main classes to make them available at package level
from .auth import APIAuthenticator, create_auth_headers, AuthenticationError
from .client import HTTPClient, HTTPError

# Define public API - what gets imported with 'from api import *'
__all__ = [
    'APIAuthenticator',
    'create_auth_headers',
    'AuthenticationError',
    'HTTPClient',
    'HTTPError',
]

# Package metadata
__version__ = '1.0.0'
__author__ = 'API Team'

# Optional: Package-level initialization
print("API client package loaded")
