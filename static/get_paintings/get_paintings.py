import pandas
import json

paintings_data = pandas.read_csv('get_paintings/tate-modified.csv')

# get the list of mediums from txt file
desired_mediums = []
with open('get_paintings/mediums.txt', 'r') as f:
    for line in f:
        desired_mediums.append(line.strip())

mediums = paintings_data['data.medium'].unique()
print(len(mediums))

# filter by dimension
paintings_data = paintings_data[paintings_data['dimensions.depth'] == 0.0]

mediums = paintings_data['data.medium'].unique()
print(len(mediums))

# for m in mediums:
#     print(m)

def filterFunc(x: str):
    return x.strip() in desired_mediums

# filter by medium
paintings_data = paintings_data[paintings_data['data.medium'].apply(filterFunc)]

mediums = paintings_data['data.medium'].unique()
print(len(mediums))

print(paintings_data.head())

# make new DataFrame
fitlered_paintings = pandas.DataFrame(columns=['painting_name', 'painting_title', 'img_url'])

urls = []
artists = []
names = []

# go through each row of CSV
for index, row in paintings_data.iterrows():
    img_url = row['data.thumbnail']
    artist = row['artist.name']
    name = row['data.title']

    urls.append(img_url)
    artists.append(artist)
    names.append(name)
    # painting = {
    #     'img_url': img_url,
    #     'artist': artist,
    #     'name': name
    # }

fitlered_paintings['img_url'] = urls
fitlered_paintings['painting_artist'] = artists
fitlered_paintings['painting_name'] = names

print(fitlered_paintings.head())

# write to CSV file
fitlered_paintings.to_csv('get_paintings/fitlered_paintings.csv')
