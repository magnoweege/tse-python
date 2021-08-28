import pandas as pd

df=pd.read_csv('file.csv', header=None, sep=';')

cidade = 'BOA VISTA'
vagasBV = 21

df_Cidade = df.loc[(df[13]==cidade)] #Separa somente votos da cidade escolhida
df_lam1 = df_Cidade # utilizado para calculos da lamina 1

df_voto_geral = df_Cidade[[11,13,21,22,7,8,5,23]] #separa colunas necessárias
df_lam2 = df_voto_geral # utilizado para calculo da lamina 2

''' ################# LAMINA 1 ##################### '''

df_eleitores = df_lam1[[7,8,16,17]].drop_duplicates()
num_eleitores = df_eleitores[17].sum()
num_faltantes = df_eleitores[16].sum()


df_vereadores = df_lam2.loc[(df_lam2[5]==13)]  #separa somente vereadores
df_ver_col = df_lam2.loc[(df_lam2[5]==13)]  #separa somente vereadores


df_vereadores[11].fillna('-', inplace=True)

df_vereadores_voto_branco = df_vereadores[(df_vereadores[22] =="BRANCO")]
df_vereadores_brancos = (df_vereadores_voto_branco.groupby(by=[11,22])[23].sum()).reset_index().drop(11, 1)

df_vereadores_voto_nulo = df_vereadores[(df_vereadores[22] =="NULO")]
df_vereadores_nulo = (df_vereadores_voto_nulo.groupby(by=[11,22])[23].sum()).reset_index().drop(11, 1)

df_ver_total   = df_vereadores[23].sum()
df_ver_nulos   = df_vereadores_nulo.iloc[0][23]
df_ver_brancos = df_vereadores_brancos.iloc[0][23]
df_ver_validos = df_ver_total - df_ver_nulos - df_ver_brancos
df_ver_QE = int(df_ver_validos / vagasBV)


print (df_ver_total)
print (df_ver_nulos)
print (df_ver_brancos)
print (df_ver_validos)
print (df_ver_QE)

######################    lamina 1
prep_df = {"Total de votos":[df_ver_total],
           "Votos Válidos":[df_ver_validos],
           "Votos Nulos":[df_ver_nulos],
           "Votos em Branco":[df_ver_brancos],
           "Quoeficiente Eleitoral":[df_ver_QE]}

df_bv = pd.DataFrame(prep_df)



######################    lamina 2
#
#Coligações:
#
col1 = "Boa Vista Para Você" 
col1p= "(PP, PSC, PRB, PMB, PMN, PEN, PTC, PTN)"
col2 = "Coragem pra Mudar Boa Vista"
col2p= "(PDT, REDE, PHS)"
col3 = "Boa Vista Para Todos Nós"
col3p= "(PT, PCdoB)"
col4 = "Trabalhando Para Todos"
col4p= "(PMDB, PSD, PR, PSB, PPS, SD, PTdoB, PSDC, PSL, PPL)"
col5 = "Boa Vista Para Todos"
col5p= "(DEM, PSDB, PRTB)"
col6 = "Boa Vista Melhor Para Todos"
col6p= "(PV, PTB)"
col7 = "(sem coligação)"
col7p= "PRP"
col8 = "Frente de Esquerda Para Boa Vista"
col8p= "(PSOL, PSTU)"
col9 = "(sem coligação)"
col9p= "PROS"
#
######################   fim lamina 2


df_vereadores_col1 = df_ver_col[(df_ver_col[11] == "PP") | (df_ver_col[11] =="PSC") | (df_ver_col[11] =="PRB") | (df_ver_col[11] =="PMB") | (df_ver_col[11] =="PMN") | (df_ver_col[11] =="PEN") | (df_ver_col[11] =="PTC") | (df_ver_col[11] =="PTN")]
df_vereadores_votos_col1 = df_vereadores_col1[23].sum()

df_vereadores_col2 = df_ver_col[(df_ver_col[11] == "PDT") | (df_ver_col[11] =="REDE") | (df_ver_col[11] =="PHS")]
df_vereadores_votos_col2 = df_vereadores_col2[23].sum()

df_vereadores_col3 = df_ver_col[(df_ver_col[11] == "PT") | (df_ver_col[11] =="PCdoB")]
df_vereadores_votos_col3 = df_vereadores_col3[23].sum()

