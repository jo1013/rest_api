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
        
    def main(kind, year, doc):
        
        csv_path = PATH.path.data_dir + '/12_19_교통사고정보.csv'
        df = pd.read_csv(csv_path, encoding='utf-8')


        kind_list = df['대상사고 구분명'] == ENUM.transform[kind].value
        year_list = df['연도'] == year
        doc = ENUM.transform[doc].value
        # return df[kind_list & year_list][doc].to_dict('record')
        return df[kind_list & year_list][doc].to_list()
    
    
    def kind_or_doc(kind_doc :str):
        
        csv_path = PATH.path.data_dir + '/12_19_교통사고정보.csv'
        df = pd.read_csv(csv_path, encoding='utf-8')
        ##
        enum_list = list(ENUM.transform)
        for i in range(len(enum_list)) :
            
            if kind_doc == enum_list[i].name :
                break
        ###
        if i < 5 :
            kind_list = df['대상사고 구분명'] == ENUM.transform[kind_doc].value
            return df[kind_list].to_dict('record')
        if 4 < i < 13:
            doc = ENUM.transform[kind_doc].value
            return df[doc].to_dict('record')
            
            
            
        

        
    def year_method(year :int):
        csv_path = PATH.path.data_dir + '/12_19_교통사고정보.csv'
        df = pd.read_csv(csv_path, encoding='utf-8')
        year_list = df['연도'] == year
        return df[year_list].to_dict('record')
        

        
        
    def kind_and_year(kind :str , year : int) :
        csv_path = PATH.path.data_dir + '/12_19_교통사고정보.csv'
        df = pd.read_csv(csv_path, encoding='utf-8')
        kind_list = df['대상사고 구분명'] == ENUM.transform[kind].value
        year_list = df['연도'] == year
        return df[kind_list & year_list].to_dict('record')