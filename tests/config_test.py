import unittest
import configparser
import os

from batch_mailer import app_config
from os import path

app_config.CONFIG_PATH = "tests/test_config.ini"

ABS_TEST_CONFIG_PATH = path.abspath(app_config.CONFIG_PATH)


class AppConfigTests(unittest.TestCase):
    def setUpClass():
        # Delete test config file if it exists
        if path.isfile(app_config.CONFIG_PATH):
            os.remove(ABS_TEST_CONFIG_PATH)

    def test_validate_config(self):
        test_configs = get_test_configs()

        for config in test_configs:
            validation_messages = app_config.validate_config(config)

            self.assertEqual(
                [],
                validation_messages,
                f"validation errors occured for test config: {config['test_config_name']}",
            )

    def test_generate_config(self):
        app_config.generate_config()

        if not path.isfile(app_config.CONFIG_PATH):
            self.fail(f"No config file generated in path: {ABS_TEST_CONFIG_PATH}")

        # Check if we get the expected error messages from the generated config file
        generated_config = configparser.ConfigParser().read(ABS_TEST_CONFIG_PATH)
        validation_messages = app_config.validate_config(generated_config)

        self.assertEqual(
            [],
            validation_messages,
            "Unexpected error messages occured from generated file validation",
        )

    # TODO: Implement test method
    def test_load_config(self):
        pass


# Load different configs to test validation
# TODO: Implement these test configs
def get_test_configs():
    pass
