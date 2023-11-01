import os
import sys

name = "Discord Rich Presence for Plex"
version = "2.3.4"

plexClientID = "discord-rich-presence-plex"
discordClientID = "973425439706079302"

dataFolderPath = "data"
configFilePath = os.path.join(dataFolderPath, "config.json")
cacheFilePath = os.path.join(dataFolderPath, "cache.json")
logFilePath = os.path.join(dataFolderPath, "console.log")

isUnix = sys.platform in ["linux", "darwin"]
processID = os.getpid()
