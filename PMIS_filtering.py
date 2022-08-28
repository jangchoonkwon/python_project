import pandas as pd
# import re
# import dic2list


def name_to_excel_roof(dt, tl, outName):
    file_in_path = "d:/FineTec/DailyLoss/pmis_down/"
    file_out_path = "d:/00 inbox/p3c_roof/"
    file_out_path = "d:/FineTec/DailyLoss/일일로스_1차완성_20220615_S-Gas_2차작업중/pmis-s/"
    file_date: dt
    file_name = "19K2({0}-{1}-{2}_{0}-{1}-{2}){3}.xlsx".format(dt[:4], dt[4:6], dt[-2:], tl)
    file_in_name = file_in_path + "19K2({0}-{1}-{2}_{0}-{1}-{2}).xlsx".format(dt[:4], dt[4:6], dt[-2:])
    # file_name: str = "19K2({0}-{1}-{2}_{0}-{1}-{2}).xlsx".format(dt[:4], dt[4:6], dt[-2:])
    # file_in_name = file_in_path + file_name
    file_out_name = file_out_path + "19K2({0}-{1}-{2}_{0}-{1}-{2}){3}.xlsx".format(dt[:4], dt[4:6], dt[-2:], tl)
    df = pd.read_excel(file_in_name, engine='openpyxl')
    df2 = df.iloc[:, [5, 6, 8, 9, 14, 15, 16, 17]]
    df_name = df.loc[df['이름'].isin(outName)]
    df_nameA: object = df2.loc[df['이름'].isin(outName)]
    df_nameC = df_name.loc[df['공종'] == 'Chemical배관']
    # df_name2 = df_name.loc[df['공종'] == 'ToxicGas배관']
    df_name2 = df_name.loc[df['공종'] == 'Chemical배관']
    print(df_nameA)

    with pd.ExcelWriter(file_out_name) as writer:
        df_name2.to_excel(writer, sheet_name="sheet1", index=False)
        # df_nameC.to_excel(writer, sheet_name="sheet1", index=False)
        print(file_out_name + " --> 파일을 만들었습니다.")


def name_to_excel(dt, tl, outName):
    file_in_path = "d:/FineTec/DailyLoss/pmis_down/"
    file_out_path = "d:/FineTec/DailyLoss/working\pmis-s/"
    # file_out_path = "d:/FineTec/DailyLoss/일일로스_1차완성_20220615_S-Gas_2차작업중/pmis-s/"
    file_date: dt
    file_name = "19K2({0}-{1}-{2}_{0}-{1}-{2}){3}.xlsx".format(dt[:4], dt[4:6], dt[-2:], tl)
    file_in_name = file_in_path + "19K2({0}-{1}-{2}_{0}-{1}-{2}).xlsx".format(dt[:4], dt[4:6], dt[-2:])
    # file_name: str = "19K2({0}-{1}-{2}_{0}-{1}-{2}).xlsx".format(dt[:4], dt[4:6], dt[-2:])
    # file_in_name = file_in_path + file_name
    file_out_name = file_out_path + "19K2({0}-{1}-{2}_{0}-{1}-{2}){3}.xlsx".format(dt[:4], dt[4:6], dt[-2:], tl)
    df = pd.read_excel(file_in_name, engine='openpyxl')
    df2 = df.iloc[:, [5, 6, 8, 9, 14, 15, 16, 17]]
    df_name = df.loc[df['이름'].isin(outName)]
    df_nameA: object = df2.loc[df['이름'].isin(outName)]
    # df_nameC = df_name.loc[df['공종'] == 'Chemical배관']
    # df_name2 = df_name.loc[df['공종'] == 'ToxicGas배관']
    # df_name2 = df_name.loc[df['공종'] == 'Chemical배관']
    print(df_nameA)

    with pd.ExcelWriter(file_out_name) as writer:
        df_name.to_excel(writer, sheet_name="sheet1", index=False)
        # df_nameC.to_excel(writer, sheet_name="sheet1", index=False)
        print(file_out_name + " --> 파일을 만들었습니다.")