df_vereadores_col4 = df_ver_col[(df_ver_col[11] == "PMDB") | (df_ver_col[11] =="PSD") | (df_ver_col[11] =="PR") | (df_ver_col[11] =="PSB") | (df_ver_col[11] =="PPS") | (df_ver_col[11] =="SD") | (df_ver_col[11] =="PTdoB") | (df_ver_col[11] =="PSDC") | (df_ver_col[11] =="PSL") | (df_ver_col[11] =="PPL")]
df_vereadores_votos_col4 = df_vereadores_col4[23].sum()

df_vereadores_col5 = df_ver_col[(df_ver_col[11] == "DEM") | (df_ver_col[11] =="PSDB") | (df_ver_col[11] =="PRTB")]
df_vereadores_votos_col5 = df_vereadores_col5[23].sum()

df_vereadores_col6 = df_ver_col[(df_ver_col[11] == "PV") | (df_ver_col[11] =="PTB")]
df_vereadores_votos_col6 = df_vereadores_col6[23].sum()

df_vereadores_col7 = df_ver_col[(df_ver_col[11] == "PRP")]
df_vereadores_votos_col7 = df_vereadores_col7[23].sum()

df_vereadores_col8 = df_ver_col[(df_ver_col[11] == "PSOL") | (df_ver_col[11] =="PSTU")]
df_vereadores_votos_col8 = df_vereadores_col8[23].sum()

df_vereadores_col9 = df_ver_col[(df_ver_col[11] == "PROS")]
df_vereadores_votos_col9 = df_vereadores_col9[23].sum()

print ("col1: ", df_vereadores_votos_col1 )
print ("col2: ", df_vereadores_votos_col2 )
print ("col3: ", df_vereadores_votos_col3 )
print ("col4: ", df_vereadores_votos_col4 )
print ("col5: ", df_vereadores_votos_col5 )
print ("col6: ", df_vereadores_votos_col6 )
print ("col7: ", df_vereadores_votos_col7 )
print ("col8: ", df_vereadores_votos_col8 )
print ("col9: ", df_vereadores_votos_col9 )

vagas_col1_QE = int(df_vereadores_votos_col1/df_ver_QE)
vagas_col2_QE = int(df_vereadores_votos_col2/df_ver_QE)
vagas_col3_QE = int(df_vereadores_votos_col3/df_ver_QE)
vagas_col4_QE = int(df_vereadores_votos_col4/df_ver_QE)
vagas_col5_QE = int(df_vereadores_votos_col5/df_ver_QE)
vagas_col6_QE = int(df_vereadores_votos_col6/df_ver_QE)
vagas_col7_QE = int(df_vereadores_votos_col7/df_ver_QE)
vagas_col8_QE = int(df_vereadores_votos_col8/df_ver_QE)
vagas_col9_QE = int(df_vereadores_votos_col9/df_ver_QE)


prep_df_col1 = {"Coligação":[col1],
           "Partidos":[col1p],
           "Votação":[df_vereadores_votos_col1],
           "Vagas QP":[vagas_col1_QE],
           "valores":[0],
           "Vagas Sobra ou média":[0]}


df_col1 = pd.DataFrame(prep_df_col1)

prep_df_col2 = {"Coligação":[col2],
           "Partidos":[col2p],
           "Votação":[df_vereadores_votos_col2],
           "Vagas QP":[vagas_col2_QE],
           "valores":[0],
           "Vagas Sobra ou média":[0]}


df_col2 = pd.DataFrame(prep_df_col2)

prep_df_col3 = {"Coligação":[col3],
           "Partidos":[col3p],
           "Votação":[df_vereadores_votos_col3],
           "Vagas QP":[vagas_col3_QE],
           "valores":[0],
           "Vagas Sobra ou média":[0]}

df_col3 = pd.DataFrame(prep_df_col3)


prep_df_col4 = {"Coligação":[col4],
           "Partidos":[col4p],
           "Votação":[df_vereadores_votos_col4],
           "Vagas QP":[vagas_col4_QE],
           "valores":[0],
           "Vagas Sobra ou média":[0]}

df_col4 = pd.DataFrame(prep_df_col4)


