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
    "netappfiles resource query-region-info",
)
class QueryRegionInfo(AAZCommand):
    """Provides storage to network proximity and logical zone mapping information.

    :example: Describes region specific information
        az netappfiles resource query-region-info -l westus
    """

    _aaz_info = {
        "version": "2023-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.netapp/locations/{}/regioninfo", "2023-11-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NetAppResourceQueryRegionInfo(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetAppResourceQueryRegionInfo(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/regionInfo",
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
                    "location", self.ctx.args.location,
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
                    "api-version", "2023-11-01",
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
            _schema_on_200.availability_zone_mappings = AAZListType(
                serialized_name="availabilityZoneMappings",
            )
            _schema_on_200.storage_to_network_proximity = AAZStrType(
                serialized_name="storageToNetworkProximity",
            )

            availability_zone_mappings = cls._schema_on_200.availability_zone_mappings
            availability_zone_mappings.Element = AAZObjectType()

            _element = cls._schema_on_200.availability_zone_mappings.Element
            _element.availability_zone = AAZStrType(
                serialized_name="availabilityZone",
            )
            _element.is_available = AAZBoolType(
                serialized_name="isAvailable",
            )

            return cls._schema_on_200


class _QueryRegionInfoHelper:
    """Helper class for QueryRegionInfo"""


__all__ = ["QueryRegionInfo"]
