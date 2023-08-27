from os import path
from datetime import datetime, date


def info():
    return


def warn():
    return


def error():
    return


def write_log(text, filePath="/logs"):
    # Create a new log file with the date as the file name in format: log_2023_08_21.txt
    try:
        todaysDate = date.today().strftime("%Y_%m_%d")
        logFileName = f"log_{todaysDate}.txt"
        absoluteLogFilePath = path.join(path.abspath(filePath), logFileName)

        with open(absoluteLogFilePath, "w") as logFile:
            logFile.write(text)

    except Exception as ex:
        print("logger.py  write_log(): Something went wrong...")
        print(ex)
