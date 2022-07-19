import os, shutil


def dir_list():
    dir_path = "d:/FineTec/DailyLoss/ocr/"
    files = os.listdir(dir_path)
    print(files)

def mkDir_forfile():
    file_path = "d:/FineTec/DailyLoss/ocr/cs_dn/"
    dir_path = "d:/FineTec/DailyLoss/ocr/"
    creat_folders = []
    files = os.listdir(file_path)
    files = [f for f in files if f.endswith('.png')]
    # tgr_path = "{}".format([:8])
    # print(len(files))
    # print(files)
    for i in files:
        if i.split('-')[0] not in creat_folders:
            creat_folders.append(i.split('-')[0])
    for item in creat_folders:
        if not os.path.exists(dir_path + '/' + item):
            os.makedirs(dir_path + '/' + item)
    for i in files:
        shutil.move(file_path + '/' + i, dir_path + '/' + i.split('-')[0] + '/' + i)


if __name__ == "__main__":
    dir_path:str = "d:/FineTec/DailyLoss/working/Loss/"
    dir_names:list = [
        "2021-10-04", "2021-10-09", "2021-10-11", "2022-02-10", "2022-02-14", "2022-02-15",
        "2022-02-16", "2022-02-17", "2022-02-18", "2022-02-21", "2022-02-22", "2022-02-23", "2022-02-24",
        "2022-02-25", "2022-02-28", "2022-03-01", "2022-03-02", "2022-03-03", "2022-03-04",
        "2022-03-07", "2022-03-08", "2022-03-10", "2022-03-11", "2022-03-12", "2022-03-14", "2022-03-15", "2022-03-16",
        "2022-03-17", "2022-03-18", "2022-03-19", "2022-03-21", "2022-03-22", "2022-03-23", "2022-03-24", "2022-03-25",
        "2022-03-26", "2022-03-28", "2022-03-29", "2022-03-30", "2022-03-31", "2022-04-01", "2022-04-02", "2022-04-04", "2022-04-05", "2022-04-06", "2022-04-07", "2022-04-08", "2022-04-09", "2022-04-11", "2022-04-12", "2022-04-13", "2022-04-14", "2022-04-15", "2022-04-16", "2022-04-18", "2022-04-19", "2022-04-20", "2022-04-21", "2022-04-22", "2022-04-23", "2022-04-25", "2022-04-26", "2022-04-27", "2022-04-28", "2022-04-29", "2022-05-03", "2022-05-10", "2022-05-17", "2022-05-18", "2022-05-19", "2022-05-23", "2022-05-24", "2022-05-25", "2022-06-08", "2022-06-13", "2022-06-14", "2022-06-15", "2022-06-16", "2022-06-27", "2022-07-14"

    ]
    for i in dir_names:
        os.makedirs(dir_path + './{}'.format(i))
else:
    print("---------- module running ---------")
