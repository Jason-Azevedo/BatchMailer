import unittest
import shutil
import os

from batch_mailer import logger
from os import path

TEST_LOG_FOLDER_PATH = path.abspath("tests/logger_test_logs")


class LoggerTests(unittest.TestCase):
    def tearDown(self):
        # clear all test logs
        if path.exists(TEST_LOG_FOLDER_PATH):
            shutil.rmtree(TEST_LOG_FOLDER_PATH)

    def test_info(self):
        self.fail("Not implemented")

    def test_warn(self):
        self.fail("Not implemented")

    def test_error(self):
        self.fail("Not implemented")

    def test_write_log(self):
        # Action
        logger.write_log(TEST_LOG_FOLDER_PATH, "Test log")
        logger.write_log(TEST_LOG_FOLDER_PATH, "Test log 2")

        # Assess
        # Does the file exist in the correct location?
        if path.exists == False:
            self.fail(f"Log directory does not exist: '{TEST_LOG_FOLDER_PATH}'")

        if os.listdir(TEST_LOG_FOLDER_PATH).count == 0:
            self.fail("No log files created")
            

        # Does the content exist within the file?
