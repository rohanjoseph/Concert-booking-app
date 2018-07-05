from catalyst_data_search import get_video_search_results
from catalyst_auth import get_authenticated_youtube
from catalyst_category_search import get_category_id_list
from catalyst_category_search import get_trending_video_list
from catalyst_get_events import get_events




                
    
client = get_authenticated_youtube()
def main():

    get_video_search_results(client,"rock jazz ed sheeran linkin music backstreet","US")
    
    get_category_id_list(client,"US")
    
    dictData = get_category_id_list(client,"US")
    get_trending_video_list(client,dictData,"US")
    get_events('justin timberlake','united states')
    
    

if __name__ == '__main__':
     main()
    