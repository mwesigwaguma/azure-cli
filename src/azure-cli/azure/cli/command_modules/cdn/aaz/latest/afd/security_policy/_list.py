# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "afd security-policy list",
)
class List(AAZCommand):
    """List security policies associated with the profile
    """

    _aaz_info = {
        "version": "2024-02-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}/securitypolicies", "2024-02-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SecurityPoliciesListByProfile(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class SecurityPoliciesListByProfile(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/securityPolicies",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "profileName", self.ctx.args.profile_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-02-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.deployment_status = AAZStrType(
                serialized_name="deploymentStatus",
                flags={"read_only": True},
            )
            properties.parameters = AAZObjectType()
            properties.profile_name = AAZStrType(
                serialized_name="profileName",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            parameters = cls._schema_on_200.value.Element.properties.parameters
            parameters.type = AAZStrType(
                flags={"required": True},
            )

            disc_web_application_firewall = cls._schema_on_200.value.Element.properties.parameters.discriminate_by("type", "WebApplicationFirewall")
            disc_web_application_firewall.associations = AAZListType()
            disc_web_application_firewall.waf_policy = AAZObjectType(
                serialized_name="wafPolicy",
            )

            associations = cls._schema_on_200.value.Element.properties.parameters.discriminate_by("type", "WebApplicationFirewall").associations
            associations.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.parameters.discriminate_by("type", "WebApplicationFirewall").associations.Element
            _element.domains = AAZListType()
            _element.patterns_to_match = AAZListType(
                serialized_name="patternsToMatch",
            )

            domains = cls._schema_on_200.value.Element.properties.parameters.discriminate_by("type", "WebApplicationFirewall").associations.Element.domains
            domains.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.parameters.discriminate_by("type", "WebApplicationFirewall").associations.Element.domains.Element
            _element.id = AAZStrType()
            _element.is_active = AAZBoolType(
                serialized_name="isActive",
                flags={"read_only": True},
            )

            patterns_to_match = cls._schema_on_200.value.Element.properties.parameters.discriminate_by("type", "WebApplicationFirewall").associations.Element.patterns_to_match
            patterns_to_match.Element = AAZStrType()

            waf_policy = cls._schema_on_200.value.Element.properties.parameters.discriminate_by("type", "WebApplicationFirewall").waf_policy
            waf_policy.id = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
