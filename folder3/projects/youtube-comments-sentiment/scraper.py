import requests
import os
from dotenv import load_dotenv
load_dotenv()
def fetch_comments():
    API_KEY=os.getenv("YOUTUBE_API_KEY")
    VIDEO_ID="dvUPDxfrEHM"
    url=" https://www.googleapis.com/youtube/v3/commentThreads"
    comments=[]
    next_page_token=None
    while True:
        params={
            "part":"snippet",
            "videoId": VIDEO_ID,
            "maxResults":100,
            "key":API_KEY,
            "pageToken":next_page_token
            }
        response=requests.get(url,params=params)
        data=response.json()

        for item in data["items"]:
            comment=item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        next_page_token=data.get("nextPageToken")
        if not next_page_token:
            break
        

    print(f"Fetched {len(comments)} comments")
    print(comments[:2])
    return comments


   















# import requests
# from database import create_database,create_table,get_connection,insert_comments
# API_KEY="AIzaSyBAdAdOZ1B2rQOKPV6hO0XarqY844W6gRQ"
# VIDEO_ID="dvUPDxfrEHM"
# url=" https://www.googleapis.com/youtube/v3/commentThreads"


# params={
#     "part":"snippet",
#     "videoId": VIDEO_ID,
#     "maxResults":50,
#     "key":API_KEY
#     }
# response=requests.get(url,params=params)
# data=response.json()

# comments=[]
# for item in data["items"]:
#     comment=item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
#     comments.append(comment)
# print(f"Fetched {len(comments)} comments")
# print(comments[:5])

# # Database creation and insertion:
# create_database()
# create_table()
# print("Inserting into database:")
# insert_comments(comments)
