from http.client import responses
from googleapiclient.discovery import build
import pprint
import csv

api_key = "your API key"
youtuber_id = "id of the youtuber you want data for"

youtube = build("youtube", "v3", developerKey=api_key)


def get_all_videos(channel_id):

    req1 = youtube.channels().list(part="contentDetails", id="UCPsZ_0SkFdi551iYTG04R2g").execute()
    playlist_id = req1["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    videos = []
    next_page_token = None

    while 1:
        req2 = (
            youtube.playlistItems()
            .list(playlistId=playlist_id, part="snippet", maxResults=50, pageToken=next_page_token)
            .execute()
        )
        videos += req2["items"]
        next_page_token = req2.get("nextPageToken")

        if next_page_token is None:
            break
    return videos[:60]


vids = get_all_videos(youtuber_id)

video_id = []
for video in vids:
    video_id.append(video["snippet"]["resourceId"]["videoId"])


def get_vid_det():
    details = []
    for n in range(0, len(video_id)):
        req3 = youtube.videos().list(id=f"{video_id[n]}", part="snippet,statistics").execute()
        temp = {
            "title": req3["items"][0]["snippet"]["title"],
            "views": req3["items"][0]["statistics"]["viewCount"],
            "likes": req3["items"][0]["statistics"]["likeCount"],
            "dislikes": req3["items"][0]["statistics"]["dislikeCount"],
            "thumbnails": req3["items"][0]["snippet"]["thumbnails"]["default"]["url"],
        }
        details.append(temp)
    return details


final = get_vid_det()

keys = final[0].keys()

a_file = open("path of the file to be referred")
dict_writer = csv.DictWriter(a_file, keys)
dict_writer.writeheader()
dict_writer.writerows(final)
a_file.close()
print("File Created")
