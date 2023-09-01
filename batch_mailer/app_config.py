import configparser, os

CONFIG_PATH = "test_config.ini"

EMPTY_FROM_EMAIL_MSG = "From email cannot be empty"
EMPTY_EMAIL_SUBJECT_MSG = "Email subject cannot be empty"
EMPTY_EMAIL_TEMPLATE_MSG = "Email template cannot be empty"


def load_config():
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
        "EmailListPath": "",
    }

    with open(os.path.abspath(CONFIG_PATH), "w") as config_file:
        config.write(config_file)


def validate_config(config):
    error_messages = []

    if config["EMAIL"]["FromEmail"] == "":
        error_messages.append(EMPTY_FROM_EMAIL_MSG)

    if config["EMAIL"]["EmailSubject"] == "":
        error_messages.append(EMPTY_EMAIL_SUBJECT_MSG)

    if config["EMAIL"]["EmailTemplate"] == "":
        error_messages.append(EMPTY_EMAIL_TEMPLATE_MSG)

    return error_messages
