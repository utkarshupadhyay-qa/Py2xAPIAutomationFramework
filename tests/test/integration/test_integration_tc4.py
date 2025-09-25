# Integration Scenarios

# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
# 4. Create a BOOKING, Delete It
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404


# Invalid Creation - enter a wrong payload or Wrong JSON.

import pytest
import allure
import json
import requests

from source.constant.api_constants import APIconstants
from source.utils.utils import Util
from source.helpers.payload_manager import *
from source.helpers.api_request_wrapper import *
from source.helpers.common_verification import *

@allure.title("TC#1 Invalid booking creation")
@allure.testcase("Verify status code")
@allure.description("verify if booking id created using invalid payload")
def test_invalid_create_booking():
    response = post_request(url=APIconstants.create_booking_url(),
                            headers=Util().common_headers_json(),
                            auth=None,
                            payload=invalid_payload_integration(),
                            in_json=False)

    #Verification
    verify_http_status_code(response, 500)