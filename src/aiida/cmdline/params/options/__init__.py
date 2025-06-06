###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida-core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
"""Module with pre-defined reusable commandline options that can be used as `click` decorators."""

# AUTO-GENERATED

# fmt: off

from .callable import *
from .config import *
from .main import *
from .multivalue import *
from .overridable import *

__all__ = (
    'ALL',
    'ALL_STATES',
    'ALL_USERS',
    'APPEND_TEXT',
    'ARCHIVE_FORMAT',
    'BROKER_HOST',
    'BROKER_PASSWORD',
    'BROKER_PORT',
    'BROKER_PROTOCOL',
    'BROKER_USERNAME',
    'BROKER_VIRTUAL_HOST',
    'CALCULATION',
    'CALCULATIONS',
    'CALC_JOB_STATE',
    'CODE',
    'CODES',
    'COMPUTER',
    'COMPUTERS',
    'CONFIG_FILE',
    'DATA',
    'DATUM',
    'DB_BACKEND',
    'DB_ENGINE',
    'DB_HOST',
    'DB_NAME',
    'DB_PASSWORD',
    'DB_PORT',
    'DB_USERNAME',
    'DEBUG',
    'DESCRIPTION',
    'DICT_FORMAT',
    'DICT_KEYS',
    'DRY_RUN',
    'EXIT_STATUS',
    'EXPORT_FORMAT',
    'FAILED',
    'FORCE',
    'FORMULA_MODE',
    'FREQUENCY',
    'GROUP',
    'GROUPS',
    'GROUP_CLEAR',
    'HOSTNAME',
    'IDENTIFIER',
    'INPUT_FORMAT',
    'INPUT_PLUGIN',
    'LABEL',
    'LIMIT',
    'NODE',
    'NODES',
    'NON_INTERACTIVE',
    'OLDER_THAN',
    'ORDER_BY',
    'ORDER_DIRECTION',
    'PAST_DAYS',
    'PAUSED',
    'PORT',
    'PREPEND_TEXT',
    'PRINT_TRACEBACK',
    'PROCESS_LABEL',
    'PROCESS_STATE',
    'PROFILE',
    'PROFILE_ONLY_CONFIG',
    'PROFILE_SET_DEFAULT',
    'PROJECT',
    'RAW',
    'REPOSITORY_PATH',
    'SCHEDULER',
    'SILENT',
    'SORT',
    'TIMEOUT',
    'TRAJECTORY_INDEX',
    'TRANSPORT',
    'TRAVERSAL_RULE_HELP_STRING',
    'TYPE_STRING',
    'USER',
    'USER_EMAIL',
    'USER_FIRST_NAME',
    'USER_INSTITUTION',
    'USER_LAST_NAME',
    'VERBOSITY',
    'VISUALIZATION_FORMAT',
    'WAIT',
    'WITH_ELEMENTS',
    'WITH_ELEMENTS_EXCLUSIVE',
    'CallableDefaultOption',
    'ConfigFileOption',
    'MultipleValueOption',
    'OverridableOption',
    'active_process_states',
    'graph_traversal_rules',
    'valid_calc_job_states',
    'valid_process_states',
)

# fmt: on
