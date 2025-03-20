import pprint
import requests
import json

def gatorme():
    f = open('database.json')
    # returns JSON object as
    # a dictionary
    file_content = json.load(f)
    baseURL = 'https://api.giphy.com/v1/gifs/random?'
    apiKey = "api_key=" +  file_content['gif_api_key']
    tag = '&tag='
    subj = 'alligator'
    requestURL = baseURL + apiKey + tag + subj
    responses = requests.get(requestURL).json()
    # pprint.pprint(responses)
    random_url_gif =   responses['data']['images']['downsized_large']['url']

    return random_url_gif

def goon():
    f = open('database.json')
    # returns JSON object as
    # a dictionary
    file_content = json.load(f)
    baseURL = 'https://api.giphy.com/v1/gifs/random?'
    apiKey = "api_key=" +  file_content['gif_api_key']
    tag = '&tag='
    subj = 'Arsenal'
    requestURL = baseURL + apiKey + tag + subj
    responses = requests.get(requestURL).json()
    # pprint.pprint(responses)
    random_url_gif =   responses['data']['images']['downsized_large']['url']

    return random_url_gif

def crocme():
    f = open('database.json')
    # returns JSON object as
    # a dictionary
    file_content = json.load(f)
    baseURL = 'https://api.giphy.com/v1/gifs/random?'
    apiKey = "api_key=" +  file_content['gif_api_key']
    tag = '&tag='
    subj = 'crocs shoes'
    requestURL = baseURL + apiKey + tag + subj
    responses = requests.get(requestURL).json()
    # pprint.pprint(responses)
    random_url_gif =   responses['data']['images']['downsized_large']['url']

    return random_url_gif

def skol():
    f = open('database.json')
    # returns JSON object as
    # a dictionary
    file_content = json.load(f)
    baseURL = 'https://api.giphy.com/v1/gifs/random?'
    apiKey = "api_key=" +  file_content['gif_api_key']
    tag = '&tag='
    subj = 'Aaron Rodgers'
    requestURL = baseURL + apiKey + tag + subj
    responses = requests.get(requestURL).json()
    # pprint.pprint(responses)
    random_url_gif =   responses['data']['images']['downsized_large']['url']

    return random_url_gif

def yakuza():
    f = open('database.json')
    # returns JSON object as
    # a dictionary
    file_content = json.load(f)
    baseURL = 'https://api.giphy.com/v1/gifs/random?'
    apiKey = "api_key=" +  file_content['gif_api_key']
    tag = '&tag='
    subj = 'like a dragon'
    requestURL = baseURL + apiKey + tag + subj
    responses = requests.get(requestURL).json()
    # pprint.pprint(responses)
    random_url_gif =   responses['data']['images']['downsized_large']['url']

    return random_url_gif
