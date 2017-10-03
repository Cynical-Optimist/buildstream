#!/usr/bin/env python3
#
#  Copyright (C) 2017 Codethink Limited
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library. If not, see <http://www.gnu.org/licenses/>.
#
#  Authors:
#        Tristan Van Berkom <tristan.vanberkom@codethink.co.uk>

from .. import _yaml
from .. import LoadError, LoadErrorReason
from .option import Option, OPTION_SYMBOLS


# OptionBool
#
# A boolean project option
#
class OptionBool(Option):

    OPTION_TYPE = 'bool'

    def load(self, node):

        super(OptionBool, self).load(node)
        _yaml.node_validate(node, OPTION_SYMBOLS + ['default'])
        self.value = _yaml.node_get(node, bool, 'default')

    def load_value(self, node):
        self.value = _yaml.node_get(node, bool, self.name)

    def set_value(self, value):
        if value == 'True' or value == 'true':
            self.value = True
        elif value == 'False' or value == 'false':
            self.value = False
        else:
            raise LoadError(LoadErrorReason.INVALID_DATA,
                            "Invalid value for boolean option {}: {}".format(self.name, value))