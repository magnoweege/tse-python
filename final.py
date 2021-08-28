import pandas as pd
df=pd.read_csv('file.csv', header=None, sep=';')

cidade = 'BOA VISTA'

df_Cidade = df.loc[(df[13]==cidade)] #Separa somente votos da cidade escolhida
df_lam1 = df_Cidade # utilizado para calculos da lamina 1

df_voto_geral = df_Cidade[[11,21,22,7,8,5,23]] #separa colunas necessárias
df_lam2 = df_voto_geral # utilizado para calculo da lamina 2

''' ################# LAMINA 1 ##################### '''

num_secoes = len(df_lam1[[7,8]].drop_duplicates())
num_zonas = len(df_lam1[[7]].drop_duplicates())
df_eleitores = df_lam1[[7,8,16,17]].drop_duplicates()
num_eleitores = df_eleitores[17].sum()
num_faltantes = df_eleitores[16].sum()

prep_df = {"Secoes":[num_secoes],
     "Zonas":[num_zonas],
     "Eleitores votantes":[num_eleitores],
     "Eleitores faltantes":[num_faltantes]}

df_bv = pd.DataFrame(prep_df)


''' ################# FIM LAMINA 1 ##################### '''


''' ################# LAMINA 2 ##################### ''' 

#Prefeitos
df_prefeitos = df_lam2.loc[(df_lam2[5]==11)]  #separa somente prefeitos
df_prefeitos[11].fillna('-', inplace=True)

df_pref_soma_votos = (df_prefeitos.groupby(by=[11,22])[23].sum()).reset_index().drop(11, 1) # soma votos
df_pref_soma_votos3 = (df_prefeitos.groupby(by=[11,22])[23].sum()).reset_index() # #uso lamina 3
df_pref_soma_votos.rename(columns={ 11:'Legenda', 22:'Prefeitos', 23:'Votos'}, inplace=True) #muda nome colunas

#Vereadores
df_vereadores = df_lam2.loc[(df_lam2[5]==13)]  #separa somente vereadores

df_vereadores[11].fillna('-', inplace=True)
df_vereadores_sem_legenda = df_vereadores[(df_vereadores[21] > 100) | (df_vereadores[22] =="NULO") | (df_vereadores[22] =="BRANCO")]
df_ver_soma_votos = (df_vereadores_sem_legenda.groupby(by=[11,22])[23].sum()).reset_index().drop(11, 1) # soma votos
df_ver_soma_votos4 = (df_vereadores_sem_legenda.groupby(by=[11,22])[23].sum()).reset_index() #uso lamina 4
df_ver_soma_votos.rename(columns={ 11:'Legenda', 22:'Vereadores', 23:'Votos'}, inplace=True) #muda nome colunas

df_pref_ver = pd.concat([df_pref_soma_votos, df_ver_soma_votos], axis=1)

'''  ################# FIM LAMINA 2 #################'''

''' ################# LAMINA 3 ##################### ''' 

df_pref_soma_votos3.rename(columns={ 22:'Prefeitos', 11:'Legenda', 23:'Votos'}, inplace=True)
df_pref_soma_votos_M = df_pref_soma_votos3.sort_values(['Votos', 'Legenda', 'Prefeitos'], ascending=[0,0,1])# ordem decrescente por voto


''' ################# FIM LAMINA 3 ##################### '''

''' ################# LAMINA 4 ##################### ''' 

df_ver_soma_votos4.rename(columns={ 22:'Vereadores',11:'Legenda', 23:'Votos'}, inplace=True) #muda nome colunas
df_ver_soma_voto_M = df_ver_soma_votos4.sort_values(['Votos', 'Legenda', 'Vereadores'], ascending=[0,0,1])# ordem decrescente


''' ################# FIM LAMINA 4 #####################'''

df_vereadores_5 = df_lam2.loc[(df_lam2[5]==13)]
df_vereadores_sem_legenda_5 = df_vereadores_5[(df_vereadores_5[21] > 100) | (df_vereadores_5[22] =="NULO") | (df_vereadores_5[22] =="BRANCO")]
df_ver_soma_votos_5 = (df_vereadores_sem_legenda_5.groupby(by=[11,22])[23].sum()).reset_index() #uso lamina 4


''' #################  GRAVAR EXCEL ##################### '''

arquivo = cidade+".xlsx"
writer = pd.ExcelWriter(arquivo)

df_bv.to_excel(writer,"Boa Vista - resumo",index=None)   # LAMINA 1
df_pref_ver.to_excel(writer,"Prefeitos e Vereadores",index=None)   # LAMINA 2
df_pref_soma_votos_M.to_excel(writer,"Prefeitos Votos Descrescente",index=None)   # LAMINA 3
df_ver_soma_voto_M.to_excel(writer,"Vereadores Votos Descrescente",index=None)   # LAMINA 4

for name, group in df_ver_soma_votos_5.groupby([11]):
    df_ord = group.sort_values([11,23], ascending=[True,False]).drop(11, 1)
    df_ord.rename(columns={ 22:'Vereadores', 23:'Votos'}, inplace=True) #muda nome colunas
    df_ord.to_excel(writer,name,index=None) # LAMINA 5 +

writer.save()

''' #################  FIM ##################### '''
