import gspread
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import os
# def init_gsheets():
#     scope = [
#         "https://spreadsheets.google.com/feeds",
#         "https://www.googleapis.com/auth/drive"
#     ]
#     secrets_path = os.path.join(os.getcwd(), ".streamlit", "secrets.toml")
#     if os.path.exists(secrets_path):
#         if "GOOGLE_CREDS" in st.secrets and st.secrets["GOOGLE_CREDS"]:
#             creds_dict = json.loads(st.secrets["GOOGLE_CREDS"])
#             creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
#         else:
#             raise RuntimeError("GOOGLE_CREDS not found in Streamlit secrets.")
#     else:  # Local development
#         creds = ServiceAccountCredentials.from_json_keyfile_name("config/creds.json", scope)
#     client = gspread.authorize(creds)
#     return client
def init_gsheets():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    if "GOOGLE_CREDS" in st.secrets:
        creds_dict = dict(st.secrets["GOOGLE_CREDS"])
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    else:
        creds = ServiceAccountCredentials.from_json_keyfile_name("config/creds.json", scope)
    client = gspread.authorize(creds)
    return client

def log_lead(data):
    client = init_gsheets()
    sheet = client.open("Lead_Records").sheet1
    sheet.append_row(data)
