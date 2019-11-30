#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:23:48 2019

@author: uvakalapudi
"""


import unittest
from parameterized import parameterized
import requests

#Unit TestCases for Webservice
class TestWebService(unittest.TestCase):
    @parameterized.expand([
        ["positive_case1", "5cd95395de30eff6ebccde5b", "5cd99d4bde30eff6ebccfea0",48,],
        ["negative_case1", "5cd95395de30eff6ebccde5b", "5cd99d4bde30eff6ebccfe07","Unable to find the character dialogs in the movie"],
        ["positive_case2", "5cd95395de30eff6ebccde5d", "5cd99d4bde30eff6ebccfe9e",75],
        ["negative_case2", "5cd95395de30eff6ebccde5", "5cd99d4bde30eff6ebccfe9e","Unable to find the movie/character in the database"],
    ])
    def test_webservice(self, test_type, movieId, characterId,total_quotes):
        request_url = "http://127.0.0.1:5000/quotes/movie/{}/character/{}".format(movieId,characterId) 
        response_data = requests.get(request_url)
        
        if("quotes" in response_data.json()):
            quotes = response_data.json()["quotes"]
            quote_len = len(quotes)
        else:
            quote_len = response_data.json()["response_codes"]["Reason"]
        
        self.assertEqual(quote_len,total_quotes)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWebService)
    unittest.TextTestRunner(verbosity=2).run(suite)