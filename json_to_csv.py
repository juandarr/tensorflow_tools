import os
import glob
import pandas as pd
import json

'''
Path is defined as an argument here
'''
def json_to_csv():
    json_list = []
    for json_file in glob.glob('*.json'):
        with open(json_file, 'r') as f:
            datastore = json.load(f)
        
            for data in datastore:
                value = ('filename',
                        data['pos']['w'],
                        data['pos']['h'],
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
    xml_df = json_to_csv()
    xml_df.to_csv('raccoon_labels.csv', index=None)
    print('Successfully converted xml to csv.')

main()