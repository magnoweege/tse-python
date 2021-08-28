import pandas as pd
df=pd.read_csv('file.csv', header=None, sep=';')

cidade = 'BOA VISTA'

df_Cidade = df.loc[(df[13]==cidade)] #Separa somente votos da cidade escolhida
df_lam1 = df_Cidade # utilizado para calculos da lamina 1

df_voto_geral = df_Cidade[[21,22,7,8,5,23]] #separa colunas necessárias
df_lam2 = df_voto_geral # utilizado para calculo da lamina 2


df_vereadores = df_lam2.loc[(df_lam2[5]==13)] #separa somente vereadores
print(len(df_vereadores))

df_vereadores_sem_legenda = df_vereadores[df_vereadores[21] > 100]
print(len(df_vereadores_sem_legenda))

df_vereadores_sem_legenda_unique = df_vereadores_sem_legenda[[22]].drop_duplicates() #nomes dos candidatos a vereador
print(len(df_vereadores_sem_legenda_unique))

arquivo = cidade+"_ver.xlsx"
writer = pd.ExcelWriter(arquivo)

df_vereadores_sem_legenda.to_excel(writer,"Vereador 1",index=None)   # LAMINA 1
df_vereadores_sem_legenda_unique.to_excel(writer,"Vereador 2",index=None)   # LAMINA 2

writer.save()
