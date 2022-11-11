"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    contacts_text = ""
    for contact_line in csv.reader(
        contacts.splitlines(),
        quotechar='"',
        delimiter=",",
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    ):
        current_contact_job = contact_line[1]
        if job_description in current_contact_job.lower():
            contact_line.append(contact_line)
        return contact_line
    # create an empty list of the contacts
    # iterate through the file, parsing it line by line
    # refer to the file called input/contacts.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse
    # iterate through each line of the file and extract the current job
    # extract the current job for the contact on this line of the CSV
    # the job description matches and thus we should save it in the list
    # return the list of the contacts who have a job description that matches
