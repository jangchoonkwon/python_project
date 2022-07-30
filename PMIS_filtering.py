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
    date = ["20220615"]
    tail = ["z4"]
    name = [
        "강상희", "강용환", "강혜자", "고도원", "고연희", "곽승진", "곽유미", "곽희명", "권남수", "권덕철", "권수안", "권혁규", "권혁산", "김경민", "김경식", "김경이",
        "김경희", "김광필", "김규봉", "김근화", "김기태", "김동철", "김동학", "김명호", "김미수", "김미숙", "김미영", "김민주", "김민호", "김범석", "김병호", "김보현",
        "김서현", "김선웅", "김선창", "김성규", "김수정", "김숙희", "김승연", "김승혜", "김시현", "김옥진", "김완호", "김운화", "김원태", "김원희", "김은용", "김인식",
        "김재철", "김재칠", "김정미", "김정수", "김정현", "김종섭", "김준", "김준호", "김지혜", "김지훈", "김진만", "김진우", "김진욱", "김태현", "김평호", "김현지",
        "김형구", "김형기", "김형석", "김홍근", "김홍주", "나우흠", "남궁진용", "남도경", "남성현", "노준탁", "박경민", "박경선", "박두리", "박두환", "박득순",
        "박민경", "박민국", "박민수", "박상웅", "박상준", "박새은", "박성재", "박성준", "박순미", "박용준", "박은철", "박제훈", "박종현", "박주완", "박지연", "박찬휘",
        "박현준", "박현춘", "박효웅", "배수진", "배윤호", "백민찬", "백인찬", "백정일", "서상민", "서연학", "서원균", "서종국", "서준석", "소정현", "손경애", "손수영",
        "송경애", "송동일", "송성호", "송영재", "송익준", "송현우", "신기재", "신윤철", "신종철", "신호철", "심흥성", "안수창", "안치옥", "안태준", "안태춘", "양기식",
        "양승범", "양정현", "오민석", "오은경", "오진용", "오현성", "오형철", "왕대위", "우영현", "유미선", "유영하", "윤수빈", "윤순경", "윤여림", "윤영대", "윤인숙",
        "윤자경", "윤지은", "이경일", "이경재", "이경철", "이광석", "이광호", "이국기", "이근혁", "이기환", "이동철", "이문하", "이미향", "이민", "이민호", "이승규",
        "이승호", "이영복", "이윤아", "이은미", "이은혁", "이의현", "이재민", "이정기", "이정길", "이종규", "이종아", "이종현", "이중재", "이지복", "이진석", "이진수",
        "이창준", "이창호", "이철연", "이태진", "이태현", "이한철", "이현숙", "이혜림", "이혜선", "이호삼", "이호상", "이효현", "임병혁", "장영식", "장윤미", "장일수",
        "장정남", "전기홍", "전길남", "전상구", "전희구", "정구열", "정덕수", "정동숙", "정병진", "정성민", "정성호", "정순일", "정영애", "정인수", "정정민", "정지완",
        "정지원", "정창욱", "정현종", "제갈훈", "조대식", "조성범", "조성제", "조장현", "조현규", "조현정", "주영남", "지성현", "진선미", "진성진", "차동운", "차소리",
        "최건희", "최광열", "최기원", "최동인", "최명임", "최선영", "최선화", "최성일", "최순표", "최용석", "최은석", "최이지", "최정호", "최정훈", "최지호", "최지후",
        "최현석", "편승필", "한경범", "한동범", "한동현", "한승용", "한영희", "한종완", "허성문", "허성운", "허찬무", "허찬우", "홍성식", "황미애", "황병철", "황원욱",
        "황인아", "황현승", "황효숙"

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
