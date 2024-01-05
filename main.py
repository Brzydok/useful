from pytube import Search, YouTube

# Your search query
search_query = "Python programming tutorial"

# Create a Search object
search = Search(search_query)

# Print the search results
for video in search.results:
    print("Title:", video.title)
    print("URL:", video.watch_url)
    print("Duration:", video.duration)
    print("Views:", video.views)
    print("")

# Get the first video from the search results
first_video = search.results[0]

# Create a YouTube object using the video URL
yt = YouTube(first_video.watch_url)

try:
    yt.streams.filter(progressive=True, file_extension="mp4").first().download(output_path='<your output path here>',
                                                                               filename="downloaded_video.mp4")
except Exception as e:
    print(f"Error: {e}")

print('Task Completed!')