prep_df_col5 = {"Coligação":[col5],
           "Partidos":[col5p],
           "Votação":[df_vereadores_votos_col5],
           "Vagas QP":[vagas_col5_QE],
           "valores":[0],
           "Vagas Sobra ou média":[0]}

df_col5 = pd.DataFrame(prep_df_col5)


prep_df_col6 = {"Coligação":[col6],
           "Partidos":[col6p],
           "Votação":[df_vereadores_votos_col6],
           "Vagas QP":[vagas_col6_QE],
           "valores":[0],
           "Vagas Sobra ou média":[0]}

df_col6 = pd.DataFrame(prep_df_col6)


prep_df_col7 = {"Coligação":[col7],
           "Partidos":[col7p],
           "Votação":[df_vereadores_votos_col7],
           "Vagas QP":[vagas_col7_QE],
           "valores":[0],
           "Vagas Sobra ou média":[0]}

df_col7 = pd.DataFrame(prep_df_col7)


prep_df_col8 = {"Coligação":[col8],
           "Partidos":[col8p],
           "Votação":[df_vereadores_votos_col8],
           "Vagas QP":[vagas_col8_QE],
           "valores":[0],
           "Vagas Sobra ou média":[0]}

df_col8 = pd.DataFrame(prep_df_col8)


prep_df_col9 = {"Coligação":[col9],
           "Partidos":[col9p],
           "Votação":[df_vereadores_votos_col9],
           "Vagas QP":[vagas_col9_QE],
           "valores":[0],
           "Vagas Sobra ou média":[0]}

df_col9 = pd.DataFrame(prep_df_col9)


df_aba1 = df_col1.append(df_col2)
df_aba2 = df_aba1.append(df_col3)
df_aba3 = df_aba2.append(df_col4)
df_aba4 = df_aba3.append(df_col5)
df_aba5 = df_aba4.append(df_col6)
df_aba6 = df_aba5.append(df_col7)
df_aba7 = df_aba6.append(df_col8)
df_aba  = df_aba6.append(df_col9)


vagas_preenchidas_QP = df_aba["Vagas QP"].sum()
vagas_faltantes = vagasBV - vagas_preenchidas_QP

#for i in range (len(df_aba)):
#    if ((df_aba.iloc[i]["Vagas QP"]) > 0):
#        print (df_aba.iloc[i]["Vagas QP"])



df_calculo = df_aba[(df_aba["Vagas QP"] > 0)].reset_index()



for i in range (len(df_calculo)):
    df_calculo.at[i, "valores"] = df_calculo.iloc[i]["Votação"] / df_calculo.iloc[i]["Vagas QP"] + df_calculo.iloc[i]["Vagas Sobra ou média"]+1

for i in range (len(df_calculo)):
    if ( df_calculo.iloc[i]["valores"] == max(df_calculo["valores"])):
         df_calculo.at[i]["Vagas Sobra ou média"] = df_calculo.iloc[i]["Vagas Sobra ou média"]+1

print(df_calculo)

    


#for i in range (len(calculo)):
#    print(df_aba.iloc[i]["Vagas QP"])

#print (temp)
#print(len(temp))

#temp = df_vQP.loc[(df_vQP["Vagas QP"] > 0)]

   



''' #################  GRAVAR EXCEL ##################### '''

arquivo = "RR-BoaVista.xlsx"
writer = pd.ExcelWriter(arquivo)

df_bv.to_excel(writer,"Dados Gerais",index=None)   # LAMINA 1
df_aba.to_excel(writer,"Vagas por Coligações",index=None)   # LAMINA 2

#df_pref_ver.to_excel(writer,"Prefeitos e Vereadores",index=None)   # LAMINA 2
#df_pref_soma_votos_M.to_excel(writer,"Prefeitos Votos Descrescente",index=None)   # LAMINA 3
#df_ver_soma_voto_M.to_excel(writer,"Vereadores Votos Descrescente",index=None)   # LAMINA 4

'''   usar depois
for name, group in df_ver_soma_votos_5.groupby([11]):
    df_ord = group.sort_values([11,23], ascending=[True,False]).drop(11, 1)
    df_ord.rename(columns={ 22:'Vereadores', 23:'Votos'}, inplace=True) #muda nome colunas
    df_ord.to_excel(writer,name,index=None) # LAMINA 5 +
'''
writer.save()

''' #################  FIM ##################### '''
