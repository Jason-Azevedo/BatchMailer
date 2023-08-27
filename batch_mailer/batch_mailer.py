import __main__
import logger
import config
import mailer
import os

# Prevent execution of this file if it is not the main script
if __name__ != "__main__":
    exit()

# Log the start of the program
# Log if we found a config file or not
