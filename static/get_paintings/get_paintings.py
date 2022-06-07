import pandas
import json

paintings_data = pandas.read_csv('tate-modified.csv')

# get the list of mediums from txt file
desired_mediums = []
with open('mediums.txt', 'r') as f:
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
fitlered_paintings = pandas.DataFrame()

urls = []
artists = []
names = []

# go through each row of CSV
for index, row in paintings_data.iterrows():
    img_url = row['data.thumbnail']
    artist = row['artist.name']
    name = row['data.title']

    if img_url is None:
        print ('no image')
    # print(artist)

    urls.append(img_url)
    artists.append(artist)
    names.append(name)
    # painting = {
    #     'img_url': img_url,
    #     'artist': artist,
    #     'name': name
    # }

print(len(urls))
print(len(artists))
print(len(names))

fitlered_paintings['img_url'] = urls
fitlered_paintings['painting_artist'] = artists
fitlered_paintings['painting_name'] = names

print(fitlered_paintings.head())

# write to CSV file
fitlered_paintings.to_csv('fitlered_paintings.csv')

print('CSV file written: filtered_paintings.csv')
