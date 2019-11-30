#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:42:52 2019

@author: Uday Vakalapudi
"""

from flask import Flask
from response_data import APIPosResponse, APINegResponse
import requests
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()

# Read the configuration file to load the important parameters like Bearer Token, Endpoint URLs
config.read('src/main/python/project_config.ini')

characters_url = config['endpoint.urls']['characters_url']
movies_url = config['endpoint.urls']['movies_url']
common_header = {'Authorization': "Bearer "+config['Auth']['Authorization']}

characters_response = requests.request("GET", characters_url, headers=common_header)
movies_response = requests.request("GET", movies_url, headers=common_header)

#Generate gobals for character and movie IDs
characters_dict = dict([(item["_id"].rstrip(),item["name"].rstrip()) for item in characters_response.json()["docs"]])
movies_dict = dict([(item["_id"].rstrip(),item["name"].rstrip()) for item in movies_response.json()["docs"]])


@app.route('/quotes/movie/<string:movieId>/character/<string:characterId>', methods=['GET'])
def quotes_by_movie_and_character(movieId, characterId):
    ''' This WebService is responsible for returning filtered quotes by movie and character fields
        @param movieId   - movie id
        @param characterId  - character id from the same movie id

        @return  return_response - Positive Response:- {
                                      "character_name": "<<CHARACTER_NAME>>"
                                      ,"movie_name" : "<<MOVIE_NAME>>"
                                      ,"quotes" : [
                                        "quote 1"
                                        ,"quote 2"
                                        ,"quote 3"
                                      ]
                                    }

                                   Negative Response:- {
                                   "request_type": "Bad Request",
                                   "response_codes":{"quotes_url":status_code,
                                                     "Reason":XXXXXXX}
                                   }
    '''

    if(movieId in movies_dict and characterId in characters_dict):
        # Endpoint URL used to format the desired output (character_name, movie_name, quotes)
        quotes_url = config['endpoint.urls']['quotes_url'].format(
            movieId)
    
        # Get response objects from quotes_url
        quotes_response = requests.request("GET", quotes_url, headers=common_header)
        
        # If the response status for quotes_url is 200, then, send the desired output, else send the Bad Request as Response
        if(quotes_response.status_code == 200):
            character_name = characters_dict[characterId]
            movie_name = movies_dict[movieId]
            quotes = [item["dialog"].rstrip() for item in quotes_response.json()["docs"] if item["character"] == characterId]
            
            if len(quotes) > 0:
                #Serialize the response_obj by creating class for response elements
                response_obj = APIPosResponse(character_name,movie_name,quotes)
            else:
                request_type = "Bad Request"
                response_codes = {"quotes_url": quotes_response.status_code,
                                  "Reason": "Unable to find the character dialogs in the movie"}
                response_obj = APINegResponse(request_type,response_codes)
            
        else:
            request_type = "Bad Request"
            response_codes = {"quotes_url": quotes_response.status_code,
                              "Reason": "Unable to make the request"}
            response_obj = APINegResponse(request_type,response_codes)
            
    else:
        request_type = "Bad Request"
        response_codes = {"Reason": "Unable to find the movie/character in the database"}
        response_obj = APINegResponse(request_type,response_codes)
        
    return response_obj.convertToJSON()



if __name__ == '__main__':
    app.run()
