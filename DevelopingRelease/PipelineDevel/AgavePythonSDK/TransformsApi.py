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


class TransformsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def list(self, **kwargs):
        """Find all transforms for use within the api.

        Args:
            
        Returns: MultipleTransformResponse
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method list" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transforms/2.0/'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'MultipleTransformResponse')
        return responseObject
        
        
    def get(self, transformId, **kwargs):
        """Find all transforms matching the given name.

        Args:
            transformId, str: The name of the transform requested. (required)
            
        Returns: MultipleTransformResponse
        """

        allParams = ['transformId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transforms/2.0/{transformId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('transformId' in params):
            replacement = str(self.apiClient.toPathValue(params['transformId']))
            resourcePath = resourcePath.replace('{' + 'transformId' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'MultipleTransformResponse')
        return responseObject
        
        
    def transformAndStage(self, transformId, owner, filePath, url, **kwargs):
        """Transform a file and stage it to a specified location.

        Args:
            transformId, str: The name of the transform to apply to the given file. (required)
            owner, str: The name of the api user owning the file at the given path. (required)
            filePath, str: The path to the file to be transformed and staged (required)
            native_format, str: The original file type of the file. If not given, the file type is assumed to be raw. (optional)
            url, str: The uri to which the transformed file will be staged. (required)
            callbackURL, str: The URI to notify when the transfer is complete. This can be an email address or http URL. If a URL is given, a GET will be made to this address. URL templating is supported. Valid template values are: ${NAME}, ${SOURCE_FORMAT}, ${DEST_FORMAT}, ${STATUS} (optional)
            
        Returns: MultipleTransformResponse
        """

        allParams = ['transformId', 'owner', 'filePath', 'native_format', 'url', 'callbackURL']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method transformAndStage" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transforms/2.0/{transformId}/async/{owner}/{filePath}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('transformId' in params):
            replacement = str(self.apiClient.toPathValue(params['transformId']))
            resourcePath = resourcePath.replace('{' + 'transformId' + '}',
                                                replacement)
        if ('owner' in params):
            replacement = str(self.apiClient.toPathValue(params['owner']))
            resourcePath = resourcePath.replace('{' + 'owner' + '}',
                                                replacement)
        if ('filePath' in params):
            replacement = str(self.apiClient.toPathValue(params['filePath']))
            resourcePath = resourcePath.replace('{' + 'filePath' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'MultipleTransformResponse')
        return responseObject
        
        
    def transformAndDownload(self, transformId, owner, filePath, **kwargs):
        """Transform a file and download it directly.

        Args:
            transformId, str: The name of the transform to apply to the given file. (required)
            owner, str: The name of the api user owning the file at the given path. (required)
            filePath, str: The path to the file to be transformed and downloaded. (required)
            native_format, str: The original file type of the file. If not given, the file type is assumed to be raw. (optional)
            
        Returns: TransfomFileDownload
        """

        allParams = ['transformId', 'owner', 'filePath', 'native_format']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method transformAndDownload" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transforms/2.0/{transformId}/sync/{owner}/{filePath}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('transformId' in params):
            replacement = str(self.apiClient.toPathValue(params['transformId']))
            resourcePath = resourcePath.replace('{' + 'transformId' + '}',
                                                replacement)
        if ('owner' in params):
            replacement = str(self.apiClient.toPathValue(params['owner']))
            resourcePath = resourcePath.replace('{' + 'owner' + '}',
                                                replacement)
        if ('filePath' in params):
            replacement = str(self.apiClient.toPathValue(params['filePath']))
            resourcePath = resourcePath.replace('{' + 'filePath' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'TransfomFileDownload')
        return responseObject
        
        
    def listByTag(self, tag, **kwargs):
        """Find all transforms with the given tag.

        Args:
            tag, str: The tag to search for transforms on. (required)
            
        Returns: MultipleTransformResponse
        """

        allParams = ['tag']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method listByTag" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transforms/2.0/tags/{tag}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('tag' in params):
            replacement = str(self.apiClient.toPathValue(params['tag']))
            resourcePath = resourcePath.replace('{' + 'tag' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'MultipleTransformResponse')
        return responseObject
        
        
    


