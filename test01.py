import pandas as pd

# file_in_path = str('D:/FineTec/DailyLoss/pmis/')
# file_out_path = str('D:/FineTec/DailyLoss/pmis_change/')
# file_date = str('2022-01-12')
# file_end = str('.xlsx')
# file_name = str('19K2(') + file_date + str('_') + file_date + str(')')
# file_in_name = file_in_path + file_name + file_end
# file_out_name = file_out_path + file_name + file_end

# nameList = ['김미선', '김정호', '김연수', '이경일', '김민우', '최영철', '윤대성', '전명희', '이희구', '정도균', '이야곱', '정진희', '김노범', '김재호', '김행원', '정상근', '고도현', '정보경', '정기호', '조재혁', '강원진']
# comp = 'ToxicGas배관'

file_in_name: str = '../../FineTec/DailyLoss/pmis/19K2(2022-03-02_2022-03-02).xlsx'
df: object = pd.read_excel(file_in_name, sheet_name=0, engine='openpyxl')
df = df.head()
# df2 = df.iloc[:,[5, 6, 7, 9, 15, 16, 17]]
print(df)

# # df2 = df[['이름', '생년월일', '공종', '출역일자', '출근시각', '퇴근시각']]
# df2 = df[[6, 7, 9, 15, 16, 17]]
#
# # df_name = df.loc[df['이름'].isin(nameList)]
# df_name2 = df2.loc[df['이름'].isin(nameList)]
#
# print(df_name2)
