from os import path
from datetime import datetime, date

INFO = "INFO"
WARN = "WARN"
ERROR = "ERROR"
LOG_FOLDER_PATH = "/logs"


def info(text):
    log(INFO, text)


def warn(text):
    log(WARN, text)


def error(text):
    log(ERROR, text)


def log(type: str, text):
    current_time = datetime.now().strftime("%H:%M:%S")
    log_message = f"[{type} {current_time}]: {text}\n"

    write_log(log_message)


def write_log(text):
    # Create a new log file with the date as the file name in format: log_2023_08_21.txt
    try:
        todaysDate = date.today().strftime("%Y_%m_%d")
        logFileName = f"log_{todaysDate}.txt"
        absoluteLogFilePath = path.join(path.abspath(LOG_FOLDER_PATH), logFileName)

        with open(absoluteLogFilePath, "a") as logFile:
            logFile.write(text + "\n")

    except Exception as ex:
        print("logger.py  write_log(): Something went wrong...")
        print(ex)
