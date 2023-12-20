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

from openapi_client.models.referenced_share import ReferencedShare  # noqa: E501

class TestReferencedShare(unittest.TestCase):
    """ReferencedShare unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReferencedShare:
        """Test ReferencedShare
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferencedShare`
        """
        model = ReferencedShare()  # noqa: E501
        if include_optional:
            return ReferencedShare(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                id = '',
                reference = openapi_client.models.flattened_share_[dag_safe].FlattenedShare [DAG SAFE](
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    id = '', 
                    asset = '', 
                    user = '', 
                    link = '', 
                    access = 'PUBLIC', 
                    accessors = openapi_client.models.accessors.Accessors(
                        iterable = [
                            openapi_client.models.accessor.Accessor(
                                id = '', 
                                os = '', 
                                share = '', 
                                count = 56, 
                                user = openapi_client.models.flattened_user_profile.FlattenedUserProfile(
                                    id = '', 
                                    email = '', 
                                    name = '', 
                                    username = '', 
                                    picture = '', 
                                    vanityname = '', ), )
                            ], ), 
                    created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                    short = '', 
                    name = '', 
                    assets = openapi_client.models.flattened_assets_[dag_safety].FlattenedAssets [DAG Safety](
                        indices = {
                            'key' : 56
                            }, 
                        score = openapi_client.models.score.Score(
                            manual = 56, 
                            automatic = 56, 
                            priority = 56, 
                            reuse = 56, 
                            update = 56, ), ), 
                    distributions = openapi_client.models.flattened_distributions.FlattenedDistributions(
                        iterable = [
                            openapi_client.models.referenced_distribution.ReferencedDistribution(
                                id = '', )
                            ], ), 
                    score = openapi_client.models.score.Score(
                        manual = 56, 
                        automatic = 56, 
                        priority = 56, 
                        reuse = 56, 
                        update = 56, ), )
            )
        else:
            return ReferencedShare(
                id = '',
        )
        """

    def testReferencedShare(self):
        """Test ReferencedShare"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
