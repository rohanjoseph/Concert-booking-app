import csv

def get_most_popular_video_data(data):
    
    with open('popular.csv','w',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(data.keys())
        w.writerows(zip(*data.values()))
        
    print("print data in most popular data")
    
def get_video_result_output(data):
    
    with open('data.csv','w',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(data.keys())
        w.writerows(zip(*data.values()))
    print("print data in get_data_output")

def get_category_list_output(data):
    
    with open('category.csv','w',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(data.keys())
        w.writerows(zip(*data.values()))
    print("print data in get_category_data_output")
    
def get_event_list_output(data):
    
    with open('event.csv','w',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(data.keys())
        w.writerows(zip(*data.values()))
    print("print data in get_category_data_output")