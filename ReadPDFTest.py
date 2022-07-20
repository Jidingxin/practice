import pdfplumber
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt


with pdfplumber.open("D:\投资\财报\巨星科技\\2021年第一季度报告全文.PDF") as pdf:
    dfList = []
    dfDict = {}
    tableNum = 0
    column = []
    for page in pdf.pages:
        if page.extract_text().find('第四节 财务报表') == -1:
            continue
        for table in page.extract_tables():
            print(table)
            if table[0][0] == '项目':
                dfList.append(pd.DataFrame(table[1:],columns=table[0]))
                column = table[0]
                tableNum += 1
            else :
                dfList.append(pd.DataFrame(table[0:],columns=column))