def name_to_excel_s1(dt, tl, outName):
    file_in_path = "d:/FineTec/DailyLoss/pmis_down/"
    file_out_path = "d:/FineTec/DailyLoss/working/pmis-s/"
    file_date: dt
    file_name = "19K2({0}-{1}-{2}_{0}-{1}-{2}).xlsx".format(dt[:4], dt[4:6], dt[-2:])
    file_in_name = file_in_path + file_name
    file_out_name = file_out_path + "19K2({0}-{1}-{2}_{0}-{1}-{2}){3}.xlsx".format(dt[:4], dt[4:6], dt[-2:], tl)

    df = pd.read_excel(file_in_name, engine='openpyxl')
    df_name = df.loc[df['이름'].isin(outName)]
    df_nameS = df_name.loc[df['공종'] == 'ToxicGas배관']

    df2 = df.iloc[:, [5, 6, 8, 9, 14, 15, 16, 17]]
    df2_name: object = df2.loc[df['이름'].isin(outName)]
    df2_nameS = df2_name.loc[df['공종'] == 'ToxicGas배관']
    print(df2_nameS)

    with pd.ExcelWriter(file_out_name) as writer:
        df_nameS.to_excel(writer, sheet_name="sheet1", index=False)
        print(file_out_name + " --> 파일을 만들었습니다.")


def name_to_excel_c1(dt, tl, outName):
    file_in_path = "d:/FineTec/DailyLoss/pmis_down/"
    file_out_path = "d:/FineTec/DailyLoss/pmis-c/"
    file_date: dt
    file_name = "19K2({0}-{1}-{2}_{0}-{1}-{2}).xlsx".format(dt[:4], dt[4:6], dt[-2:])
    file_in_name = file_in_path + file_name
    file_out_name = file_out_path + "19K2({0}-{1}-{2}_{0}-{1}-{2}){3}.xlsx".format(dt[:4], dt[4:6], dt[-2:], tl)

    df = pd.read_excel(file_in_name, engine='openpyxl')
    df_name = df.loc[df['이름'].isin(outName)]
    df_nameC = df_name.loc[df['공종'] == 'Chemical배관']

    df2 = df.iloc[:, [5, 6, 8, 9, 14, 15, 16, 17]]
    df2_name: object = df2.loc[df['이름'].isin(outName)]
    df2_nameC = df2_name.loc[df['공종'] == 'Chemical배관']
    print(df2_nameC)

    with pd.ExcelWriter(file_out_name) as writer:
        df_name.to_excel(writer, sheet_name="sheet1", index=False)
        print(file_out_name + " --> 파일을 만들었습니다.")


def name_view(dt: str, tl: str, outName: object):
    file_in_path = "d:/FineTec/DailyLoss/pmis_down/"
    file_out_path = "d:/FineTec/DailyLoss/일일로스_1차완성_20220615_S-Gas_2차작업중/pmis-s/"
    file_date: dt
    file_name: str = "19K2({0}-{1}-{2}_{0}-{1}-{2}).xlsx".format(dt[:4], dt[4:6], dt[-2:])
    file_in_name = file_in_path + file_name
    df = pd.read_excel(file_in_name, engine='openpyxl')
    df2 = df.iloc[:, [5, 6, 8, 9, 14, 17]]
    df2_name: object = df2.loc[df['이름'].isin(outName)]
    # df2_nameC = df_name.loc[df['공종']== 'Chemical배관']
    df2_nameS = df2_name.loc[df['공종'] == 'ToxicGas배관']
    print(df2_nameS)


