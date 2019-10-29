import sys
import os
import base64
import pandas as pd
#sys.path.append(os.path.realpath('../lib'))
#from superpipeline import Superpipeline


useful_columns = ["BUKRS", "IBAN", "LIFNR", "PSWSL", "KOSTL", 
                  "AUFNR", "PROJK", "NPLNR", "GROSS_AMOUNT", "NET_AMOUNT", 
                  "VEND_NAME", "F_TAX_AMOUNT", "TAXRATE_1"]  


class MyProcessor: 
    def check_df(self, df):
        assert len(df.columns)>=13, "Wrong number of columns, expected at least 13"
        assert set(useful_columns).issubset(set(df.columns)), "Some columns are missing"
        
    def run_ml(self, df):
        self.check_df(df)
        sp = Superpipeline()
        sp.load_pipelines()
        predictions = sp.predict(df[useful_columns])
        predictions["GL_prob"] = predictions["GL_prob"].round(decimals=2)
        predictions["TAX_prob"] = predictions["TAX_prob"].round(decimals=2)
        predictions["prob"] = predictions["prob"].round(decimals=2)
        return predictions
    
    def save_files(self, dct):
        with open("{}.pdf".format(dct["FILENAME"]), "wb") as file:
            file.write(base64.b64decode(dct["CONTENT"]))

