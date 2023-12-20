# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field
from openapi_client.models.embedded_model_schema import EmbeddedModelSchema
from openapi_client.models.text_location import TextLocation

class TextMatch(BaseModel):
    """
    Thext Match currently used for sensitive for scales for people, and anything related to text matching.  group: is the entire match subgroup is the inner match within the group.(optional)  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    group: TextLocation = Field(...)
    subgroup: Optional[TextLocation] = None
    __properties = ["schema", "group", "subgroup"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TextMatch:
        """Create an instance of TextMatch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subgroup
        if self.subgroup:
            _dict['subgroup'] = self.subgroup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TextMatch:
        """Create an instance of TextMatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TextMatch.parse_obj(obj)

        _obj = TextMatch.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "group": TextLocation.from_dict(obj.get("group")) if obj.get("group") is not None else None,
            "subgroup": TextLocation.from_dict(obj.get("subgroup")) if obj.get("subgroup") is not None else None
        })
        return _obj


