import logger
import app_config
import mailer


def validate_config(config):
    validation_messages = app_config.validate_config(config)

    if len(validation_messages) == 0:
        return True

    for message in validation_messages:
        logger.error(f"Config error: {message}")

    return False


logger.info("STARTING RUN")

# Load the config file
config = app_config.load_config()
config_valid = validate_config(config)

if config_valid:
    mailer.send_mails(config)


logger.info("RUN COMPLETE\n\n")
