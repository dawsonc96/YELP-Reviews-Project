import requests
import json
import pandas as pd
import numpy as np

term = 'restaurant'
location = 'Los Angeles'
categories = 'cafe'
radius = 3500

# set theurl and endpoint we want to hit
url = 'https://api.yelp.com/v3/businesses/search'
url2 = 'https://api.yelp.com/v3/businesses/{id}/reviews'

headers = {
        'Authorization': 'Bearer {}'.format(api_key),
    }

client_id = '2TNko8fRlzRwhqkvrJTE1A'
api_key = 'WRaElnmVvKVyeugVhRae2QOHQWJFhUyoKuqpXHbE5uZDHKgA32CaYDcjqHwVOifJr57QPLjqIkT8fY2M9K6H2yEzUFJS7nClpT2tlSukjYTGzA5_-SeJVPlnk3PzX3Yx'

response = requests.get(url, headers=headers, params=url_params)

url_params = {
                "term": term.replace(' ', '+'),
                "location": location.replace(' ', '+'),
                "categories" : categories,
                "radius": radius,
                "limit": 50,
            }

def yelp_call(url, url_params, api_key):
    response = requests.get(url, headers=headers, params=url_params)
    data = response.json()
    return data

def parse_results(results):
    
    parsed_results = []
    count = 0
    
    for business in results['businesses']:
        for item in ['businessid', 'rating', 'price', 'name', 'review_count', 'address', 'city', 'metro_area', 'zip_code']:
            if item not in business:
                business[item] = np.nan
            else:
                business[item]
    
        biz_tuple = (business['id'],
                business['rating'],
                business['price'],
                business['name'],
                business['review_count'],
                business['location']['display_address'][0],
                business['location']['city'],
                location,
                business['location']['zip_code']
                    )
        count += 1
        parsed_results.append(biz_tuple)
    
    return parsed_results

def db_insert(conn, cursor, parse_results):
    add_business = ("""
    INSERT INTO businesses (businessid, rating, price, name, review_count, address, city, metro_area, zip_code) 
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
    """)
    cursor.executemany(add_business, parse_results)
    conn.commit()