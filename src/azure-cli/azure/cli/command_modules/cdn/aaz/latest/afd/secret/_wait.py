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
    "afd secret wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cdn/profiles/{}/secrets/{}", "2024-02-01"],
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
            help="Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.secret_name = AAZStrArg(
            options=["-n", "--name", "--secret-name"],
            help="Name of the Secret under the profile.",
            required=True,
            id_part="child_name_1",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SecretsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class SecretsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/secrets/{secretName}",
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
                    "secretName", self.ctx.args.secret_name,
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
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

            parameters = cls._schema_on_200.properties.parameters
            parameters.type = AAZStrType(
                flags={"required": True},
            )

            disc_azure_first_party_managed_certificate = cls._schema_on_200.properties.parameters.discriminate_by("type", "AzureFirstPartyManagedCertificate")
            disc_azure_first_party_managed_certificate.certificate_authority = AAZStrType(
                serialized_name="certificateAuthority",
                flags={"read_only": True},
            )
            disc_azure_first_party_managed_certificate.expiration_date = AAZStrType(
                serialized_name="expirationDate",
                flags={"read_only": True},
            )
            disc_azure_first_party_managed_certificate.secret_source = AAZObjectType(
                serialized_name="secretSource",
            )
            _WaitHelper._build_schema_resource_reference_read(disc_azure_first_party_managed_certificate.secret_source)
            disc_azure_first_party_managed_certificate.subject = AAZStrType(
                flags={"read_only": True},
            )
            disc_azure_first_party_managed_certificate.subject_alternative_names = AAZListType(
                serialized_name="subjectAlternativeNames",
            )
            disc_azure_first_party_managed_certificate.thumbprint = AAZStrType(
                flags={"read_only": True},
            )

            subject_alternative_names = cls._schema_on_200.properties.parameters.discriminate_by("type", "AzureFirstPartyManagedCertificate").subject_alternative_names
            subject_alternative_names.Element = AAZStrType(
                flags={"read_only": True},
            )

            disc_customer_certificate = cls._schema_on_200.properties.parameters.discriminate_by("type", "CustomerCertificate")
            disc_customer_certificate.certificate_authority = AAZStrType(
                serialized_name="certificateAuthority",
                flags={"read_only": True},
            )
            disc_customer_certificate.expiration_date = AAZStrType(
                serialized_name="expirationDate",
                flags={"read_only": True},
            )
            disc_customer_certificate.secret_source = AAZObjectType(
                serialized_name="secretSource",
                flags={"required": True},
            )
            _WaitHelper._build_schema_resource_reference_read(disc_customer_certificate.secret_source)
            disc_customer_certificate.secret_version = AAZStrType(
                serialized_name="secretVersion",
            )
            disc_customer_certificate.subject = AAZStrType(
                flags={"read_only": True},
            )
            disc_customer_certificate.subject_alternative_names = AAZListType(
                serialized_name="subjectAlternativeNames",
            )
            disc_customer_certificate.thumbprint = AAZStrType(
                flags={"read_only": True},
            )
            disc_customer_certificate.use_latest_version = AAZBoolType(
                serialized_name="useLatestVersion",
            )

            subject_alternative_names = cls._schema_on_200.properties.parameters.discriminate_by("type", "CustomerCertificate").subject_alternative_names
            subject_alternative_names.Element = AAZStrType(
                flags={"read_only": True},
            )

            disc_managed_certificate = cls._schema_on_200.properties.parameters.discriminate_by("type", "ManagedCertificate")
            disc_managed_certificate.expiration_date = AAZStrType(
                serialized_name="expirationDate",
                flags={"read_only": True},
            )
            disc_managed_certificate.subject = AAZStrType(
                flags={"read_only": True},
            )

            disc_url_signing_key = cls._schema_on_200.properties.parameters.discriminate_by("type", "UrlSigningKey")
            disc_url_signing_key.key_id = AAZStrType(
                serialized_name="keyId",
                flags={"required": True},
            )
            disc_url_signing_key.secret_source = AAZObjectType(
                serialized_name="secretSource",
                flags={"required": True},
            )
            _WaitHelper._build_schema_resource_reference_read(disc_url_signing_key.secret_source)
            disc_url_signing_key.secret_version = AAZStrType(
                serialized_name="secretVersion",
            )

            system_data = cls._schema_on_200.system_data
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


class _WaitHelper:
    """Helper class for Wait"""

    _schema_resource_reference_read = None

    @classmethod
    def _build_schema_resource_reference_read(cls, _schema):
        if cls._schema_resource_reference_read is not None:
            _schema.id = cls._schema_resource_reference_read.id
            return

        cls._schema_resource_reference_read = _schema_resource_reference_read = AAZObjectType()

        resource_reference_read = _schema_resource_reference_read
        resource_reference_read.id = AAZStrType()

        _schema.id = cls._schema_resource_reference_read.id


__all__ = ["Wait"]
