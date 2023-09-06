import yagmail
import csv

from batch_mailer import logger
from os import path


EMAIL_TEMPLATE_PATH = "email_templates"
EMAIL_ATTACHMENTS_PATH = "email_attachments"

EMAIL_RECIPIENTS_PATH = "data/emails.csv"
ACTIONED_EMAILS_PATH = "data/actioned_emails.csv"


def send_mails(config):
    try:
        emailConfig = config["EMAIL"]
        generalConfig = config["GENERAL"]

        yag = yagmail.SMTP(
            user=emailConfig["UserEmail"], password=emailConfig["UserPassword"]
        )

        emails = load_recipient_emails()
        attachments = get_absolute_attachment_paths()
        template = get_email_template()

        # send emails
        yag.send(
            to=emails,
            subject=emailConfig["EmailSubject"],
            attachments=attachments,
            content=template,
        )

        # Log actioned emails
        mark_emails_as_actioned()

        if generalConfig["ClearEmailsAfterRun"] == "Y":
            clear_recipient_emails()

    except Exception as err:
        logger.error(
            "An error occured in send_mails mailer.py. See below for more info"
        )
        logger.error(err)


def load_recipient_emails():
    recipient_emails = []

    with open(EMAIL_RECIPIENTS_PATH, "r") as recipients_file:
        csvreader = csv.reader(recipients_file)

        # skip the header row
        next(csvreader)

        for email_row in csvreader:
            recipient_emails.append(email_row[0])

        return recipient_emails


def get_absolute_attachment_paths(config):
    attachments = config["EMAIL"]["Attachments"]
    absolute_attachments = []

    for attachment in attachments:
        absolute_path_to_attachment = path.join(
            path.abspath(EMAIL_ATTACHMENTS_PATH), attachment
        )

        absolute_attachments.append(absolute_path_to_attachment)

    return absolute_attachments


def get_email_template(config):
    pass


def mark_emails_as_actioned(config, emails):
    # TODO: With the following columns: actioned_date, email, subject, template_name, attachments
    pass


def clear_recipient_emails():
    pass
