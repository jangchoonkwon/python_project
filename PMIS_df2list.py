import csv
import pandas as pd


def mk_moList(pm_date):
    pm_dir = "d:/FineTec/DailyLoss/pmis_down/"
    pm_file:str = "19K2({0}_{0}).xlsx".format(pm_date)
    pm_name:str = pm_dir + pm_file
    df = pd.read_excel(pm_name)
    # df = df.loc[df['공종'] == 'ToxicGas배관']
    df = df.loc[df['계약구분'] == '단순노무직']
    df = df['이름']
    df_list = df.tolist()
    with open("d:/FineTec/DailyLoss/ocr/cs_list_all.csv", 'a', newline='', encoding='cp949') as f:
        writer = csv.writer(f)
        writer.writerow(df_list)
    print(df_list)


def get_unik(moN):
    pm_dir = "d:/FineTec/DailyLoss/ocr/"
    pm_file:str = "cs_list_{}.xlsx".format(moN)
    pm_name:str = pm_dir + pm_file
    df = pd.read_excel(pm_name)
    df = df.values.tolist()
    df = sum(df, [])
    df = set(df)
    with open("d:/FineTec/DailyLoss/ocr/cs_tolist_{}.csv".format(moN), 'a', newline='', encoding='cp949') as f:
        writer = csv.writer(f)
        writer.writerow(df)
    print(df)


if __name__ == "__main__":
    get_unik(100)

    # x_list = [
    #
    # ]
    #
    # for d in x_list:
    #     mk_moList(d)





else:
    print("---------- module running ----------")
