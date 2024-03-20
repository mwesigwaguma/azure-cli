# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from .generated._help import helps  # pylint: disable=unused-import
try:
    from .manual._help import helps  # pylint: disable=reimported
except ImportError:
    pass


class DataBoxEdgeManagementClientCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azure.cli.core.profiles import ResourceType
        databoxedge_custom = CliCommandType(
            operations_tmpl='azure.cli.command_modules.databoxedge.custom#{}')
        parent = super(DataBoxEdgeManagementClientCommandsLoader, self)
        parent.__init__(cli_ctx=cli_ctx, custom_command_type=databoxedge_custom,
                        resource_type=ResourceType.MGMT_DATABOXEDGE)

    def load_command_table(self, args):
        from .generated.commands import load_command_table
        from azure.cli.core.aaz import load_aaz_command_table
        try:
            from . import aaz
        except ImportError:
            aaz = None
        if aaz:
            load_aaz_command_table(
                loader=self,
                aaz_pkg_name=aaz.__name__,
                args=args
            )
        load_command_table(self, args)
        try:
            from .manual.commands import load_command_table as load_command_table_manual
            load_command_table_manual(self, args)
        except ImportError:
            pass
        return self.command_table

    def load_arguments(self, command):
        from .generated._params import load_arguments
        load_arguments(self, command)
        try:
            from .manual._params import load_arguments as load_arguments_manual
            load_arguments_manual(self, command)
        except ImportError:
            pass


COMMAND_LOADER_CLS = DataBoxEdgeManagementClientCommandsLoader
