import os

AGILE_API_SETTINGS = {}

AGILE_TIMEZONE = os.environ.get('AGILE_TIMEZONE')
if not AGILE_TIMEZONE:
    AGILE_TIMEZONE = 'America/Los_Angeles'
AGILE_API_SETTINGS['AGILE_TIMEZONE'] = AGILE_TIMEZONE

AGILE_DATE_FORMAT = os.environ.get('AGILE_DATE_FORMAT')
if not AGILE_DATE_FORMAT:
    AGILE_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'
AGILE_API_SETTINGS['AGILE_DATE_FORMAT'] = AGILE_DATE_FORMAT

