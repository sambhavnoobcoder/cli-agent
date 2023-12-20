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

from openapi_client.models.referenced_tag import ReferencedTag  # noqa: E501

class TestReferencedTag(unittest.TestCase):
    """ReferencedTag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReferencedTag:
        """Test ReferencedTag
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferencedTag`
        """
        model = ReferencedTag()  # noqa: E501
        if include_optional:
            return ReferencedTag(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                id = '',
                reference = openapi_client.models.flattened_tag.FlattenedTag(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    id = '', 
                    text = '', 
                    mechanisms = {
                        'key' : 'MANUAL'
                        }, 
                    assets = openapi_client.models.flattened_assets_[dag_safety].FlattenedAssets [DAG Safety](
                        iterable = [
                            openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                                id = '2254f2c8-5797-40e8-ac56-41166dc0e159', )
                            ], 
                        indices = {
                            'key' : 56
                            }, 
                        score = openapi_client.models.score.Score(
                            manual = 56, 
                            automatic = 56, 
                            priority = 56, 
                            reuse = 56, 
                            update = 56, ), ), 
                    created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                    updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                    deleted = , 
                    category = 'HANDLE', 
                    relationship = openapi_client.models.relationship.Relationship(
                        id = '', 
                        embeddings = openapi_client.models.embeddings.Embeddings(
                            iterable = [
                                openapi_client.models.embedding.Embedding(
                                    raw = [
                                        1.337
                                        ], 
                                    model = openapi_client.models.model.Model(
                                        id = '', 
                                        version = '', 
                                        created = , 
                                        name = '', 
                                        description = '', 
                                        cloud = True, 
                                        type = 'BALANCED', 
                                        usage = 'OCR', 
                                        bytes = openapi_client.models.byte_descriptor.ByteDescriptor(
                                            value = 33600, 
                                            readable = '33.6 KB', ), 
                                        ram = openapi_client.models.byte_descriptor.ByteDescriptor(
                                            value = 33600, 
                                            readable = '33.6 KB', ), 
                                        quantization = '', 
                                        foundation = 'GPT_3.5', 
                                        downloaded = True, 
                                        loaded = True, 
                                        unique = '', 
                                        parameters = 1.337, 
                                        provider = 'APPLE', 
                                        cpu = True, 
                                        downloading = True, ), 
                                    created = , 
                                    updated = , )
                                ], ), 
                        edges = openapi_client.models.edges.Edges(
                            iterable = [
                                openapi_client.models.node.Node(
                                    id = '', 
                                    type = 'TAG', 
                                    root = True, 
                                    created = , )
                                ], ), 
                        created = , 
                        updated = , ), 
                    interactions = 56, 
                    persons = openapi_client.models.flattened_persons.FlattenedPersons(
                        iterable = [
                            openapi_client.models.referenced_person.ReferencedPerson(
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
            return ReferencedTag(
                id = '',
        )
        """

    def testReferencedTag(self):
        """Test ReferencedTag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
