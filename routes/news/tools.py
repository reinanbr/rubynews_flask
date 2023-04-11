import pyimgur
import json
import os
im = pyimgur.Imgur('e89683761351f10')


DIR_DB_JSON = '/db/notice_db.json'

def upload_imgurl(path,title):
    uploaded_image = im.upload_image(path, title=title)
    print(uploaded_image)
    return uploaded_image

def save_news(notice_db):
    print(notice_db)
    news_json = json.dumps(notice_db,indent=4)
    file_db_json = json.load(open(DIR_DB_JSON,'a'))
    file_db_json['notice_db'].append(news_json)
    with open(DIR_DB_JSON,'wb') as file_json:
        file_json.write(json.dumps(file_db_json))
    return notice_db['title_url']