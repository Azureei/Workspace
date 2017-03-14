import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tdjango.settings')
import django
django.setup()

import json
import urllib
import urllib2

def read_webhose_key():

        webhose_api_key = None

        try:
                with open('search.key', 'r') as f:
                        webhose_api_key = f.readline().strip()
        except:
                raise IOError('search.key file not found')

        return webhose_api_key

def run_query(search_terms, size=10):
        """
        Given a string containing search terms (query), and a number of results to return (default of 10),
        returns a list of results from the Webhose API, with each result consisting of a title, link and summary.
        """
        webhose_api_key = read_webhose_key()

        if not webhose_api_key:
                raise KeyError('Webhose key not found')


        # What's the base URL for the Webhose API?
        root_url = 'http://webhose.io/search'
        
        # Format the query string - escape special characters.
        query_string = urllib.quote(search_terms)
        
        # Use string formatting to construct the complete API URL.
        search_url = '{root_url}?token={key}&format=json&q={query}&sort=relevancy&size={size}'.format(
                                        root_url=root_url,
                                        key=webhose_api_key,
                                        query=query_string,
                                        size=size)
        
        results = []

        try:
                # Connect to the Webhose API, and convert the response to a Python dictionary.
                print(search_url)
                response = urllib2.urlopen(search_url).read()
                print(response)
                json_response = json.loads(response)
                
                # Loop through the posts, appendng each to the results list as a dictionary.
                for post in json_response['posts']:
                        print(post['title'])
                        results.append({'title': post['title'],
                                                        'link': post['url'],
                                                        'summary': post['text'][:200]})
        except Exception as e: 
                print(e)
                print("Error when querying the Webhose API")
        
        # Return the list of results to the calling function.
        return results


if __name__ == '__main__':
    print("Starting Rango Webhose search script...")
    read_webhose_key()
    query = raw_input()
    run_query(query, size=10)
