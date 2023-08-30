# gunicorn_config.py

workers = 4         # Number of worker processes
bind = "0.0.0.0:8000"  # Binding address and port
timeout = 1       # Maximum request/response timeout