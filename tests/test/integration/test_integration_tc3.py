# Integration Scenarios

# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
# 4. Create a BOOKING, Delete It
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404



# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.

import pytest
import allure
import json
import requests

from src.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *


class Testsinglebookingupdate(object):

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

    @pytest.fixture()
    def get_all_bookings(self):
        response = get_request(url=APIconstants.create_booking_url(),
                               auth=None)

        booking_ids = response.json()
        booking_id = booking_ids[0]
        booking = booking_id['bookingid']

        return booking

    @allure.title("#TC1 update existing booking id")
    @allure.testcase("Verify update booking")
    @allure.description("Verify attributes for existing booking id")
    def test_update_existing_booking(self, get_all_bookings, create_token):
        response = put_request(url=APIconstants.url_patch_put_delete(get_all_bookings),
                               headers=Util().put_patch_delete_headers_cookie(create_token),
                               auth=None,
                               payload=existing_put_payload_integration(),
                               in_json=False)

        print(response.json())

        first_name = response.json()["firstname"]
        last_name = response.json()["lastname"]
        total_amt = response.json()["totalprice"]

        # verification

        verify_http_status_code(response, 200)

        verify_first_name(first_name, 'john')

        verify_last_name(last_name, 'cameron')

        verify_key_not_null(total_amt)

        verify_key_not_equal_zero(total_amt)