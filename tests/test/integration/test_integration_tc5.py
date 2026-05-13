# Integration Scenarios

# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
# 4. Create a BOOKING, Delete It
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404

# 5. Invalid Creation - enter a wrong payload or Wrong JSON.

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class Test_Integration_TC5(object):


    @allure.title("Invalid Booking creation")
    @allure.description("Create a booking with invalid payload")
    def test_invalid_booking_creations(self):
        post_response=post_request(url=APIConstants.url_create_booking(),
                                    headers=Util().common_headers_json(),
                                    auth=None,
                                    in_json=False,
                                    payload=payload_invalid())


        verify_http_status_code(response_data=post_response,expect_data=500)

