import re
import pandas as pd

frame = pd.read_csv("d:/FineTec/DailyLoss/ocr/CS_nameList.csv", encoding='cp949')
print(frame)

ch_name = frame.apply(lambda x: replace("허타석","허태석"))

# frame.to_csv("./", header=False, index=False)


