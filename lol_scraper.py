#! python3

import os
import requests


def download_image(_file_path, _image_url, _res):
    load_file = open(os.path.join(_file_path, os.path.basename(_image_url)), 'wb')
    for chunk in _res.iter_content(100000):
        load_file.write(chunk)
    load_file.close()


# The three URL types are splash, loading, and square. Below is the template for each
splash_url = 'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'
loading_url = 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/'
square_url = 'http://ddragon.leagueoflegends.com/cdn/6.6.1/img/champion/'

# Make the leagueoflegends directory for all the images
os.makedirs('leagueoflegends', exist_ok=True)

# Grab the API data and place it into the response object. Then grab its 'data' property and place it into champions
url = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?api_key=2bf25f2b-c0bd-4781-9a52-1cc9307bb0f3'
res = requests.get(url)
champions = res.json()['data']
for champion in champions:
    # The only thing we need is the champion's key. Also, reset the iterator to 0 on each run through.
    champ_key = champions[champion]['key']
    i = 0

    # This makes the subdirectory for the champion and the two subdirectories for splash and loading within
    os.makedirs('leagueoflegends/' + champ_key, exist_ok=True)
    os.makedirs('leagueoflegends/' + champ_key + '/splash', exist_ok=True)
    os.makedirs('leagueoflegends/' + champ_key + '/loading', exist_ok=True)

    # There's only one square art, so just grab it from here without any issues or loops needed
    curr_square = square_url + champ_key + '.png'
    res = requests.get(curr_square)
    file_path = 'leagueoflegends/' + champ_key
    download_image(file_path, curr_square, res)

    # Because we don't know how many splashes each champion has, we'll use a while loop to check for the request status
    res = requests.get(splash_url + champ_key + '_0.jpg')
    while res.status_code == 200:
        # Set j = to the iterator i
        j = str(i)

        # Using the iterator and the variables above, set the image paths from Riot's API
        curr_splash = splash_url + champ_key + '_' + j + '.jpg'
        curr_load = loading_url + champ_key + '_' + j + '.jpg'

        # Grab the response object for the curr_splash url and download the image
        res = requests.get(curr_splash)
        file_path = 'leagueoflegends/' + champ_key + '/splash/'
        download_image(file_path, curr_splash, res)

        # Grab the response object for the curr_load url and download the image
        res = requests.get(curr_load)
        file_path = 'leagueoflegends/' + champ_key + '/loading/'
        download_image(file_path, curr_load, res)

        # Increment i and set the url to the next integer, j. The while loop will check if it is valid
        i += 1
        j = str(i)
        curr_splash = splash_url + champ_key + '_' + j + '.jpg'
        res = requests.get(curr_splash)
    print("Done with " + champ_key)

print(champions)
print('Done.')
