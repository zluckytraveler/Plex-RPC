# INSTALL

When the script runs for the first time, you need to follow the prompts for connecting your Plex account, and a `config.json` file will automatically be created.

## LOCAL

***The script must be running on the same server as your Discord client.***

### PREREQUISITES
- Python 3.10
-  Pip
   
### Mac & Linux
1. `cd <path to directory>`
2. `python3 -m pip install -U -r requirements.txt`
3. `python3 bot.py`

### Windows
1. `cd <path to directory>`
2. `py -m pip install -U -r requirements.txt`
3. `py bot.py`

<br />

## DOCKER

***Both containers must be running on the same server.***

1. Run Discord Docker
2. Go to https://YOUR-IP:6901
3. User = `kasm_user`
4. Password = Set in Run Command
5. Login to your Discord Account
6. Run Plex-RPC Docker
7. Check output for URL to connect Plex account
8. Add extra settings to `config.json` and restart Plex-RPC container (Optional)

<br />

Replace with your own information. 
- `/PATH/TO/`
- `PASSWORD`
- `YOURSERVER`

<br />

**Docker Discord**
```
docker run -d \
  --name Discord \
  --restart unless-stopped \
  --shm-size=512m \
  -p 6901:6901 \
  -e VNC_PW=PASSWORD \
  -v /PATH/TO/Plex-RPC/unix-socket:/tmp \
  kasmweb/discord:1.14.0
```

**Plex-RPC**
```
docker run -d \
  --name Plex-RPC \
  --restart unless-stopped \
  -e PLEX_SERVER_NAME=YOURSERVER \
  -v /PATH/TO/Plex-RPC/data:/app/data \
  -v /PATH/TO/Plex-RPC/unix-socket:/run/app:ro \
  zluckytraveler/plex-rpc
```
<br />

# CONFIG SETTINGS

| DATA | TYPE | OPTION | DESCRIPTION |
| --- | --- | --- | --- |
|`logging`| list | | |
|`debug`| boolean | true/false | Extra logging information |
|`writeToFile`| boolean | true/false | Writes everything ouputted to a console.log |
|`display`| list | | |
|`hideTotalTime`| boolean | true/false | Hides the total duration of the media |
|`useRemainingTime`| boolean | true/false | Displays your remaining time instead of elapsed time |
|`posters`| list | | |
|`enabled`| boolean | true/false | Allows media posters instead logo image |
|`imgurClientID`| integer |optional | Client ID from Imgur needed for media posters |
|`buttons`| list | optional | |
|`label`| string | optional | The label that shows for the button | 
|`url`| string | optional | Any url the button directs to or for dynamic butttons |
|`users`| list | | |
|`token`| string | |Access token associated with your Plex account |
|`servers`| list | |
|`name`| string | | Name of the Plex Media Server |
|`listenForUser`| string |optional | Finds a specific account, shared or managed user |
|`blacklistedLibraries`| list | optional | Ignores a session for specific libraries |
|`whitelistedLibraries`| list | optional | Finds a session for specific libraries |

<br />

## Obtaining Imgur Client ID (Optional)

1. Go to Imgur's application registration page (<https://api.imgur.com/oauth2/addclient>)
2. Enter a name for the application and select "OAuth2 without a callback URL", and enter you email address.
3. Submit the form to obtain your application's client ID


## Dynamic Button URL (Optional)

When streaming media a direct link will be provided to the media info for either IMDb or TMDB by using dynamic URL placeholders.

- IMDb: `dynamic:imdb`
-  TMDB: `dynamic:tmdb`

*A Discord bug makes the buttons unresponsive for your own account, but other users are able to use them without issue.*

<br />

# CONFIG EXAMPLE

```json
{
  "logging": {
    "debug": true,
    "writeToFile:": false
  },
  "display": {
    "hideTotalTime": false,
    "useRemainingTime": false,
    "posters": {
      "enabled": true,
      "imgurClientID": "1234567890"
  },
  "buttons": [
  { "label": "IMDb",
    "url": "dynamic:imdb"
    },
    {
    "label": "YOUR BUTTON LABEL",
    "url": "https://www.YourURLHere.com"
    }
    ]
  },
  "users": [
  { "token": "PLEX TOKEN",
    "servers": [
    { "name": "PLEX SERVER NAME"
      },
      {
      "name": "YOUR USERNAME",
      "listenForUser": "MANAGED/SHARED USERNAME",
      "whitelistedLibraries": ["Movies"],
      "blacklistedLibraries": ["TV Shows"]
      }
      ]
    }
  ]
}
```
