# Integration Scenarios

# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
# 4. Create a BOOKING, Delete It
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404



# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

import pytest
import allure
import json
import requests

from source.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *


class Testbookingget(object):

    @pytest.fixture()
    def create_booking(self):
        response = post_request(url=APIconstants.create_booking_url(),
                                headers=Util().common_headers_json(),
                                auth=None,
                                payload=create_booking_payload_integration(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        return booking_id

    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIconstants.create_token_url(),
                                headers=Util().common_headers_json(),
                                payload=create_token_payload(),
                                auth=None,
                                in_json=False
                                )
        token = response.json()["token"]
        return token

    @allure.title("TC#1 Delete booking")
    @allure.testcase("Delete booking")
    @allure.description("Verify booking got deleted successfully")
    def test_delete_booking(self, create_booking, create_token):
        response = delete_request(url=APIconstants.url_patch_put_delete(create_booking),
                                  headers=Util().put_patch_delete_headers_cookie(create_token),
                                  auth=None,
                                  payload=None,
                                  in_json=False)

        # verify status code

        verify_http_status_code(response, 400)

    @allure.title("TC#2 Get booking")
    @allure.testcase("Get booking details")
    @allure.description("Verify no details are present for the selected booking id")
    def test_get_deleted_booking(self, create_booking):
        response = get_request(url=APIconstants.get_url(create_booking),
                               auth=None)
        #print(response.text)

        verify_http_status_code(response, 404)
