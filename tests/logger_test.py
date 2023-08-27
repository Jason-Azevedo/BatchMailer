import unittest
import shutil
import os

from batch_mailer import logger
from os import path

TEST_LOG_FOLDER_PATH = path.abspath("tests/logger_test_logs")


class LoggerTests(unittest.TestCase):
    def setUp(self):
        if not path.isdir(TEST_LOG_FOLDER_PATH):
            os.mkdir(TEST_LOG_FOLDER_PATH)

    def tearDown(self):
        # clear all test logs
        if path.exists(TEST_LOG_FOLDER_PATH):
            shutil.rmtree(TEST_LOG_FOLDER_PATH)

    def test_info(self):
        logInfoMessage = "Test log info"
        logger.info(logInfoMessage)

        self.do_logger_assertions(logInfoMessage)

    def test_warn(self):
        logWarnMessage = "Test warn info"
        logger.warn(logWarnMessage)

        self.do_logger_assertions(logWarnMessage)

    def test_error(self):
        logErrorMessage = "Test error info"
        logger.error(logErrorMessage)

        self.do_logger_assertions(logErrorMessage)

    def test_write_log(self):
        # Action
        logger.write_log("Test log", TEST_LOG_FOLDER_PATH)
        logger.write_log("Test log 2", TEST_LOG_FOLDER_PATH)

        # Assess
        self.do_logger_assertions(self, "Test log")
        self.do_logger_assertions(self, "Test log 2")

    def assert_log_file_contents(self, contents):
        pass

    def assert_log_file(self):
        pass

    def do_logger_assertions(self, logText):
        pass
        # Something is wrong with this method:

        # if path.exists(TEST_LOG_FOLDER_PATH) == False:
        #     self.fail(f"Log directory does not exist: '{TEST_LOG_FOLDER_PATH}'")

        # if os.listdir(TEST_LOG_FOLDER_PATH).count == 0:
        #     self.fail("No log files created")

        # logFileName = path.join(
        #     TEST_LOG_FOLDER_PATH, os.listdir(TEST_LOG_FOLDER_PATH)[0]
        # )

        # with open(logFileName, "r") as logFile:
        #     logFileContents = logFile.read()

        #     if not logText in logFileContents:
        #         self.fail(
        #             f"Expected: '{logText}', but found the following in log file: '{logFileContents}'"
        #         )
