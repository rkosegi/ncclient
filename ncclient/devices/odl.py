# Copyright 2016 Richard Kosegi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Handler for Opendaylight specific information.
"""

from .default import DefaultDeviceHandler
from ncclient.xml_ import BASE_NS_1_0

class OdlDeviceHandler(DefaultDeviceHandler):
    def __init__(self, device_params):
        super(OdlDeviceHandler, self).__init__(device_params)
 
    def get_capabilities(self):
        return [
            "urn:ietf:params:netconf:base:1.0",
        ]
    def get_xml_base_namespace_dict(self):
        return {None: BASE_NS_1_0}