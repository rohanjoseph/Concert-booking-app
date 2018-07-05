
from catalyst_data_output import get_video_result_output

def get_video_search_results(client,q,regionCode):
    '''General search request for the videos are made in this function'''

    data_request = client.search().list(q=q,maxResults=50,type='video',videoLicense='youtube',videoType='any',order='relevance',part="id,snippet",regionCode=regionCode).execute()
    
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
         response = client.videos().list(part='statistics, snippet',id=data_result['id']['videoId']).execute()    
         channelId.append(response['items'][0]['snippet']['channelId'])
         channelTitle.append(response['items'][0]['snippet']['channelTitle'])
         categoryId.append(response['items'][0]['snippet']['categoryId'])
         viewCount.append(response['items'][0]['statistics']['viewCount'])
         likeCount.append(response['items'][0]['statistics']['likeCount'])
         dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])
         try:
             tags.append(response['items'][0]['snippet']['tags'])
         except:
             print("tags getting appended")
    
    else:
        print("in the else block")
        
    data_dict = {'videos': videos,'channelId': channelId,'channelTitle': channelTitle,'categoryId': categoryId,'channelTitle': channelTitle,'viewCount': viewCount,'likeCount': likeCount,'dislikeCount': dislikeCount,'tags': tags}
    print(data_dict)
    
    '''The dictonary output is converted into the csv file in the below function'''
    get_video_result_output(data_dict)
