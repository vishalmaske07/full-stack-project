from googleapiclient.discovery import build

def youtube_search(api_key, query, max_results=10, page_token=None):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part="id,snippet",
        maxResults=max_results,
        q=query,
        order="date",
        type="video",
        pageToken=page_token
    )
    response = request.execute()

    return response

def main():
    api_key = "AIzaSyDeBofjc0FHdiZSVJh-ipdspwYudsLPbLE"
    query = "how to make tea"

    response = youtube_search(api_key, query)

    for item in response["items"]:
        print(f"Title: {item['snippet']['title']}, Published at: {item['snippet']['publishedAt']}")

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = youtube_search(api_key, query, page_token=page_token)
        for item in response["items"]:
            print(f"Title: {item['snippet']['title']}, Published at: {item['snippet']['publishedAt']}")

if __name__ == "__main__":
    main()