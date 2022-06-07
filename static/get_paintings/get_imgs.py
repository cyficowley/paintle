import requests
import pandas
import os

painting_data = pandas.read_csv('fitlered_paintings.csv')

for index, row in painting_data.iterrows():
    img_url = row['img_url']
    file_name = 'retrieved_paintings/' + img_url.split('/')[-1]

    with open(file_name, 'wb') as opened_file:
        response = requests.get(img_url, stream=True)

        if not response.ok:
            print('removed:', file_name, response)
            os.remove(file_name)
            continue

        for block in response.iter_content(1024):
            if not block:
                break
            opened_file.write(block)

# TODO: go through images in retrieved_paintings and remove those that have 0 size
