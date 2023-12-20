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

from openapi_client.models.tag import Tag  # noqa: E501

class TestTag(unittest.TestCase):
    """Tag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tag:
        """Test Tag
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tag`
        """
        model = Tag()  # noqa: E501
        if include_optional:
            return Tag(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                id = '',
                text = '',
                mechanisms = {
                    'key' : 'MANUAL'
                    },
                assets = openapi_client.models.flattened_assets_[dag_safety].FlattenedAssets [DAG Safety](
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                            id = '2254f2c8-5797-40e8-ac56-41166dc0e159', 
                            reference = openapi_client.models.flattened_asset_[dag_safety].FlattenedAsset [DAG Safety](
                                id = '2254f2c8-5797-40e8-ac56-41166dc0e159', 
                                name = '', 
                                creator = '497f6eca-6276-4993-bfeb-53cbbbba6f08', 
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                synced = , 
                                deleted = , 
                                formats = openapi_client.models.flattened_formats.FlattenedFormats(
                                    iterable = [
                                        openapi_client.models.referenced_format_[dag_safety].ReferencedFormat [DAG Safety](
                                            id = '102ff265-fdfb-4142-8d94-4932d400199c', )
                                        ], ), 
                                preview = openapi_client.models.flattened_preview.FlattenedPreview(
                                    base = '', 
                                    overlay = '', ), 
                                original = '0872ccbf-1d8f-4f46-9028-469794d72761', 
                                shares = openapi_client.models.flattened_shares_[dag_safe].FlattenedShares [DAG Safe](
                                    iterable = [
                                        openapi_client.models.flattened_share_[dag_safe].FlattenedShare [DAG SAFE](
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
                                            created = , 
                                            short = '', 
                                            name = '', 
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
                                        ], 
                                    score = openapi_client.models.score.Score(
                                        manual = 56, 
                                        automatic = 56, 
                                        priority = 56, 
                                        reuse = 56, 
                                        update = 56, ), ), 
                                mechanism = 'MANUAL', 
                                websites = openapi_client.models.flattened_websites.FlattenedWebsites(
                                    iterable = [
                                        openapi_client.models.referenced_website.ReferencedWebsite(
                                            id = '', )
                                        ], 
                                    indices = {
                                        'key' : 56
                                        }, ), 
                                interacted = , 
                                tags = openapi_client.models.flattened_tags.FlattenedTags(
                                    iterable = [
                                        openapi_client.models.referenced_tag.ReferencedTag(
                                            id = '', )
                                        ], ), 
                                sensitives = openapi_client.models.flattened_sensitives.FlattenedSensitives(
                                    iterable = [
                                        openapi_client.models.referenced_sensitive.ReferencedSensitive(
                                            id = '', )
                                        ], ), 
                                persons = openapi_client.models.flattened_persons.FlattenedPersons(
                                    iterable = [
                                        openapi_client.models.referenced_person.ReferencedPerson(
                                            id = '', )
                                        ], ), 
                                curated = True, 
                                discovered = True, 
                                activities = openapi_client.models.flattened_activities.FlattenedActivities(
                                    iterable = [
                                        openapi_client.models.referenced_activity.ReferencedActivity(
                                            id = '', )
                                        ], ), 
                                score = , 
                                favorited = True, 
                                pseudo = True, 
                                annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                    iterable = [
                                        openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                            id = '', )
                                        ], ), 
                                hints = openapi_client.models.flattened_hints.FlattenedHints(
                                    iterable = [
                                        openapi_client.models.referenced_hint.ReferencedHint(
                                            id = '', )
                                        ], ), 
                                anchors = openapi_client.models.flattened_anchors.FlattenedAnchors(
                                    iterable = [
                                        openapi_client.models.referenced_anchor.ReferencedAnchor(
                                            id = '', )
                                        ], ), 
                                conversations = openapi_client.models.flattened_conversations.FlattenedConversations(
                                    iterable = [
                                        openapi_client.models.referenced_conversation.ReferencedConversation(
                                            id = '', )
                                        ], ), ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = , ),
                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                deleted = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                category = 'HANDLE',
                relationship = openapi_client.models.relationship.Relationship(
                    id = '', 
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    embeddings = openapi_client.models.embeddings.Embeddings(
                        iterable = [
                            openapi_client.models.embedding.Embedding(
                                raw = [
                                    1.337
                                    ], 
                                model = openapi_client.models.model.Model(
                                    id = '', 
                                    version = '', 
                                    created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
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
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = , 
                                deleted = , )
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
                    updated = , 
                    deleted = , ),
                interactions = 56,
                persons = openapi_client.models.flattened_persons.FlattenedPersons(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.referenced_person.ReferencedPerson(
                            id = '', 
                            reference = openapi_client.models.flattened_person.FlattenedPerson(
                                id = '', 
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                deleted = , 
                                type = openapi_client.models.person_type.PersonType(
                                    basic = openapi_client.models.person_basic_type.PersonBasicType(
                                        username = '', 
                                        name = '', 
                                        picture = '', 
                                        email = '', 
                                        sourced = 'TWITTER', 
                                        url = '', 
                                        mailgun = openapi_client.models.mailgun_metadata.MailgunMetadata(
                                            message_id = '', ), ), 
                                    platform = openapi_client.models.user_profile.UserProfile(
                                        picture = 'https://picsum.photos/200', 
                                        email = 'user@pieces.app', 
                                        username = '', 
                                        id = '', 
                                        name = '', 
                                        aesthetics = openapi_client.models.aesthetics.Aesthetics(
                                            theme = openapi_client.models.theme.Theme(
                                                dark = True, ), 
                                            font = openapi_client.models.font.Font(
                                                size = 56, ), ), 
                                        vanityname = '', 
                                        allocation = openapi_client.models.allocation_cloud.AllocationCloud(
                                            id = '', 
                                            user = '', 
                                            urls = openapi_client.models.allocation_cloud_urls.AllocationCloudUrls(
                                                base = openapi_client.models.allocation_cloud_url.AllocationCloudUrl(
                                                    status = 'PENDING', 
                                                    url = '', ), 
                                                id = openapi_client.models.allocation_cloud_url.AllocationCloudUrl(
                                                    status = 'PENDING', 
                                                    url = '', ), 
                                                vanity = , ), 
                                            status = openapi_client.models.allocation_cloud_status.AllocationCloudStatus(
                                                cloud = 'PENDING', ), 
                                            project = '', 
                                            version = '', 
                                            region = '', ), 
                                        providers = openapi_client.models.external_providers.ExternalProviders(
                                            iterable = [
                                                openapi_client.models.external_provider.ExternalProvider(
                                                    type = 'github', 
                                                    user_id = '', 
                                                    access_token = '', 
                                                    expires_in = 56, 
                                                    created = , 
                                                    updated = , 
                                                    profile_data = openapi_client.models.external_provider_profile_data.ExternalProviderProfileData(
                                                        name = '', 
                                                        picture = '', 
                                                        nickname = '', 
                                                        email = '', 
                                                        email_verified = True, 
                                                        node_id = '', 
                                                        gravatar_id = '', 
                                                        url = '', 
                                                        html_url = '', 
                                                        followers_url = '', 
                                                        following_url = '', 
                                                        gists_url = '', 
                                                        starred_url = '', 
                                                        subscriptions_url = '', 
                                                        organizations_url = '', 
                                                        repos_url = '', 
                                                        events_url = '', 
                                                        received_events_url = '', 
                                                        site_admin = True, 
                                                        company = '', 
                                                        blog = '', 
                                                        anchor = '', 
                                                        hireable = True, 
                                                        bio = '', 
                                                        twitter_username = '', 
                                                        public_repos = 56, 
                                                        public_gists = 56, 
                                                        followers = 56, 
                                                        following = 56, 
                                                        created_at = '', 
                                                        updated_at = '', 
                                                        private_gists = 56, 
                                                        total_private_repos = 56, 
                                                        owned_private_repos = 56, 
                                                        disk_usage = 56, 
                                                        collaborators = 56, 
                                                        two_factor_authentication = True, ), 
                                                    connection = '', 
                                                    is_social = True, )
                                                ], ), 
                                        auth0 = openapi_client.models.auth0_user_metadata.Auth0UserMetadata(
                                            global_id = '', 
                                            cloud_key = '', 
                                            stripe_customer_id = '', 
                                            vanityname = '', ), ), ), 
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
                                mechanisms = {
                                    'key' : 'MANUAL'
                                    }, 
                                interactions = 56, 
                                access = {
                                    'key' : openapi_client.models.person_access.PersonAccess(
                                        scoped = 'OWNER', )
                                    }, 
                                tags = openapi_client.models.flattened_tags.FlattenedTags(
                                    iterable = [
                                        openapi_client.models.referenced_tag.ReferencedTag(
                                            id = '', )
                                        ], ), 
                                websites = openapi_client.models.flattened_websites.FlattenedWebsites(
                                    iterable = [
                                        openapi_client.models.referenced_website.ReferencedWebsite(
                                            id = '', )
                                        ], ), 
                                models = {
                                    'key' : openapi_client.models.person_model.PersonModel(
                                        asset = openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                                            id = '2254f2c8-5797-40e8-ac56-41166dc0e159', ), 
                                        model = openapi_client.models.referenced_model.ReferencedModel(
                                            id = '', ), 
                                        explanation = openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                            id = '', ), )
                                    }, 
                                annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                    iterable = [
                                        openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                            id = '', )
                                        ], ), 
                                score = openapi_client.models.score.Score(
                                    manual = 56, 
                                    automatic = 56, 
                                    priority = 56, 
                                    reuse = 56, 
                                    update = 56, ), ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = , ),
                score = openapi_client.models.score.Score(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    manual = 56, 
                    automatic = 56, 
                    priority = 56, 
                    reuse = 56, 
                    update = 56, 
                    reference = 56, )
            )
        else:
            return Tag(
                id = '',
                text = '',
                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    readable = 'Last week - June 3rd, 3:33 a.m.', ),
                category = 'HANDLE',
        )
        """

    def testTag(self):
        """Test Tag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
