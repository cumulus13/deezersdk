# DeezerSDK

A package to search and download musics on [Deezer](https://www.deezer.com/en/), Download MP3 or FLAC from Deezer.com by Artist Name (cli).

## Installation

```bash
pip install deezersdk
```

## Usage as a CLI

```bash
usage: deez.py [-h] [-p DOWNLOAD_PATH] [-t TYPE] query

positional arguments:
  query                 Search For Artist

optional arguments:
  -h, --help            show this help message and exit
  -p DOWNLOAD_PATH, --download-path DOWNLOAD_PATH
                        Save download to
  -t TYPE, --type TYPE  mp3 or flac, default = mp3
```

## Usage as a package

#### Logging In

```python
from deezersdk import Deezer

arl = "edit_this"
deezer = Deezer(arl=arl)
user_info = deezer.user
# or
# deezer = Deezer()
# user_info = deezer.login_via_arl(arl)
```

You can get the your `arl` by manually logging into [Deezer](https://www.deezer.com/) using your browser and check the `cookies` and look for the value of `arl`.

#### Searching

```python
# Some login code here

# Search tracks
track_search_results = deezer.search_tracks("IM DOPE")
# Search albums
album_search_results = deezer.search_albums("DAMN", limit=10)
# Search artists
artist_search_results = deezer.search_artists("J. Cole", limit=5)
# Search playlists
playlist_search_results = deezer.search_playlists("top", index=2)
```

#### Getting Information and Downloading

```python
# Some login code here

# Some download stuffs
from deezersdk.constants import track_formats

download_dir = "~/Downloads/"

track_id = "547653622"
track = deezer.get_track(track_id)
# track is now a dict with a key of info, download, tags, and get_tag
# info and tags are dict
track_info = track["info"]
tags_separated_by_comma = track["tags"]
# download and get_tag are partial functions
track["download"](download_dir, quality=track_formats.MP3_320) # this will download the file, default file name is Filename.[mp3 or flac]
tags_separated_by_semicolon = track["get_tag"](separator="; ") # this will return a dictionary similar to track["tags"] but this will override the default separator

artist_id = "53859305"
artist = deezer.get_artist(artist_id)

album_id = "39949511"
album = deezer.get_album(album_id) # returns a dict containing data about the album

playlist_id = "1370794195"
playlist = deezer.get_playlist(playlist_id) # returns a dict containing data about the playlist
```

## TODO

- [ ] More CLI features, save used Arls for convenience.
- [ ] Multithreaded downloader (1 song / 1 thread)
- [ ] Binary file
- [ ] GUI

## Disclaimer

I will and should not be held responsible for the usage of this package.

Don't use this package illegaly and against Deezer's [Terms Of Use](https://www.deezer.com/legal/cgu).

This is licensed under [GNU GPL v3](https://choosealicense.com/licenses/gpl-3.0/#).
