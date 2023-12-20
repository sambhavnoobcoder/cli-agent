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

from openapi_client.models.accessor import Accessor  # noqa: E501

class TestAccessor(unittest.TestCase):
    """Accessor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Accessor:
        """Test Accessor
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Accessor`
        """
        model = Accessor()  # noqa: E501
        if include_optional:
            return Accessor(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                id = '',
                os = '',
                share = '',
                count = 56,
                user = openapi_client.models.flattened_user_profile.FlattenedUserProfile(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    id = '', 
                    email = '', 
                    name = '', 
                    username = '', 
                    picture = '', 
                    vanityname = '', )
            )
        else:
            return Accessor(
                id = '',
                os = '',
                share = '',
                count = 56,
        )
        """

    def testAccessor(self):
        """Test Accessor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
