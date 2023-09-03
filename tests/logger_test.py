import unittest
import shutil
import os

from batch_mailer import logger
from os import path
from datetime import datetime

TEST_LOG_FOLDER_PATH = path.abspath("tests/logger_test_logs")

logger.LOG_FOLDER_PATH = TEST_LOG_FOLDER_PATH


class LoggerTests(unittest.TestCase):
    def setUpClass():
        if not path.isdir(TEST_LOG_FOLDER_PATH):
            os.mkdir(TEST_LOG_FOLDER_PATH)

    def tearDownClass():
        # clear all test logs
        if path.exists(TEST_LOG_FOLDER_PATH):
            shutil.rmtree(TEST_LOG_FOLDER_PATH)

    # NOTE: For debugging: the 3 tests below are time sensitive tests
    def test_info(self):
        logger.info("This is an info log")
        self.assert_log_type(logger.INFO, "This is an info log")

    def test_warn(self):
        logger.warn("This is an warning log")
        self.assert_log_type(logger.WARN, "This is an warning log")

    def test_error(self):
        logger.error("This is an error log")
        self.assert_log_type(logger.ERROR, "This is an error log")

    def test_write_log(self):
        # Action
        logger.write_log("Test log")
        logger.write_log("There was an error!")

        # Assess
        self.do_logger_assertions("Test log")
        self.do_logger_assertions("There was an error!")

    def assert_log_type(self, type: str, text):
        log_time = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{type.upper()} {log_time}]: {text}\n"

        self.do_logger_assertions(log_message)

    def do_logger_assertions(self, logText):
        if path.exists(TEST_LOG_FOLDER_PATH) == False:
            self.fail(f"Log directory does not exist: '{TEST_LOG_FOLDER_PATH}'")

        if os.listdir(TEST_LOG_FOLDER_PATH).count == 0:
            self.fail("No log files created")

        logFileName = path.join(
            TEST_LOG_FOLDER_PATH, os.listdir(TEST_LOG_FOLDER_PATH)[0]
        )

        with open(logFileName, "r") as logFile:
            for line in logFile.readlines():
                if logText in line:
                    return

            self.fail(f"Unable to find line with content: '{logText}'")
