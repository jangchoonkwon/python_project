import getCSName


dirFiles = [
    '20220714'
    ]


for dirf in dirFiles:
     try:
         getCSName.del_Han("d:/FineTec/DailyLoss/ocr" + "/{}".format(dirf))
         getCSName.name_list("d:/FineTec/DailyLoss/ocr" + "/{}".format(dirf))
     except:
          pass
