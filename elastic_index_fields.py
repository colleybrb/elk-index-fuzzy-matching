import pandas as pd
import json
import os

def file_to_json(file,path):
    path = path +"\\"+ file
    print(path)
    with open(path) as f:
        print(f)
        json_data = json.load(f)
        temp_dict=(json_data["fields"])
        temp_list=temp_dict.keys()
        if file.endswith('.txt'):
            file = file[:-4]
        df=pd.DataFrame(columns=['file','field'])
        df.at[0,'file'] = file
        df.at[0,'field'] = temp_list
        #data = {'file': file, 'fields': temp_list}
    
        #df=pd.DataFrame.from_dict(data)
        return(df)


path = r"C:\Users\user\Downloads\indices"
dir_list = os.listdir(path)
df1 = pd.DataFrame()
for file in dir_list:
    df=file_to_json(file, path)
    df1 = pd.concat([df1, df], ignore_index=True)
print(df1)
df1.to_csv(r"C:\Users\user\Downloads\fields2.csv", index=False, header=True)
    