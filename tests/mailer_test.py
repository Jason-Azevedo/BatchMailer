import unittest

from batch_mailer import mailer
from os import path

TEST_ATTACHMENT_FOLDER = "tests/attachments"


class MailerTest(unittest.TestCase):
    def test_load_recipient_emails(self):
        pass

    def test_get_absolute_attachment_paths(self):
        config = {"EMAIL": {"Attachments": ["test.txt", "test2.txt"]}}

        # Get the expected absolute email paths
        expected_attachment_paths = []

        for attachment in config["EMAIL"]["Attachments"]:
            absolute_path = path.abspath(path.join(TEST_ATTACHMENT_FOLDER, attachment))
            expected_attachment_paths.append(absolute_path)

        mailer.EMAIL_ATTACHMENTS_PATH = TEST_ATTACHMENT_FOLDER
        attachment_paths = mailer.get_absolute_attachment_paths(config)

        self.assertEqual(expected_attachment_paths, attachment_paths)

    def test_load_email_template(self):
        pass

    def test_mark_emails_as_actioned(self):
        pass

    def test_clear_recipient_emails(self):
        pass
