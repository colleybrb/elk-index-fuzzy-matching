from fuzzywuzzy import fuzz
import pandas as pd
from tqdm import tqdm
import ast
with open(r"C:\Users\user\Downloads\fields.txt") as f:
    fields = [line.rstrip('\n') for line in f]
confidence_list=[70,80,90]
field_df = pd.read_csv(r'C:\Users\user\Downloads\fields2.csv',skip_blank_lines=True)
    

for ratio in confidence_list:
    df1=pd.DataFrame()
    for index, row in tqdm(field_df.iterrows()):
        index=(row['file'])
        fields_available=(row['field'])
        fields_available = ast.literal_eval(fields_available)
        for field_available in fields_available:
            for field_inquery in fields:
                confidenceratio=fuzz.token_sort_ratio(field_available, field_inquery)
                if confidenceratio>ratio:
                    print(f"{index},{field_available},{field_inquery},{confidenceratio}")
                    data={'index':index,'field_in_index':field_available,'field_in_search':field_inquery,'confidence':confidenceratio}
                    df=pd.DataFrame.from_dict(data,orient='index')
                    df1 = pd.concat([df1, df], ignore_index=True,axis=1)
    df1.to_csv("C:\\Users\\user\\Downloads\\"+ str(ratio) +"score.csv", index=False, header=True)
    print(df1)
