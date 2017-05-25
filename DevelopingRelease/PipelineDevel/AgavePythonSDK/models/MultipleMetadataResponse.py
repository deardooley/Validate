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
class MultipleMetadataResponse:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'message': 'str',
            'result': 'list[MetadataResponse]',
            'status': 'str',
            'version': 'str'

        }


        #Error message caused by this request
        self.message = None # str
        #Metadata resources matching the query.
        self.result = None # list[MetadataResponse]
        #success or failure
        self.status = None # str
        #API version number
        self.version = None # str
        
