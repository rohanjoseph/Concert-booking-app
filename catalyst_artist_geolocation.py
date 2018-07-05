
import json
from DjamBase import DjamBase 
from catalyst_auth import JAMBASE_API_KEY
def get_artist_list():
    
    #venueId = []
    
    api = DjamBase.API(JAMBASE_API_KEY)
    #dict_data = api.venue_search("ontario").status
    dict_data = json.loads((api.venue_search("ontario")))
    print(dict_data)    