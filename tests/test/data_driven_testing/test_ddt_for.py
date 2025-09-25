# Read the CSV or EXCEL file
# Create a Function of create_token which can take values from the Excel File
# Verify the Expected Result.

# Read the Excel - openpyxl
import openpyxl
import requests

from src.constants.api_constants import APIConstants
from src.utils.utils import Util
from src.helpers.api_request_wrapper import *



# read the excel file and put this into dictionary
def read_credentials_from_excel(file_path):    # This will give you dataset -> multiple usernames and passwords from excel
    credentials = [] # Created an empty list  -> This list will be list of rows
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active   # looking into sheet which is active -> Sheet1
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username,password = row  # We have created a username, password dictionary
        credentials.append(({     # we are adding username,password dictionary into credential list ->list containing multiple dictionary
            "username" : username,
            "password" : password
        }))
    return credentials


def create_auth_request(username,password):   # For each set of username and password -> this function will run
    payload = {
        "username": username,
        "password": password
    }
    response = post_request(
        url=APIConstants.url_create_token(),
        headers=Util().common_headers_json(),
        auth=None,
        payload=payload,
        in_json=False
    )
    return response


def test_create_auth_with_excel():   # This will run the create_auth_request function
    file_path = "C:/Users/DELL/PycharmProjects/Py2xAPIAutomationFramework/tests/test/data_driven_testing/testdata_ddt_123.xlsx"
    credentials = read_credentials_from_excel(file_path=file_path)
    print(credentials)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        response = create_auth_request(username=username,password=password)
        print(response.status_code)

