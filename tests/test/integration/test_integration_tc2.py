# Integration Scenarios

# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
# 4. Create a BOOKING, Delete It
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404



# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

class Test_Integration_TC2(object):

    @pytest.fixture()
    def create_token(self):
        response=post_request(url=APIConstants.url_create_token(),
                               headers=Util().common_headers_json(),
                               auth=None,
                               in_json=False,
                               payload=payload_create_token())


        token=response.json()["token"]
        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null_token(token)
        return token



    @pytest.fixture()
    def create_booking(self):
        response=post_request(url=APIConstants.url_create_booking(),
                               headers=Util().common_headers_json(),
                               auth=None,
                               in_json=False,
                               payload=payload_create_booking())

        booking_id= response.json()["bookingid"]
        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id



    @allure.title("Delete the Booking")
    @allure.description("Verify that booking is deleted successfully")
    def test_delete_bookingid_verify_get_integration_tc2(self,create_booking,create_token):

        booking_id=create_booking
        token=create_token
        delete_response=delete_requests(url=APIConstants.url_patch_put_delete(booking_id=booking_id),
                                 headers=Util().common_header_put_delete_patch_cookie(token=token),
                                 auth=None,
                                 in_json=False,
                                 )

        verify_response_delete(response=delete_response.text)
        verify_http_status_code(response_data=delete_response,expect_data=201)

        get_response=get_request(url=APIConstants.url_patch_put_delete(booking_id=booking_id),
                                  auth=None)

        verify_http_status_code(response_data=get_response,expect_data=404)

