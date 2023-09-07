import yagmail
import csv
import logger

from os import path
from datetime import datetime


EMAIL_TEMPLATE_PATH = "templates"
EMAIL_ATTACHMENTS_PATH = "attachments"

EMAIL_RECIPIENTS_PATH = "data/emails.csv"
ACTIONED_EMAILS_PATH = "data/actioned_emails.csv"


def send_mails(config):
    try:
        emailConfig = config["EMAIL"]
        generalConfig = config["GENERAL"]

        yag = yagmail.SMTP(
            user=emailConfig["Email"], password=emailConfig["EmailPassword"]
        )

        emails = load_recipient_emails()
        attachments = get_absolute_attachment_paths(config)
        template = get_email_template(config)

        # send emails
        yag.send(
            to=emails,
            subject=emailConfig["Subject"],
            contents=template,
            attachments=attachments,
        )

        # Log actioned emails
        mark_emails_as_actioned(config, emails)

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
    attachments = config["EMAIL"]["Attachments"].split(",")
    absolute_attachments = []

    for attachment in attachments:
        absolute_path_to_attachment = path.join(
            path.abspath(EMAIL_ATTACHMENTS_PATH), attachment.strip()
        )

        absolute_attachments.append(absolute_path_to_attachment)

    return absolute_attachments


def get_email_template(config):
    template_name = config["EMAIL"]["Template"]
    template_path = path.join(path.abspath(EMAIL_TEMPLATE_PATH), template_name)

    if not path.isfile(template_path):
        raise FileExistsError(f"The following path is not a file: {template_path}")

    with open(template_path, "r") as template_file:
        return template_file.read()


def mark_emails_as_actioned(config, emails):
    actioned_emails_path = path.abspath(ACTIONED_EMAILS_PATH)
    file_exists = path.isfile(actioned_emails_path)

    with open(actioned_emails_path, "a") as actioned_file:
        csv_rows = []

        config_subject = config["EMAIL"]["Subject"]
        config_template = config["EMAIL"]["Template"]
        config_attachments = config["EMAIL"]["Attachments"]

        if not file_exists:
            # Create header row with the following columns: actioned_date, email, subject, template_name, attachments
            csv_rows.append(
                ["actioned_date", "email", "subject", "template_name", "attachments"]
            )

        for email in emails:
            # Create the date time format
            actioned_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

            csv_rows.append(
                [
                    actioned_date,
                    email,
                    config_subject,
                    config_template,
                    config_attachments,
                ]
            )

        csvwriter = csv.writer(actioned_file)
        csvwriter.writerows(csv_rows)


def clear_recipient_emails():
    recipient_emails_path = path.abspath(EMAIL_RECIPIENTS_PATH)

    if not path.isfile(recipient_emails_path):
        raise FileExistsError(
            f"The following file does not exist: {recipient_emails_path}"
        )

    with open(recipient_emails_path, "w") as recipients_file:
        recipients_file.writelines("EMAILS")
