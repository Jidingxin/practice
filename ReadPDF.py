import pdfplumber
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

tableList = []
column = []

def initTableList():
    tableList.append('合并资产负债表')
    tableList.append('母公司资产负债表')
    tableList.append('合并利润表')
    tableList.append('母公司利润表')
    tableList.append('合并现金流量表')
    tableList.append('母公司现金流量表')

def getDf(tables):
    df = None
    for table in tables:
        df = pd.DataFrame(table)
        # 第一列当成表头：
        df = pd.DataFrame(table[1:],columns=table[0])
        global column
        column = table[0]
        # print("column1 = ", column)
    return df

def getDfWithoutHead(tables):
    df = None
    # print("column2 = ", column)
    for table in tables:
        if table[0][0] == '项目':
            break
        df = pd.DataFrame(table[0:],columns=column)
        # print(df)
    return df

def splitTables(pdf):
    initTableList()
    tablePageRange = {}
    index = []
    pageNumber = 0
    for page in pdf.pages:
        text = page.extract_text()
        if text.find('财务报表调整情况说明') != -1:
            index.append(pageNumber)
        if len(index) == 7:
            break
        for table in tableList:
            if text.find(table) != -1:
                # print("111111",table ,"111111")
                index.append(pageNumber)
        pageNumber += 1
    i = 0
    for table in tableList:
        # if i < 5:
        tablePageRange[table] = index[i:i+2]
        i += 1
        # else:
        #     tablePageRange[table] = [index[i],24]
    # print("2",tablePageRange,"2")
    # print("3",index,"3")
    return tablePageRange




with pdfplumber.open("D:\投资\财报\巨星科技\\2021年第一季度报告全文.PDF") as pdf:

    tablePageRange = splitTables(pdf)
    for key,value in tablePageRange.items():
        # print(value)
        dfList = []
        i = 0
        for page in range(value[0],value[1]+1):
            # print("page =",page)
            if i == 0 :
                dfList.append(getDf(pdf.pages[page].extract_tables()))
                i += 1
            else:
                dfList.append(getDfWithoutHead(pdf.pages[page].extract_tables()))
        dfCombine = pd.concat(dfList, ignore_index=True, sort=False)
        dfCombine.to_excel("D:\投资\财报\巨星科技\\2021年第一季度报告全文_"+key+".xlsx", sheet_name=key)
        print('finish',key)







# with pdfplumber.open("D:\投资\财报\巨星科技\\2021年第一季度报告全文.PDF") as pdf:
#     page14 = pdf.pages[14]
#     # page13 = pdf.pages[12]
#     text14 = page14.extract_text()
#     #print(text14)
#     tables14 = page14.extract_tables()
#     print(tables14)
#     # tables13 = page13.extract_tables()
#     # print(tables12)
#     dfList = []
#     for table in tables14:
#         print(table[0])
#         print(table[0][0] =='其他综合收益')
#         # for row in table:
#         #     print(row)
#         print("#########")
#
#     # df12 = getDf(tables14)
#     df14 = getDfWithoutHead(tables14)
#     # dfCombine = df12.append(df13,sort=False)
#     # dfCombine = pd.concat([df12,df13],ignore_index=True,sort=False)
#     # print(df.head(2))
#         # print(df.tail(3))
#         # print(df.index)
#         # print(df.columns)
#         # #print(df.describe)
#         # print(df[1:2]['2021年3月31日'])
#         # print(df.iloc[1,1])
#         # # df=df.cumsum()
#         # # plt.figure()
#         # # df.plot()
#     # df14.to_excel("D:\投资\财报\巨星科技\\2021年第一季度报告全文.xlsx",sheet_name='Sheet1')


