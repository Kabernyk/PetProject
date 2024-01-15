"""
Log levels:
DEBUG
INFO
WARNING
ERROR
FATAL
"""

import logging

LOG_FILE_NAME = "test"
# Create a custom logger
log = logging.getLogger(__name__)
# Create handlers
_c_handler = logging.StreamHandler()
_f_handler = logging.FileHandler(f"{LOG_FILE_NAME}.log")
_c_handler.setLevel(logging.DEBUG)
_f_handler.setLevel(logging.INFO)
# Create formatters and add it to handlers
_c_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
_f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
_c_handler.setFormatter(_c_format)
_f_handler.setFormatter(_f_format)
# Add handlers to the logger
log.addHandler(_c_handler)
log.addHandler(_f_handler)
