import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%D %H:%M:%S")


def sheet_data(sport, write=None, db_new=None):
    scope = ["https://spreadsheets.google.com/feeds"]
    config_path = os.path.join(os.path.dirname(__file__), "./google-credentials.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(config_path, scope)
    client = gspread.authorize(creds)

    if not write:
        sheet_prev = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1XLeWiVBUTC1mD5ZVNRM6LHV5MBh-UAMUSsWWrSm0YKs/edit#gid=0"
        ).worksheet(sport)
        # get_all_values gives a list of rows.s
        rows_prev = sheet_prev.get_all_values()
        prev_urls = [url[0] for url in rows_prev]
        return prev_urls
    else:
        sheet_latest = client.open_by_key(
            "1XLeWiVBUTC1mD5ZVNRM6LHV5MBh-UAMUSsWWrSm0YKs"
        ).worksheet(sport)
        data_values = pd.DataFrame(db_new).values.tolist()
        sheet_latest.append_rows(data_values)
        print(
            f"[{__name__}]-[{current_time}] - Ran successfuly for URLS:- \n{db_new['Links']}"
        )


