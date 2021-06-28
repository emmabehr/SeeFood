import requests
import json

def getCredentials():
    configuration = {"api_key": "", "api_app": ""}
    #read from file
    try:
        config_file = open("edamam.conf")
        configuration = json.load(config_file)
        print(configuration)
    except:
        print("Failed to read configuration")

    return configuration

def searchByIngredient(ingredient):
    configuration = getCredentials()
    if configuration['api_app'] == "" or configuration['api_key'] == "":
        return {}

    try:
        query = f"https://api.edamam.com/api/recipes/v2?type=public&q={ingredient}&app_id={configuration['api_app']}&app_key={configuration['api_key']}"
        search_results = requests.get(query)
        info = search_results.json()
        return info['hits']
    except:
        return {'error': True}