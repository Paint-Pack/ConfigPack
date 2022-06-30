import tabula
import pandas as pd
import os

path ="C:\work\СПЕЦИФИКАЦИИ\CS"

filelist = []
napr_list = [[], []]
error_list = []
napr_kolvo = 0

#pdf_file = 'C:/Users/79955/PycharmProjects/Mebel/CS 039.pdf'



for root, dirs, files in os.walk(path):
    for file in files:
        filelist.append(os.path.join(root,file))


for pdf_file in filelist:
    print(pdf_file)
    df = tabula.read_pdf(pdf_file, pages=1)

    for i in range(3):
        try:
            names_colomn = df[i].columns[1]
            if names_colomn.find('Направляющая') != -1 or names_colomn.find('Направляющии') != -1:
                napr_kolvo = napr_kolvo + 1
                for l in range(300, 550, 50):
                    print("...")
                    if names_colomn.find(str(l)) != -1:
                        names_colomn = "Направляющая " + str(l)
                if names_colomn not in napr_list[0]:
                    napr_list[0].append(names_colomn)
                # napr_list[napr_list.index(names_colomn)][0] = napr_list[napr_list.index(names_colomn)][0] + 1


            for el in range(df[i].index.stop):
                naim = df[i][df[i].columns[1]][el]
                # print(naim)
                if naim.find('Направляющая') != -1 or naim.find('Направляющии') != -1:
                    napr_kolvo = napr_kolvo + 1
                    for l in range(300, 550, 50):
                        print("...")
                        if naim.find(str(l)) != -1:
                            naim = "Направляющая " + str(l)
                    if naim not in napr_list:
                        napr_list[0].append(naim)
                    # napr_list[napr_list.index(naim)][0] = napr_list[napr_list.index(naim)][0] + 1
        except:
            error_list.append(pdf_file)
            print("Обработка")

    print(napr_list)
    #for i in range(len(napr_list)):
        #print(napr_list[0][i] + napr_list[1][0])
        #print('\n')
print('error list', error_list)


#pdf_file = 'C:/Users/79955/PycharmProjects/Mebel/CS 039.pdf'




print(df[0])
print(type(df[0]))
print(df[0].columns[1])
print(df[0].index)
names_colomn = df[0].columns[1]
print(df[0][names_colomn][1])

