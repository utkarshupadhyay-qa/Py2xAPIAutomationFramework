# Integration Scenarios

# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
# 4. Create a BOOKING, Delete It
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404



# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.

# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.



import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class Test_Integration_TC3(object):

    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(),
                                 headers=Util().common_headers_json(),
                                 auth=None,
                                 in_json=False,
                                 payload=payload_create_token()
                                 )


        token = response.json()["token"]
        return token


    @pytest.fixture()
    def get_existing_booking_id(self):
        response=get_request(url=APIConstants.url_create_booking(),
                              auth=None
                              )
        bookings=response.json()
        booking_ids = bookings[0]
        booking_id=booking_ids["bookingid"]
        return booking_id


    @allure.title("Update the booking_id and verify it got updated")
    @allure.description("Update the booking using PUT and verify that booking got updated")
    def test_update_booking_verify_updated(self,create_token,get_existing_booking_id):
        token=create_token
        booking_id=get_existing_booking_id
        response=put_requests(url=APIConstants.url_patch_put_delete(booking_id=booking_id),
                              headers=Util().common_header_put_delete_patch_cookie(token=token),
                              auth=None,
                              in_json=False,
                              payload=payload_create_booking_integration())

        verify_http_status_code(response_data=response,expect_data=200)


        get_response=get_request(url=APIConstants.url_patch_put_delete(booking_id=booking_id),
                                  auth=None)

        data=get_response.json()
        verify_first_name(key=data["firstname"],expected_result="Johnson")
        verify_last_name(key=data["lastname"],expected_result="Brown")

        print("Booking Updated Succesfully")


