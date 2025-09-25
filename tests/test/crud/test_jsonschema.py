# Get Response
# Create the JSON schema - https://www.jsonschema.net/
# Save that schema into the name.json file
# If you want to validate the json schema - https://www.jsonschemavalidator.net/


import json
import os

import allure
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_request
from src.helpers.common_verifications import verfiy_http_status_code, verify_json_key_for_not_null
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util


class TestCreateBookingJSONSchema(object):

    def load_schema(self, file_name):  # This function will load the schema
        with open(file_name, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_schema(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        booking_id = response.json()["bookingid"]

        verfiy_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

        # Verify response with schema.json (created_booking_schema.json) stored
        file_path = os.getcwd() + "/create_booking_schema.json"
        schema = self.load_schema(file_name=file_path)

        try:
            validate(instance=response.json(), schema=schema)   # Validate our response with the schema stored
        except ValidationError as e:
            print(e.message)
            pytest.fail("Failed : JSON schema error")