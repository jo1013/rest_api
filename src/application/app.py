import os
import sys
import pandas as pd


from . import ENUM
sys.path.append(os.path.dirname(os.path.abspath( __file__ ))) #py용
import dir_path as PATH

class APP :
    
    def __init__(self, kind :str , year: int , doc :str):
        self.kind = kind
        self.year = year
        self.doc = doc
        
    def main(kind :str , year : int, doc :str):
        
        csv_path = PATH.path.data_dir + '/12_19_교통사고정보.csv'
        df = pd.read_csv(csv_path, encoding='utf-8')
        trans = list(ENUM.transform)


        kind_list = df['대상사고 구분명'] == ENUM.transform[kind].value
        year_list = df['연도'] == year
        doc = ENUM.transform[doc].value
        return df[kind_list & year_list][doc].to_dict()