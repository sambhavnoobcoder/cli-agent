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

from openapi_client.api.models_api import ModelsApi  # noqa: E501


class TestModelsApi(unittest.TestCase):
    """ModelsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ModelsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_models_create_new_model(self) -> None:
        """Test case for models_create_new_model

        /models/create [POST]  # noqa: E501
        """
        pass

    def test_models_delete_specific_model(self) -> None:
        """Test case for models_delete_specific_model

        /models/{model}/delete [POST]  # noqa: E501
        """
        pass

    def test_models_snapshot(self) -> None:
        """Test case for models_snapshot

        /models [GET]  # noqa: E501
        """
        pass

    def test_unload_models(self) -> None:
        """Test case for unload_models

        /models/unload [POST]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
