import time
from lyricsgenius import Genius
import requests

def type_out_message(message, delay=0.1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def retry_with_exponential_backoff(func, max_retries=5, initial_delay=1, backoff_factor=2):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            return func()
        except (requests.exceptions.Timeout, requests.exceptions.HTTPError) as e:
            if attempt == max_retries - 1:
                raise e
            print(f"Error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= backoff_factor

def clean_lyrics(lyrics, title):
    lines = lyrics.split('\n')
    start_idx = next((idx for idx, line in enumerate(lines) if title.lower() in line.lower()), 0)
    cleaned_lines = [line for line in lines[start_idx:] if not line.startswith('[') and line.strip()]
    return '\n'.join(cleaned_lines)

def fetch_and_display_lyrics(genius, artist_name, max_songs):
    try:
        artist = retry_with_exponential_backoff(lambda: genius.search_artist(artist_name, max_songs=max_songs))
        if not artist:
            print(f"No songs found for {artist_name}.")
            return

        print(f"Found {len(artist.songs)} songs by {artist.name}:")
        for idx, song in enumerate(artist.songs):
            print(f"{idx + 1}. {song.title}")

        song_choice = int(input("Enter the number of the song you want the lyrics for: ")) - 1
        if song_choice < 0 or song_choice >= len(artist.songs):
            print("Invalid choice.")
            return

        song = artist.songs[song_choice]
        print(f"Fetching lyrics for '{song.title}'...")
        lyrics = retry_with_exponential_backoff(lambda: song.lyrics)
        cleaned_lyrics = clean_lyrics(lyrics, song.title)

        message = f"\nHere are the lyrics for '{song.title}':\n\n{cleaned_lyrics}"
        type_out_message(message)
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"An error occurred: {e}")

def main():
    # Get your Genius API token
    token = "***********************************************"  # Replace with your actual token
    genius = Genius(token)

    artist_name = input("Enter the name of the artist: ").strip()
    max_songs = int(input("Enter the maximum number of songs to fetch: ").strip())
    fetch_and_display_lyrics(genius, artist_name, max_songs)

if __name__ == "__main__":
    main()
