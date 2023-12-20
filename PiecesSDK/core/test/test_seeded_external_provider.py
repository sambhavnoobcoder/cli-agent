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

from openapi_client.models.seeded_external_provider import SeededExternalProvider  # noqa: E501

class TestSeededExternalProvider(unittest.TestCase):
    """SeededExternalProvider unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SeededExternalProvider:
        """Test SeededExternalProvider
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SeededExternalProvider`
        """
        model = SeededExternalProvider()  # noqa: E501
        if include_optional:
            return SeededExternalProvider(
                type = 'github'
            )
        else:
            return SeededExternalProvider(
                type = 'github',
        )
        """

    def testSeededExternalProvider(self):
        """Test SeededExternalProvider"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
