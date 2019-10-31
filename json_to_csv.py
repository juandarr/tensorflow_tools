import os
import glob
import pandas as pd
import json
from PIL import Image 

'''
Path is defined as an argument here
'''
def json_to_csv(path):
    json_list = []
    for json_file in glob.glob(path + '/*.json'):
        with open(json_file, 'r') as f:
            datastore = json.load(f)
            print('Here is the Json file: ', json_file)
            filename = json_file.split('/')[-1].split('.')[0]
            print('And this is the filename: ', filename)
            filename += '.jpg'
            im = Image.open(filename)
            width, height = im.size
            for data in datastore:
                value = (filename,
                        width,
                        height,
                        data['name'],
                        data['pos']['x'],
                        data['pos']['y'],
                        data['pos']['x']+data['pos']['w'],
                        data['pos']['y']+data['pos']['h']
                        )
                json_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(json_list, columns=column_name)
    return xml_df

def main():
    image_path = os.path.join(os.getcwd(), 'annotations')
    xml_df = json_to_csv(image_path)
    xml_df.to_csv('raccoon_labels.csv', index=None)
    print('Successfully converted json to csv.')

main()