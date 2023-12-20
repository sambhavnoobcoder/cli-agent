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

from openapi_client.models.seeded_mac_os_asset import SeededMacOSAsset  # noqa: E501

class TestSeededMacOSAsset(unittest.TestCase):
    """SeededMacOSAsset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SeededMacOSAsset:
        """Test SeededMacOSAsset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SeededMacOSAsset`
        """
        model = SeededMacOSAsset()  # noqa: E501
        if include_optional:
            return SeededMacOSAsset(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                application = openapi_client.models.application.Application(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    id = '', 
                    name = 'SUBLIME', 
                    version = '', 
                    platform = 'WEB', 
                    onboarded = True, 
                    privacy = 'OPEN', 
                    capabilities = 'LOCAL', 
                    mechanism = 'MANUAL', 
                    automatic_unload = True, ),
                value = 'console.log("hello world")'
            )
        else:
            return SeededMacOSAsset(
                value = 'console.log("hello world")',
        )
        """

    def testSeededMacOSAsset(self):
        """Test SeededMacOSAsset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
