#!/usr/bin/env python
"""
Copyright 2012 Wordnik, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Metadata:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'associationIds': 'list[str]',
            'created': 'date-time',
            'internalUsername': 'str',
            'lastUpdated': 'date-time',
            'name': 'str',
            'owner': 'str',
            'uuid': 'str',
            'value': 'str'

        }


        #UUIDs of associated Agave entities, including the Data to which this Metadata belongs.
        self.associationIds = None # list[str]
        #A timestamp indicating when this Metadata was created in the metadata store.
        self.created = None # date-time
        #The name of the Internal User, if any, who owns this metadata.
        self.internalUsername = None # str
        #A timestamp indicating when this Metadata was last updated in the metadata store.
        self.lastUpdated = None # date-time
        #The name of this metadata
        self.name = None # str
        #The API user who owns this Metadata.
        self.owner = None # str
        #The UUID for this Metadata.
        self.uuid = None # str
        #A free text or JSON string containing the metadata stored for the given associationIds
        self.value = None # str
        
