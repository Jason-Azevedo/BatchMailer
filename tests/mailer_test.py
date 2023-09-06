import unittest
import csv

from batch_mailer import mailer
from os import path

TEST_TEMPLATE_FOLDER = path.abspath("tests/templates")
TEST_ATTACHMENT_FOLDER = path.abspath("tests/attachments")
TEST_ACTIONED_EMAILS_PATH = path.abspath("tests/data/actioned_emails.csv")
TEST_RECIPIENT_EMAILS_PATH = path.abspath("tests/data/recipient_emails.csv")


TEST_APP_CONFIG = {
    "GENERAL": {"ClearEmailsAfterRun": "Y"},
    "EMAIL": {
        "Subject": "This is a test email",
        "Template": "test_template.html",
        "Attachments": ["test.txt", "test2.txt"],
    },
}

mailer.ACTIONED_EMAILS_PATH = TEST_ACTIONED_EMAILS_PATH
mailer.EMAIL_RECIPIENTS_PATH = TEST_RECIPIENT_EMAILS_PATH
mailer.EMAIL_TEMPLATE_PATH = TEST_TEMPLATE_FOLDER


class MailerTest(unittest.TestCase):
    def tearDownClass(self):
        # TODO: Delete this file, as the method generates it.
        open(TEST_ACTIONED_EMAILS_PATH, "w").close()

    def test_load_recipient_emails(self):
        # load data from test recipient file
        test_recipients = []
        with open(TEST_RECIPIENT_EMAILS_PATH, "r") as recipients_file:
            csvreader = csv.reader(recipients_file)
            next(csvreader)  # skip the header

            for emailrow in csvreader:
                test_recipients.append(emailrow[0])

        recipients = mailer.load_recipient_emails()

        self.assertEqual(test_recipients, recipients)

    def test_get_absolute_attachment_paths(self):
        # Get the expected absolute email paths
        expected_attachment_paths = []

        for attachment in TEST_APP_CONFIG["EMAIL"]["Attachments"]:
            absolute_path = path.join(TEST_ATTACHMENT_FOLDER, attachment)
            expected_attachment_paths.append(absolute_path)

        mailer.EMAIL_ATTACHMENTS_PATH = TEST_ATTACHMENT_FOLDER
        attachment_paths = mailer.get_absolute_attachment_paths(TEST_APP_CONFIG)

        self.assertEqual(expected_attachment_paths, attachment_paths)

    def test_load_email_template(self):
        # Load the test template
        template_text = ""
        with open(
            path.join(TEST_TEMPLATE_FOLDER, "test_template.html"), "r"
        ) as template_file:
            template_text = template_file.read()

        template = mailer.get_email_template(TEST_APP_CONFIG)

        self.assertEqual(template_text, template)

    def test_mark_emails_as_actioned(self):
        actioned_emails = ["test@mail.com", "test2@outlook.com", "test3@something.io"]

        mailer.mark_emails_as_actioned(TEST_APP_CONFIG, actioned_emails)

        # load the csv and check if the 3 entries are correct
        with open(TEST_ACTIONED_EMAILS_PATH) as csv_file:
            csvreader = csv.reader(csv_file)

            # read the lines and compare
            not_found_emails = []
            for email in actioned_emails:
                email_found = False

                for row in csvreader:
                    if row[1] == email:
                        email_found = True
                        break

                if not email_found:
                    not_found_emails.append(email)

            self.assertEqual(
                [],
                not_found_emails,
                "These emails were not found in actioned_emails.csv",
            )

    def test_clear_recipient_emails(self):
        # Load the original contents
        original_file_contents = []
        with open(TEST_RECIPIENT_EMAILS_PATH, "r") as recipients_file:
            original_file_contents = recipients_file.readlines()

        mailer.clear_recipient_emails()

        # Assert if the file is empty
        with open(TEST_RECIPIENT_EMAILS_PATH, "r") as recipients_file:
            file_contents = recipients_file.readlines()

            self.assertEqual(["EMAILS"], file_contents)

        # Restore the file, because it is used in git
        with open(TEST_RECIPIENT_EMAILS_PATH, "w") as recipients_file:
            recipients_file.writelines(original_file_contents)
