import requests
import pandas
import os
import json

painting_data = pandas.read_csv('fitlered_paintings.csv')

for index, row in painting_data.iterrows():

    # TODO: remove this part when we want to run all of them
    if index > 20:
        break

    img_url = row['img_url']
    file_name = './retrieved_paintings/' + img_url.split('/')[-1]

    response = requests.get(img_url, stream=True)

    if not response.ok:
        print('removed:', file_name, response)
        continue

    with open(file_name, 'wb') as opened_file:
        for block in response.iter_content(1024):
            if not block:
                break
            opened_file.write(block)

images = os.listdir('./retrieved_paintings')

# check size of all images
print('Checking size of all images...')
for image in images:
    file_size = os.path.getsize('./retrieved_paintings/' + image)
    assert(file_size > 0)
print('All images are valid.')

json_stuff = []
for index, row in painting_data.iterrows():
    # ,img_url,painting_artist,painting_name
    img_url = row['img_url']

    path = '/paintings/' + img_url.split('/')[-1]
    path = path.replace('jpg', 'webp')
    artist = row['painting_artist']
    name = row['painting_name']

    json_stuff.append({
        'artist': artist,
        'name': name,
        'path': path
    })

# write to JSON file
json_dumb = {'paintings': json_stuff}
with open('ignore.json', 'w') as outfile:
    json.dump(json_dumb, outfile)
