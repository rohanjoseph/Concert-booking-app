

import eventful
from catalyst_data_output import get_event_list_output
from catalyst_auth import EVENTFUL_API_KEY

def get_events(query,location):
  
    id = []
    url = []
    title = []
    start_time = []
    stop_time = []
    venue_id = []
    venue_name = []
    city_name = []
    region_name = []
    country_name = []
    latitude = []
    longitude = []
    geocode_type = []
    api = eventful.API(EVENTFUL_API_KEY,'api.eventful.com')
    event = api.call('/events/search', q=query, l=location)
    print(event)
    for e in event['events']['event']:
        id.append(e['id'])
        url.append(e['url'])
        title.append(e['title'])  
        start_time.append(e['start_time'])
        stop_time.append(e['stop_time'])
        venue_id.append(e['venue_id'])
        venue_name.append(e['venue_name'])
        city_name.append(e['city_name'])
        region_name.append(e['region_name'])
        country_name.append(e['country_name'])
        latitude.append(e['latitude'])
        longitude.append(e['longitude'])
        geocode_type.append(e['geocode_type'])
        #print ("%s at %s" % (event['title'], event['venue_name']))
        #print ("%s" % (e['country_name']))
    event_dict={'id': id,'url': url,'title': title,'start_time': start_time,'stop_time': stop_time,'venue_id': venue_id,'venue_name': venue_name,'city_name': city_name,'region_name': region_name,'country_name': country_name,'latitude': latitude,'longitude': longitude,'geocode_type': geocode_type}
    
    get_event_list_output(event_dict)