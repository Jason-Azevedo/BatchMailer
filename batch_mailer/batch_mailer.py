import __main__
import logger
import app_config
import os


def validate_config(config):
    validation_messages = app_config.validate_config(config)

    if validation_messages.count == 0:
        return True

    for message in validation_messages:
        logger.error(f"Config error: {message}")

    return False


# Prevent execution of this file if it is not the main script
if __name__ != "__main__":
    exit()


logger.info("STARTING RUN")

# Load the config file
config = app_config.load_config()
config_valid = validate_config(config)

if config_valid:
    # Send mails
    pass


logger.info("RUN COMPLETE\n\n")
