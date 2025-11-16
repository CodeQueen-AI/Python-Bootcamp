import logging

# Configure logging
logging.basicConfig(
    filename="app.log",       # Log file name
    level=logging.DEBUG,      # Log everything from DEBUG to CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Sample log messages
logging.debug("This is a debug message – useful for developers.")
logging.info("Program is running smoothly.")
logging.warning("This is a warning – something might be wrong.")
logging.error("An error occurred!")
logging.critical("Critical issue! Immediate attention needed.")
