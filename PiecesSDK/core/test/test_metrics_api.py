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

from openapi_client.api.metrics_api import MetricsApi  # noqa: E501


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MetricsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_metrics_formats(self) -> None:
        """Test case for get_metrics_formats

        /metrics/formats [GET]  # noqa: E501
        """
        pass

    def test_metrics_formats_ordered(self) -> None:
        """Test case for metrics_formats_ordered

        /metrics/formats/ordered [GET]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
