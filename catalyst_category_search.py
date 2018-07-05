from catalyst_data_output import get_category_list_output
from catalyst_data_output import get_most_popular_video_data

def get_category_id_list(client,regionCode):
    """
    This Function helps in fetching the categories
    """
    categoryId_request = client.videoCategories().list(regionCode=regionCode,part="snippet").execute()
       
    categoryId = []
    title = []
    channelId = []
    for categoryId_result in categoryId_request.get('items',[]):
        if categoryId_result['kind'] == 'youtube#videoCategory':
            categoryId.append(categoryId_result['id'])
            title.append(categoryId_result['snippet']['title'])
            channelId.append(categoryId_result['snippet']['channelId'])
        else:
            print("in else")
        
    
        #print ('catgeoryId:\n', '\n'.join(catgeoryId), '\n')
        data_dict = {'catgeoryId':categoryId,'title':title,'channelId':channelId}
        
        get_category_list_output(data_dict)
        print("in the get category")
        print((categoryId))
        
    return categoryId
    
def get_most_popular_video_list(client,videoCategoryId,regionCode):
    '''This function is created for the most popular videos'''
    data_request = client.search().list(maxResults=1,type='video',videoLicense='youtube',videoType='any',order='relevance',part="id,snippet").execute()
    data_response = client.videos().list(videoCategoryId=videoCategoryId,regionCode=regionCode,part='statistics,snippet',chart='mostPopular').execute()         
    channelId = []
    channelTitle = []
    categoryId = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    categoryId = []
    tags = []
    videos = []
    for data_result in data_request.get('items',[]):
        if data_result['id']['kind'] == 'youtube#video':
         videos.append(data_result['id']['videoId'])
        channelId.append(data_response['items'][0]['snippet']['channelId'])
        channelTitle.append(data_response['items'][0]['snippet']['channelTitle'])
        categoryId.append(data_response['items'][0]['snippet']['categoryId'])
        viewCount.append(data_response['items'][0]['statistics']['viewCount'])
        likeCount.append(data_response['items'][0]['statistics']['likeCount'])
        dislikeCount.append(data_response['items'][0]['statistics']['dislikeCount'])
        try:
             tags.append(data_response['items'][0]['snippet']['tags'])
        except:
             print("tags getting appended")
    
    else:
        print("in the else block")
        
    data_dict = {'videos':videos,'channelId': channelId,'channelTitle': channelTitle,'categoryId':categoryId,'channelTitle':channelTitle,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'tags': tags}
    
    print(data_dict)
    
    '''The dictonary output is converted into the csv file in the below function'''
    
    get_most_popular_video_data(data_dict)
    
    
    
    print("in the most popular")
    
    return data_response



def get_trending_video_list(client,categoryId,regionCode):
        for category in categoryId:
            try:
                get_most_popular_video_list(client,category,regionCode)
                print("in the trending video")
            except:
                print("mostPopular chart not associated with the ChannelId")