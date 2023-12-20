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

from openapi_client.models.seeded_git_hub_distribution import SeededGitHubDistribution  # noqa: E501

class TestSeededGitHubDistribution(unittest.TestCase):
    """SeededGitHubDistribution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SeededGitHubDistribution:
        """Test SeededGitHubDistribution
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SeededGitHubDistribution`
        """
        model = SeededGitHubDistribution()  # noqa: E501
        if include_optional:
            return SeededGitHubDistribution(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                gist = openapi_client.models.seeded_git_hub_gist_distribution.SeededGitHubGistDistribution(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    recipients = openapi_client.models.recipients.Recipients(
                        iterable = [
                            openapi_client.models.person_basic_type.PersonBasicType(
                                username = '', 
                                name = '', 
                                picture = '', 
                                email = '', 
                                sourced = 'TWITTER', 
                                url = '', 
                                mailgun = openapi_client.models.mailgun_metadata.MailgunMetadata(
                                    message_id = '', ), )
                            ], ), 
                    public = True, 
                    description = '', 
                    name = '', )
            )
        else:
            return SeededGitHubDistribution(
        )
        """

    def testSeededGitHubDistribution(self):
        """Test SeededGitHubDistribution"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
