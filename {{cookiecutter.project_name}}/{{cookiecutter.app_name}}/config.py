"""Default configuration
Use env var to override
"""
DEBUG = True

SQLALCHEMY_DATABASE_URI = "postgresql:////tmp/{{cookiecutter.app_name}}.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True

JWT_SECRET_KEY = "changeme"
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']