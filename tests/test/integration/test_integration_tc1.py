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


class TestBookingIntg(object):

    @pytest.fixture()
    def create_booking(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                headers=Util().common_headers_json(),
                                auth=None,
                                payload=payload_create_booking(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        # Bookingid verification

        verfiy_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)


        return booking_id

    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(),
                                headers=Util().common_headers_json(),
                                payload=payload_create_token(),
                                auth=None,
                                in_json=False
                                )
        token = response.json()["token"]
        return token

    # Patch Request - Verify that firstName is updated.

    @allure.title("TC#1 Integration test: partial update booking")
    @allure.testcase("Verify that first name is updated")
    @allure.description("verifying first name updation")
    def test_patch_request(self, create_booking, create_token):
        response = patch_requests(url=APIConstants.url_patch_put_delete(create_booking),
                                 headers=Util().common_header_put_delete_patch_cookie(create_token),
                                 auth=None,
                                 payload=payload_create_booking_dynamic(),
                                 in_json=False)

        first_name = response.json()["firstname"]
        print(first_name)

        verify_first_name(first_name, "shambhavi")
        verify_http_status_code(response, 200)

        verify_key_not_null(first_name)