"""Experiment 14: Demonstrate the various uses of the logging module -- CO-5"""

import logging

# ---------- Basic configuration: log to console AND file ----------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),                       # console
        logging.FileHandler("app.log", mode="w"),      # file
    ],
)

# 1) The five log levels
logging.debug("Debug message  - detailed info for developers")
logging.info("Info message   - normal program events")
logging.warning("Warning message - something unexpected")
logging.error("Error message  - a task failed")
logging.critical("Critical message - serious failure")

# 2) A named logger
logger = logging.getLogger("MyApp")
logger.info("Application started")


# 3) Logging inside a function with exception handling
def divide(a, b):
    try:
        result = a / b
        logger.info("Division successful: %s / %s = %s", a, b, result)
        return result
    except ZeroDivisionError:
        logger.exception("Cannot divide by zero")      # also logs traceback


divide(10, 2)
divide(5, 0)

# 4) Logging with different handler levels
handler = logging.FileHandler("errors.log", mode="w")
handler.setLevel(logging.ERROR)                        # only errors go here
handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
logger.addHandler(handler)
logger.warning("This warning will NOT be saved in errors.log")
logger.error("This error WILL be saved in errors.log")

print("\nLogs saved in 'app.log' and 'errors.log'")
