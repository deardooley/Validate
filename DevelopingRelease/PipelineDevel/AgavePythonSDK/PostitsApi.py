#!/usr/bin/env python
"""
WordAPI.py
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

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *


class PostitsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def list(self, **kwargs):
        """List existing PostIts

        Args:
            
        Returns: MultiplePostItResponse
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method list" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/postits/2.0/'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'MultiplePostItResponse')
        return responseObject
        
        
    def create(self, **kwargs):
        """Create a new PostIt

        Args:
            username, str: The username of a valid API user for whom this token will be generated. Default: the authenticated user (optional)
            internalUsername, str: The username of a valid internal user to associate with this token. Default: empty (optional)
            lifetime, int: The number of seconds this token should remain valid. Default: 2592000 (30 days) (optional)
            maxUses, int: The maximum number of times this token can be used. Default: 1 (optional)
            url, str: The target URL this PostIt should invoke. (optional)
            noauth, bool: Whether this the target URL should be called without authentication. Default: false (optional)
            
        Returns: PostIt
        """

        allParams = ['username', 'internalUsername', 'lifetime', 'maxUses', 'url', 'noauth']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method create" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/postits/2.0/'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'PostIt')
        return responseObject
        
        
    def delete(self, nonce, **kwargs):
        """Immediately invalidates this PostIt URL.

        Args:
            nonce, str: The nonce of this PostIt URL (required)
            
        Returns: SinglePostItResponse
        """

        allParams = ['nonce']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/postits/2.0/{nonce}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        if ('nonce' in params):
            replacement = str(self.apiClient.toPathValue(params['nonce']))
            resourcePath = resourcePath.replace('{' + 'nonce' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SinglePostItResponse')
        return responseObject
        
        
    


