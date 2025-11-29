import os
import json

# Configuration
IMAGE_DIRECTORY = "pictures"
OUTPUT_FILE = "data.json"

# A curated list of 24 Christmas Songs with real Spotify Track URLs
CHRISTMAS_SONGS = [
    {"name": "All I Want for Christmas Is You - Mariah Carey", "url": "https://open.spotify.com/track/0bYg9bo50gSsH3LtXe2SQn"},
    {"name": "Last Christmas - Wham!", "url": "https://open.spotify.com/track/2FRnf9qhLbvw8fu4IBXx78"},
    {"name": "Rockin' Around The Christmas Tree - Brenda Lee", "url": "https://open.spotify.com/track/2EjXfH91m7f8HiJN1yCwDY"},
    {"name": "Jingle Bell Rock - Bobby Helms", "url": "https://open.spotify.com/track/7vQbuQcyTflfCIOu3Uzzya"},
    {"name": "Santa Tell Me - Ariana Grande", "url": "https://open.spotify.com/track/0lizgQ7Qw35od7CYaoMBZb"},
    {"name": "It's Beginning to Look a Lot Like Christmas - Michael Bublé", "url": "https://open.spotify.com/track/5a1iz510svNAKiFXztvPft"},
    {"name": "Underneath the Tree - Kelly Clarkson", "url": "https://open.spotify.com/track/3nAp4IvdMPP96kHP95fkZh"},
    {"name": "Let It Snow! Let It Snow! Let It Snow! - Dean Martin", "url": "https://open.spotify.com/track/2uFaJJtFpPDc5Pa95XzTvg"},
    {"name": "Feliz Navidad - José Feliciano", "url": "https://open.spotify.com/track/7taXf5qdUmTEHsLkaYZDNY"},
    {"name": "Sleigh Ride - The Ronettes", "url": "https://open.spotify.com/track/5ASM6Qjiav2xPe7gRkQMsY"},
    {"name": "Holly Jolly Christmas - Michael Bublé", "url": "https://open.spotify.com/track/5PuKlCjfEVIXl0ZKp5wlxM"},
    {"name": "Happy Xmas (War Is Over) - John Lennon", "url": "https://open.spotify.com/track/27RYrbL6S02LNVhDWVl38b"},
    {"name": "Wonderful Christmastime - Paul McCartney", "url": "https://open.spotify.com/track/1svsk9cFBLP5pT2W276t6t"},
    {"name": "Driving Home for Christmas - Chris Rea", "url": "https://open.spotify.com/track/3Z3QhZAZpqwZa1phsbQ3JZ"},
    {"name": "Blue Christmas - Elvis Presley", "url": "https://open.spotify.com/track/3QiAAp20rPCqKKAtMNjaUY"},
    {"name": "White Christmas - Bing Crosby", "url": "https://open.spotify.com/track/4so0Wek9TpJEu5DFuOcsED"},
    {"name": "Santa Claus Is Coming To Town - The Jackson 5", "url": "https://open.spotify.com/track/2QHN1LuWn86U8Xv6XfLZQ3"},
    {"name": "Do They Know It's Christmas? - Band Aid", "url": "https://open.spotify.com/track/0247StOpd3AkeYZW52e796"},
    {"name": "Mistletoe - Justin Bieber", "url": "https://open.spotify.com/track/7xapw9Oy21WpfEcib2ErSA"},
    {"name": "Have Yourself A Merry Little Christmas - Frank Sinatra", "url": "https://open.spotify.com/track/2a1o6ZejUi8U3wzzDtCOpH"},
    {"name": "Fairytale of New York - The Pogues", "url": "https://open.spotify.com/track/3VTNVsTTu05dmTsVFrmGpK"},
    {"name": "Baby, It's Cold Outside - Dean Martin", "url": "https://open.spotify.com/track/2smO234c9cQO6h23Qh925d"},
    {"name": "Winter Wonderland - Bing Crosby", "url": "https://open.spotify.com/track/6Kq7rNbsqJ26d2zG9iL33i"},
    {"name": "Silent Night - Michael Bublé", "url": "https://open.spotify.com/track/000x2qE0Bm35UUL6AjbbQK"}
]

def generate_json():
    # 1. Get all files from directory
    if not os.path.exists(IMAGE_DIRECTORY):
        print(f"Error: Directory '{IMAGE_DIRECTORY}' not found.")
        return

    files = [f for f in os.listdir(IMAGE_DIRECTORY) if f.lower().endswith(".jpg")]
    
    # Sort files naturally (so 1.jpg comes before 2.jpg)
    # If your files are dates (2023-12-01), standard sort works fine.
    files.sort()

    output_data = []

    # 2. Loop through files and songs simultaneously
    # zip ensures we don't crash if there are more files than songs or vice versa
    for filename, song in zip(files, CHRISTMAS_SONGS):
        
        # Remove extension for the info field
        info_string = os.path.splitext(filename)[0]
        
        # Create the dictionary object
        entry = {
            "picture_path": os.path.join(IMAGE_DIRECTORY, filename),
            "picture_info": info_string,
            "song_url": song["url"],
            "song_name": song["name"],
            "puzzle": "",
            "puzzle_solution": "",
            "puzzle_hints": []
        }
        
        output_data.append(entry)

    # 3. Save to data.json
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)

    print(f"Success! Generated {OUTPUT_FILE} with {len(output_data)} entries.")

if __name__ == "__main__":
    generate_json()