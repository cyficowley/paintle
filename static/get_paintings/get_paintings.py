import pandas
import json

paintings_data = pandas.read_csv('tate-modified.csv')

# get the list of mediums from txt file
desired_mediums = []
with open('mediums.txt', 'r') as f:
    for line in f:
        desired_mediums.append(line.strip())

mediums = paintings_data['data.medium'].unique()
# print(len(mediums))

# filter by dimension
paintings_data = paintings_data[paintings_data['dimensions.depth'] == 0.0]

mediums = paintings_data['data.medium'].unique()
# print(len(mediums))

# for m in mediums:
#     print(m)

def filterFunc(x: str):
    return x.strip() in desired_mediums

# filter by medium
paintings_data = paintings_data[paintings_data['data.medium'].apply(filterFunc)]

mediums = paintings_data['data.medium'].unique()
# print(len(mediums))

# print(paintings_data.head())

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

    if str(img_url) == 'nan' or name == '[no title]' or 'Untitled' in name or name == '[title not known]':
        print('skipped bc no URL or no title: ' + name)
        continue

    chars = [' ', ',', '-', '_', ':', '.', '(', ')']
    temp_name = name
    for char in chars:
        temp_name = temp_name.replace(char, '')

    if not temp_name.isalnum():
        print('skipped bc no alpha: __' + name + '__')
        continue

    artist_split = artist.split(', ')
    if len(artist_split) == 2:
        artist = artist_split[1] + ' ' + artist_split[0]
    elif len(artist_split) == 3:
        artist = artist_split[1] + ' ' + artist_split[0] + ' ' + artist_split[2]        

    urls.append(img_url)
    artists.append(artist)
    names.append(name)

fitlered_paintings['img_url'] = urls
fitlered_paintings['painting_artist'] = artists
fitlered_paintings['painting_name'] = names

print(fitlered_paintings.head())

# write to CSV file
fitlered_paintings.to_csv('fitlered_paintings.csv')

print('\nCSV file written: get_paintings/filtered_paintings.csv')
