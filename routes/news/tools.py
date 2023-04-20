import pyimgur
import json
import os
im = pyimgur.Imgur('e89683761351f10')


def read_news(title_url):
    file_db_json = json.load(open(DIR_DB_JSON))
    return file_db_json['news'][title_url]   
    
dirname = os.path.dirname(os.path.abspath(__file__))

DIR_DB_JSON = os.path.join(dirname+'/db','news.json')

def upload_imgurl(path,title):
    uploaded_image = im.upload_image(path, title=title)
    print(uploaded_image)
    return uploaded_image

def save_news_(notice_db):
    print(notice_db)
    news_json = notice_db
    file_db_json = json.load(open(DIR_DB_JSON))
    file_db_json['news'][news_json['title_url']]=(news_json)
    with open(DIR_DB_JSON,'w') as file_json:
        file_json.write(json.dumps(file_db_json,indent=4))
    return notice_db['title_url']