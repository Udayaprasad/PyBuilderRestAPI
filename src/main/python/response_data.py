#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 22:32:46 2019

@author: uvakalapudi
"""
import json

#Used to send the Positive APIResponse
class APIPosResponse(object):
    def __init__(self, character_name, movie_name, quotes):
        self.character_name = character_name
        self.movie_name = movie_name
        self.quotes = quotes
    
    def convertToJSON(self):
        return_response = {
            "character_name": self.character_name,
            "movie_name": self.movie_name,
            "quotes": self.quotes
            }
        return json.dumps(return_response)

#Used to send the Negative APIResponse
class APINegResponse(object):
    def __init__(self, request_type, response_codes):
        self.request_type = request_type
        self.response_codes = response_codes
    
    def convertToJSON(self):
        return_response = {
            "request_type": self.request_type,
            "response_codes": self.response_codes
            }
        return json.dumps(return_response)
        
        