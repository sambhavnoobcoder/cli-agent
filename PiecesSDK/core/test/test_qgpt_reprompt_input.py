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

from openapi_client.models.qgpt_reprompt_input import QGPTRepromptInput  # noqa: E501

class TestQGPTRepromptInput(unittest.TestCase):
    """QGPTRepromptInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QGPTRepromptInput:
        """Test QGPTRepromptInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QGPTRepromptInput`
        """
        model = QGPTRepromptInput()  # noqa: E501
        if include_optional:
            return QGPTRepromptInput(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                query = '',
                conversation = openapi_client.models.qgpt_conversation.QGPTConversation(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.qgpt_conversation_message.QGPTConversationMessage(
                            text = '', 
                            role = 'USER', 
                            timestamp = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), )
                        ], ),
                application = '',
                model = ''
            )
        else:
            return QGPTRepromptInput(
                query = '',
                conversation = openapi_client.models.qgpt_conversation.QGPTConversation(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.qgpt_conversation_message.QGPTConversationMessage(
                            text = '', 
                            role = 'USER', 
                            timestamp = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), )
                        ], ),
        )
        """

    def testQGPTRepromptInput(self):
        """Test QGPTRepromptInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
