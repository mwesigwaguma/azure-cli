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
    "cdn endpoint purge",
)
class Purge(AAZCommand):
    """Removes a content from CDN.

    :example: Purge pre-loaded Javascript and CSS content.
        az cdn endpoint purge -g group -n endpoint --profile-name profile-name --content-paths '/scripts/app.js' '/styles/*'
    """

    _aaz_info = {
        "version": "2023-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}/endpoints/{}/purge", "2023-05-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.endpoint_name = AAZStrArg(
            options=["-n", "--name", "--endpoint-name"],
            help="Name of the endpoint under the profile which is unique globally.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="Name of the CDN profile which is unique within the resource group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "ContentFilePaths"

        _args_schema = cls._args_schema
        _args_schema.content_paths = AAZListArg(
            options=["--content-paths"],
            arg_group="ContentFilePaths",
            help="The path to the content to be purged. Can describe a file path or a wild card directory.",
            required=True,
        )

        content_paths = cls._args_schema.content_paths
        content_paths.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.EndpointsPurgeContent(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class EndpointsPurgeContent(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/purge",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "endpointName", self.ctx.args.endpoint_name,
                    required=True,
                ),
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
                    "api-version", "2023-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("contentPaths", AAZListType, ".content_paths", typ_kwargs={"flags": {"required": True}})

            content_paths = _builder.get(".contentPaths")
            if content_paths is not None:
                content_paths.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            pass


class _PurgeHelper:
    """Helper class for Purge"""


__all__ = ["Purge"]
