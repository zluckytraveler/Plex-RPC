from store.constants import configFilePath
from utils.dict import merge
from utils.logging import logger
import json
import models.config
import os
import time

config: models.config.Config = {
	"logging": {
		"debug": True,
		"writeToFile": True,
	},
	"display": {
		"hideTotalTime": False,
		"useRemainingTime": False,
		"posters": {
			"enabled": False,
			"imgurClientID": "",
		},
		"buttons": [],
	},
	"users": [],
}

def loadConfig() -> None:
	if os.path.isfile(configFilePath):
		try:
			with open(configFilePath, "r", encoding = "UTF-8") as configFile:
				loadedConfig = json.load(configFile)
		except:
			os.rename(configFilePath, configFilePath.replace(".json", f"-{time.time():.0f}.json"))
			logger.exception("Failed to parse the application's config file. A new one will be created.")
		else:
			merge(loadedConfig, config)
	saveConfig()

def saveConfig() -> None:
	try:
		with open(configFilePath, "w", encoding = "UTF-8") as configFile:
			json.dump(config, configFile, indent = "\t")
			configFile.write("\n")
	except:
		logger.exception("Failed to write to the application's config file.")
