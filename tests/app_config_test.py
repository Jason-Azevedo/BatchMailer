import unittest
import configparser
import os

from batch_mailer import app_config
from os import path

app_config.CONFIG_PATH = "tests/test_config.ini"

ABS_TEST_CONFIG_PATH = path.abspath(app_config.CONFIG_PATH)


class AppConfigTests(unittest.TestCase):
    def tearDownClass():
        # Delete test config file if it exists
        if path.isfile(app_config.CONFIG_PATH):
            os.remove(ABS_TEST_CONFIG_PATH)

    def test_validate_config(self):
        test_config_data = get_test_validation_config_data()

        for config in test_config_data:
            validation_messages = app_config.validate_config(config["config"])

            self.assertEqual(
                config["expected_errors"],
                validation_messages,
                config["error_message"],
            )

    def test_generate_config(self):
        app_config.generate_config()

        if not path.isfile(app_config.CONFIG_PATH):
            self.fail(f"No config file generated in path: {ABS_TEST_CONFIG_PATH}")

    def test_load_config(self):
        # Generate config for this test
        app_config.generate_config()

        config = app_config.load_config()
        validation_messages = app_config.validate_config(config)

        self.assertEqual(
            [
                app_config.EMPTY_FROM_EMAIL_MSG,
                app_config.EMPTY_EMAIL_SUBJECT_MSG,
                app_config.EMPTY_EMAIL_TEMPLATE_MSG,
            ],
            validation_messages,
            f"Unexpected validations errors occured from loading test config",
        )


# Load different configs to test validation
def get_test_validation_config_data():
    # VALID CONFIG
    valid_config = configparser.ConfigParser()
    valid_config["EMAIL"] = {
        "FromEmail": "testemail@test.com",
        "EmailSubject": "This is a test email",
        "EmailTemplate": "test_email.html",
        "EmailAttachments": "test1.pdf,test2.pdf",
        "EmailListPath": "Some path",
    }

    valid_config_data = {
        "config": valid_config,
        "expected_errors": [],
        "error_message": "Unexpected errors occured for config: Valid_Config",
    }

    # EMPTY CONFIG
    empty_config = configparser.ConfigParser()
    empty_config["EMAIL"] = {
        "FromEmail": "",
        "EmailSubject": "",
        "EmailTemplate": "",
        "EmailAttachments": "",
        "EmailListPath": "",
    }

    empty_config_data = {
        "config": empty_config,
        "expected_errors": [
            app_config.EMPTY_FROM_EMAIL_MSG,
            app_config.EMPTY_EMAIL_SUBJECT_MSG,
            app_config.EMPTY_EMAIL_TEMPLATE_MSG,
        ],
        "error_message": "Unexpected errors occured for config: Empty_Config",
    }

    return [valid_config_data, empty_config_data]
