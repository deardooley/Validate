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
class BatchQueue:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'customDirectives': 'str',
            'default': 'bool',
            'maxJobs': 'int',
            'maxUserJobs': 'int',
            'maxNodes': 'str',
            'maxMemoryPerNode': 'str',
            'maxProcessorsPerNode': 'int',
            'maxRequestedTime': 'str',
            'name': 'str'

        }


        #Any custom directives that should be appended to scheduler directives. ex. #$ -A TG-12345
        self.customDirectives = None # str
        #Is this the default queue for the system.
        self.default = None # bool
        #The maximum number of jobs that can be in queue at once.
        self.maxJobs = None # int
        #The maximum number of jobs per user that can be in queue at once.
        self.maxUserJobs = None # int
        #The max nodes available per node to jobs submitted to this queue.
        self.maxNodes = None # str
        #The max memory available per node to jobs submitted to this queue.
        self.maxMemoryPerNode = None # str
        #The max processors per node available to jobs submitted to this queue.
        self.maxProcessorsPerNode = None # int
        #The max length of jobs submitted to this queue in hhh:mm:ss format.
        self.maxRequestedTime = None # str
        #The name of the batch queue.
        self.name = None # str
        