def name_to_working(dt, tl, outName):
    file_in_path = "d:/FineTec/DailyLoss/pmis_down/"
    file_out_path = "d:/FineTec/DailyLoss/working/Loss/{0}-{1}-{2}/".format(dt[:4], dt[4:6], dt[-2:])
    file_date: dt
    file_name = "19K2({0}-{1}-{2}_{0}-{1}-{2}).xlsx".format(dt[:4], dt[4:6], dt[-2:])
    file_in_name = file_in_path + file_name
    file_out_name = file_out_path + "19K2({0}-{1}-{2}_{0}-{1}-{2}){3}.xlsx".format(dt[:4], dt[4:6], dt[-2:], tl)
    df = pd.read_excel(file_in_name, engine='openpyxl')
    df_name = df.loc[df['이름'].isin(outName)]
    df_nameS = df_name.loc[df['공종'] == 'ToxicGas배관']
    df2 = df.iloc[:, [5, 6, 8, 9, 14, 15, 16, 17]]
    df2_name: object = df2.loc[df['이름'].isin(outName)]
    df2_nameS = df2_name.loc[df['공종'] == 'ToxicGas배관']
    print(df2_nameS)

    with pd.ExcelWriter(file_out_name) as writer:
        df_nameS.to_excel(writer, sheet_name="sheet1", index=False)
        print(file_out_name + " --> 파일을 만들었습니다.")


if __name__ == "__main__":
    date = ["20220627"]
    tail = ["b4"]
    name = [
        "강용환", "고도원", "고연희", "곽유미", "김경민", "김경식", "김경식", "김경이", "김규봉", "김미숙", "김민주", "김민호", "김범석", "김상우", "김서현", "김선창",
        "김승연", "김승혜", "김영섭", "김옥진", "김원희", "김인식", "김정수", "김종섭", "김준호", "김지혜", "김지훈", "김진만", "김평호", "김형기", "나영균", "나우흠",
        "남성현", "노준탁", "박경민", "박두환", "박득순", "박민수", "박상웅", "박상준", "박용준", "박주완", "박지연", "배수진", "배윤호", "백인찬", "서상민", "서연학",
        "서원균", "서준석", "소정현", "손경애", "손수영", "송동일", "송성호", "신윤철", "안치옥", "오민석", "오진용", "오현성", "오형철", "우영현", "유성민", "윤세빈",
        "윤순경", "윤영대", "이경철", "이광석", "이광호", "이민호", "이승호", "이윤아", "이은미", "이은미", "이의현", "이재민", "이정기", "이종규", "이종아", "이준호",
        "이지복", "이창준", "이태현", "이현숙", "이혜림", "이효현", "임건우", "장광동", "장영식", "장윤미", "정구열", "정덕수", "정동숙", "정성민", "정성호", "정순일",
        "정현종", "조대식", "조현정", "주영남", "지성현", "진선미", "차동운", "차소리", "최건희", "최기원", "최명임", "최선영", "최선화", "최순표", "최용석", "최은석",
        "최이지", "최정호", "최현석", "한동범", "한승용", "허성운", "황미애", "황현승"

    ]

    # name_to_excel_c1(str(date[0]), str(tail[0]), list(name))
    name_to_excel_s1(str(date[0]), str(tail[0]), list(name))
    # name_to_excel(str(date[0]), str(tail[0]), list(name))
    # name_to_working(str(date[0]), str(tail[0]), list(name))


    # date = ["20220704", "20220704", "20220704", "20220704", "20220705", "20220705", "20220705", "20220705"]
    # tail = ["37", "38", "02", "03", "35", "36", "02", "03"]
    # df = pd.read_excel("d:/00 inbox/p3c_roof/p3c_roof.xlsx")
    # df_date = df['날짜'].to_list()
    # df_tail = df['번호'].to_list()
    # df_count = df.shape[0]
    # df_rows = []
    # for i in range(df_count):
    #     df_row = df.loc[i][2:].to_list()
    #     df_rows.append(df_row)
    #     name_to_excel(str(df_date[i]), str(df_tail[i]), list(df_rows[i]))

    # df = pd.read_excel("d:/00 inbox/p3c_roof/p3c_roof.xlsx")
    # df_date = df['날짜'].to_list()
    # df_tail = df['번호'].to_list()
    # df_count = df.shape[0]
    # df_rows = []
    # for i in range(df_count):
    #     df_row = df.loc[i][2:].to_list()
    #     df_rows.append(df_row)
    #     name_to_excel_1(str(df_date[i]), str(df_tail[i]), list(df_rows[i]))


else:
    print("---------- module is running ----------")
