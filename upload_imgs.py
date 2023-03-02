import requests
import os
import pandas


url = 'https://seasonturk.com/api/method/tourism_backend.upload_data.upload_data'
imgs_folder = 'imgs'
csv_data_file = "data.csv"

data_file = pandas.read_csv(csv_data_file)

for value in data_file.values:
    data = {
        "city": value[0],
        "type": value[1],
        "name": value[2],
        "rate": value[3],
        "likes": value[4],
        "location": value[5]   
    }
    imgs_path = os.path.join(imgs_folder, data['name'])
    files = {}
    for image in os.listdir(imgs_path):
        with open(os.path.join(imgs_path, image), 'rb') as f:
            files[image] = f.read()
            
    res = requests.post(url, files=files, data=data)
    print(res.content)