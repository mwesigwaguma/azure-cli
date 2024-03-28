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
    "afd waf-log-analytic ranking list",
)
class List(AAZCommand):
    """Get WAF log analytics charts for AFD profile
    """

    _aaz_info = {
        "version": "2024-02-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}/getwafloganalyticsrankings", "2024-02-01"],
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
        _args_schema.profile_name = AAZStrArg(
            options=["--profile-name"],
            help="Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group. which is unique within the resource group.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.actions = AAZListArg(
            options=["--actions"],
        )
        _args_schema.date_time_begin = AAZDateTimeArg(
            options=["--date-time-begin"],
            help="The start datetime.",
            required=True,
        )
        _args_schema.date_time_end = AAZDateTimeArg(
            options=["--date-time-end"],
            help="The end datetime.",
            required=True,
        )
        _args_schema.max_ranking = AAZIntArg(
            options=["--max-ranking"],
            help="The maximum number of rows to return based on the ranking.",
            required=True,
        )
        _args_schema.metrics = AAZListArg(
            options=["--metrics"],
            required=True,
        )
        _args_schema.rankings = AAZListArg(
            options=["--rankings"],
            required=True,
        )
        _args_schema.rule_types = AAZListArg(
            options=["--rule-types"],
        )

        actions = cls._args_schema.actions
        actions.Element = AAZStrArg(
            enum={"allow": "allow", "block": "block", "log": "log", "redirect": "redirect"},
        )

        metrics = cls._args_schema.metrics
        metrics.Element = AAZStrArg(
            enum={"clientRequestCount": "clientRequestCount"},
        )

        rankings = cls._args_schema.rankings
        rankings.Element = AAZStrArg(
            enum={"action": "action", "clientIp": "clientIp", "countryOrRegion": "countryOrRegion", "ruleGroup": "ruleGroup", "ruleId": "ruleId", "ruleType": "ruleType", "url": "url", "userAgent": "userAgent"},
        )

        rule_types = cls._args_schema.rule_types
        rule_types.Element = AAZStrArg(
            enum={"bot": "bot", "custom": "custom", "managed": "managed"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.LogAnalyticsGetWafLogAnalyticsRankings(ctx=self.ctx)()
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

    class LogAnalyticsGetWafLogAnalyticsRankings(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getWafLogAnalyticsRankings",
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
                    "actions", self.ctx.args.actions,
                ),
                **self.serialize_query_param(
                    "dateTimeBegin", self.ctx.args.date_time_begin,
                    required=True,
                ),
                **self.serialize_query_param(
                    "dateTimeEnd", self.ctx.args.date_time_end,
                    required=True,
                ),
                **self.serialize_query_param(
                    "maxRanking", self.ctx.args.max_ranking,
                    required=True,
                ),
                **self.serialize_query_param(
                    "metrics", self.ctx.args.metrics,
                    required=True,
                ),
                **self.serialize_query_param(
                    "rankings", self.ctx.args.rankings,
                    required=True,
                ),
                **self.serialize_query_param(
                    "ruleTypes", self.ctx.args.rule_types,
                ),
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
            _schema_on_200.data = AAZListType()
            _schema_on_200.date_time_begin = AAZStrType(
                serialized_name="dateTimeBegin",
            )
            _schema_on_200.date_time_end = AAZStrType(
                serialized_name="dateTimeEnd",
            )
            _schema_on_200.groups = AAZListType()

            data = cls._schema_on_200.data
            data.Element = AAZObjectType()

            _element = cls._schema_on_200.data.Element
            _element.group_values = AAZListType(
                serialized_name="groupValues",
            )
            _element.metrics = AAZListType()

            group_values = cls._schema_on_200.data.Element.group_values
            group_values.Element = AAZStrType()

            metrics = cls._schema_on_200.data.Element.metrics
            metrics.Element = AAZObjectType()

            _element = cls._schema_on_200.data.Element.metrics.Element
            _element.metric = AAZStrType()
            _element.percentage = AAZFloatType()
            _element.value = AAZIntType()

            groups = cls._schema_on_200.groups
            groups.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
