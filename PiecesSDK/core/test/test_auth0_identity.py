# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.auth0_identity import Auth0Identity  # noqa: E501

class TestAuth0Identity(unittest.TestCase):
    """Auth0Identity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Auth0Identity:
        """Test Auth0Identity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Auth0Identity`
        """
        model = Auth0Identity()  # noqa: E501
        if include_optional:
            return Auth0Identity(
                connection = '',
                is_social = True,
                provider = '',
                user_id = '',
                access_token = '',
                expires_in = 56
            )
        else:
            return Auth0Identity(
        )
        """

    def testAuth0Identity(self):
        """Test Auth0Identity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
