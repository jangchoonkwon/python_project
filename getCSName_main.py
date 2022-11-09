import getCSName

dirFiles = ["20220513", "20220523"]

for dirf in dirFiles:
    try:
        getCSName.del_Han("d:/FineTec/DailyLoss/ocr" + "/{}".format(dirf))
        getCSName.name_list("d:/FineTec/DailyLoss/ocr" + "/{}".format(dirf))
    except:
        pass
