import re
import pandas as pd


def df_to_list(date):
    src_dir = "d:/FineTec/DailyLoss/pmis_down/"
    src_file: str = "19K2({0}_{0}).xlsx".format(date)
    src_name:str = src_dir + src_file
    df_src:object = pd.read_excel(src_name)['이름']
    df_list:list = df_src.values.tolist()
    print(df_list)




if __name__ == "__main__":
    df_to_list("2021-12-13")





else:
    print("---------- module running ---------")
