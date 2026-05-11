# Integration Scenarios

# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
# 4. Create a BOOKING, Delete It
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404


# Test for the Single Req
# 1. Response
# 2. Status Code
# 3. Headers

# Assertions will always pass  (even for negative) -> e.g - test_create_booking.py -> negative test case will also pass


# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.


import pytest
import allure
import json
import requests

from src.constants.api_constants import APIConstants
from src.utils.utils import Util
from src.helpers.payload_manager import *
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *


# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class Test_Integration_TC1(object):

    @pytest.fixture()
    def create_token(self):
        response = post_request(
            url=APIConstants.url_create_token(),
            payload=payload_create_token(),
            auth=None,
            headers = Utils().common_headers_json(),
            in_json=False
        )

        token = response.json()["token"]
        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null_token(token)
        return token


    @pytest.fixture()
    def create_booking(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                 headers=Util().common_headers_json(),
                                 payload=payload_create_booking(),
                                 auth=None,
                                 in_json=False,
                                 )

        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id

    @allure.title("Verify First Name is Updated")
    @allure.description(
        "Verify that Patch Request is completed and First name is updated")

    def test_patch_request_firstname_updated(self,create_booking,create_token):
        booking_id=create_booking
        token=create_token

        response = patch_requests(url=APIConstants.url_patch_put_delete(booking_id=booking_id),
                                  headers=Util().common_header_put_delete_patch_cookie(token=token),
                                  auth=None,
                                  in_json=False,
                                  payload=payload_create_booking_integration(),
                                  )

        first_name = response.json()["firstname"]
        print(first_name)

        verify_first_name(first_name,"Johnson")
        verify_http_status_code(response_data=response,expect_data=200)
        verify_response_key_should_not_be_none(first_name)

