import __main__
import config
import mailer
import os

# Prevent execution of this file if it is not the main script
if __name__ != "__main__":
    exit()

try: 
    CONFIG_FILE_NAME = "batch_mailer.cfg"
    CONFIG_FILE_PATH = os.path.dirname(__main__.__file__)

    if (not os.path.isfile(CONFIG_FILE_NAME)):
        print(f"No config file found in '{CONFIG_FILE_PATH}'")
        print("Generating new config file...")

        config.generate_config()

    config = config.load_config()
    mailer.send_mails(config)

    print("Done!")

except:
    print("An unknown error occured!")



