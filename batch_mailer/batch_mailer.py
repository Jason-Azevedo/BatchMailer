import __main__
import logger
import config
import mailer
import os

# Prevent execution of this file if it is not the main script
if __name__ != "__main__":
    exit()

logger.info("STARTING RUN")

# Load the config file


logger.info("RUN COMPLETE\n\n")
