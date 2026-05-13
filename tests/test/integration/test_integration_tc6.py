# Integration Scenarios


# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.
# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
# 4. Create a BOOKING, Delete It
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404

# 6. Trying to Update on a Delete Id -> 404


import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util



class Test_Integration_TC6(object):

    @pytest.fixture()
    def create_token(self):
        response=post_request(url=APIConstants.url_create_token(),
                              headers=Util().common_headers_json(),
                               auth=None,
                               in_json=False,
                               payload=payload_create_token())


        token= response.json()["token"]
        return token



    @pytest.fixture()
    def create_booking(self):
        response=post_request(url=APIConstants.url_create_booking(),
                               headers=Util().common_headers_json(),
                               auth=None,
                               in_json=False,
                               payload=payload_create_booking())

        booking_id=response.json()["bookingid"]
        return booking_id




    @allure.title("Update booking of deleted booking")
    @allure.description("Verify that when we try to update the booking of any deleted booking it gives 404 error")
    def test_update_deleted_booking(self,create_booking,create_token):

        booking_id = create_booking
        token = create_token

        delete_response=delete_requests(url=APIConstants.url_patch_put_delete(booking_id=booking_id),
                                        auth=None,
                                        headers=Util().common_header_put_delete_patch_cookie(token=token),
                                        in_json=False)

        verify_response_delete(response=delete_response.text)

        update_response = put_requests(url=APIConstants.url_patch_put_delete(booking_id=booking_id),
                                       headers=Util().common_header_put_delete_patch_cookie(token=token),
                                       payload=payload_create_booking_integration(),
                                       in_json=False,
                                       auth=None)

        print(update_response.status_code)
        print(update_response.text)

        verify_http_status_code(response_data=update_response,expect_data=405)

