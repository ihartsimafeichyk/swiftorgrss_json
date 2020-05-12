import xmltodict
import requests

from cachetools import cached, TTLCache

"""
Base URL for fetching data.
"""
base_url = 'https://swift.org/atom.xml';


@cached(cache=TTLCache(maxsize=1024, ttl=3600))
def get_data():
    """
    Retrieves the data.
    """
    data = requests.get(base_url)
    feed = xmltodict.parse(data.content)

    return feed
