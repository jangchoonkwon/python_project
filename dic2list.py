import pandas as pd



df = pd.read_excel("d:/00 inbox/p3c_roof/p3c_roof.xlsx")
df_date = df['날짜'].to_list()
df_tail = df['번호'].to_list()

df_row = df.iloc[0][2:].to_list()
df_count = df.shape[0]
df_rows = []
for i in range(df_count):
    df_rows.append(df_row)

print(df_date)
print(df_tail)
print(df_rows)

