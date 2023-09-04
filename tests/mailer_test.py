import unittest

from batch_mailer import mailer
from os import path

TEST_TEMPLATE_FOLDER = path.abspath("tests/templates")
TEST_ATTACHMENT_FOLDER = path.abspath("tests/attachments")
TEST_ACTIONED_EMAILS_PATH = path.abspath("tests/data/actioned_emails.csv")


TEST_APP_CONFIG = {
    "GENERAL": {"ClearEmailsAfterRun": "Y"},
    "EMAIL": {
        "Template": "test_template.html",
        "Attachments": ["test.txt", "test2.txt"],
    },
}


class MailerTest(unittest.TestCase):
    def tearDownClass(self):
        # Clear the actioned_emails file
        pass

    def test_load_recipient_emails(self):
        pass

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

    def test_clear_recipient_emails(self):
        pass
