import requests
import pandas
import os

painting_data = pandas.read_csv('fitlered_paintings.csv')

for index, row in painting_data.iterrows():
    if index > 20:
        break
    img_url = row['img_url']
    file_name = './retrieved_paintings/' + img_url.split('/')[-1]

    response = requests.get(img_url, stream=True)

    if not response.ok:
        print('removed:', file_name, response)
        # os.remove(file_name)
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
