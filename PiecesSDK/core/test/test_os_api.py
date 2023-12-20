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

from openapi_client.api.os_api import OSApi  # noqa: E501


class TestOSApi(unittest.TestCase):
    """OSApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OSApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_link_provider(self) -> None:
        """Test case for link_provider

        /os/link_provider [POST]  # noqa: E501
        """
        pass

    def test_os_restart(self) -> None:
        """Test case for os_restart

        Your GET endpoint  # noqa: E501
        """
        pass

    def test_pick_files(self) -> None:
        """Test case for pick_files

        /os/files/pick [POST]  # noqa: E501
        """
        pass

    def test_pick_folders(self) -> None:
        """Test case for pick_folders

        /os/folders/pick [POST]  # noqa: E501
        """
        pass

    def test_sign_into_os(self) -> None:
        """Test case for sign_into_os

          # noqa: E501
        """
        pass

    def test_sign_out_of_os(self) -> None:
        """Test case for sign_out_of_os

        /os/sign_out [POST]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
