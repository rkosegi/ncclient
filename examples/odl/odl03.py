#!/usr/bin/env python
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

'''
Create simple network topology configuration
'''

from ncclient import manager

import logging

logging.basicConfig(level=logging.DEBUG)

xml_data = """
    <config>
        <network-topology xmlns="urn:TBD:params:xml:ns:yang:network-topology">
            <topology>
                <topology-id>11</topology-id>
                <link>
                    <link-id>from2to1</link-id>
                    <destination>
                        <dest-tp>eth0</dest-tp>
                        <dest-node>node1</dest-node>
                    </destination>
                    <source>
                        <source-node>node2</source-node>
                        <source-tp>eth0</source-tp>
                    </source>
                </link>
                <node>
                    <node-id>node2</node-id>
                    <termination-point>
                        <tp-id>eth0</tp-id>
                    </termination-point>
                </node>
                <node>
                    <node-id>node1</node-id>
                    <termination-point>
                        <tp-id>eth0</tp-id>
                    </termination-point>
                </node>
            </topology>
        </network-topology> 
    </config>"""

def connect(host, port, user, password):
    with manager.connect(host=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
            device_params={'name':'odl'},
            hostkey_verify=False, allow_agent=False,
                     look_for_keys=False) as conn:

        conn.edit_config(config=xml_data,  default_operation="merge", target="candidate")

if __name__ == '__main__':
    connect('localhost', 2830, 'admin', 'admin')
