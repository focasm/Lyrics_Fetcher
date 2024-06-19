# Lyrics Fetcher

This script fetches and displays song lyrics for a given artist using the Genius API. It includes functionalities such as retrying requests with exponential backoff, cleaning up the fetched lyrics, and typing out the lyrics character by character for a dynamic display.

## Features

- **Type-out Message:** Displays messages character by character with a delay for a typewriter effect.
- **Retry with Exponential Backoff:** Retries failed HTTP requests using exponential backoff to handle temporary issues.
- **Clean Lyrics:** Processes and cleans the fetched lyrics to remove unwanted characters and lines.
- **Fetch and Display Lyrics:** Fetches the lyrics of songs by an artist and displays them dynamically.

## Requirements

- Python 3.x
- `requests` library
- `lyricsgenius` library

## Installation

1. Install the required libraries:
    ```bash
    pip install requests lyricsgenius
    ```

2. Get your Genius API token from [Genius API](https://genius.com/api-clients).

## Usage

1. Replace the placeholder `token` with your actual Genius API token in the script.

    ```python
    token = "your_genius_api_token_here"
    ```

2. Run the script:
    ```bash
    python lyrics_fetcher.py
    ```

3. Enter the name of the artist and the maximum number of songs to fetch when prompted.

## Script Overview

### Importing Libraries


The `main` function initializes the Genius API client and prompts the user for the artist's name and the number of songs to fetch, then calls the `fetch_and_display_lyrics` function to fetch and display the lyrics.

## Error Handling

The script includes error handling for network issues and invalid user inputs, providing appropriate messages to guide the user.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Replace the placeholder `token` with your actual Genius API token before running the script. The script fetches the lyrics of songs by the specified artist and displays them dynamically, making it a fun and interactive way to read lyrics.