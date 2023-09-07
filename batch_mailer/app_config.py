import configparser, os

CONFIG_PATH = "batch_mailer.ini"

EMPTY_FROM_EMAIL_MSG = "From email cannot be empty"
EMPTY_EMAIL_SUBJECT_MSG = "Email subject cannot be empty"
EMPTY_EMAIL_TEMPLATE_MSG = "Email template cannot be empty"


def load_config():
    if not os.path.isfile(os.path.abspath(CONFIG_PATH)):
        generate_config()

    config = configparser.ConfigParser()
    config.read(os.path.abspath(CONFIG_PATH))

    return config


def generate_config():
    config = configparser.ConfigParser()
    config["EMAIL"] = {
        "FromEmail": "",
        "EmailSubject": "",
        "EmailTemplate": "",
        "EmailAttachments": "",
    }

    with open(os.path.abspath(CONFIG_PATH), "w") as config_file:
        config.write(config_file)


def validate_config(config):
    error_messages = []

    if config["EMAIL"]["Email"] == "":
        error_messages.append(EMPTY_FROM_EMAIL_MSG)

    if config["EMAIL"]["Subject"] == "":
        error_messages.append(EMPTY_EMAIL_SUBJECT_MSG)

    if config["EMAIL"]["Template"] == "":
        error_messages.append(EMPTY_EMAIL_TEMPLATE_MSG)

    return error_messages
