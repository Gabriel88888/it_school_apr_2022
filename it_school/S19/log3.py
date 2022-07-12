import logging
from tabnanny import verbose

LOGGER_NAME = "main_logger"


# creem un logger nou
logger = logging.getLogger("LOGGER_NAME")

# format
#https://docs.python.org/3/library/logging.html#logrecord-attributes
message_only = logging.Formatter("%(message)")


#Handler
# https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers

cli_handler = logging.StreamHandler() # pentru CI - consola
#ii spunem ce format sa foloseasca aceste handler
cli_handler.formatter = message_only


#Logger
# creem un logger nou, care are nevoie de un nume , retinu in LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)
#set nivel de gravitate
logger.setLevel(logging.DEBUG)