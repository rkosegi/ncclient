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
Reads netconf topology data
'''

from ncclient import manager


topo_filter = """
      <network-topology xmlns="urn:TBD:params:xml:ns:yang:network-topology">
          <topology>
              <topology-id>topology-netconf</topology-id>
          </topology>
      </network-topology> """

def connect(host, port, user, password):
    with manager.connect(host=host,
            port=port,
            username=user,
            password=password,
            timeout=10,
            device_params={'name':'odl'},
            hostkey_verify=False, allow_agent=False,
                     look_for_keys=False) as conn:

        print(conn.get(("subtree", topo_filter)))

if __name__ == '__main__':
    connect('localhost', 2830, 'admin', 'admin')
