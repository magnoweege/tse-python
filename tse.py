import pandas as pd
df=pd.read_csv('file.csv', header=None, sep=';')

cidade = 'BOA VISTA'

df_Cidade = df.loc[(df[13]==cidade)] #Separa somente votos da cidade escolhida
df_lam1 = df_Cidade # utilizado para calculos da lamina 1

df_voto_geral = df_Cidade[[21,22,7,8,5,23]] #separa colunas necessárias
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

df_prefeitos = df_lam2.loc[(df_lam2[5]==11)]  #separa somente prefeitos
df_nomes_prefeitos = df_prefeitos[[22]].drop_duplicates() #nomes dos candidatos a prefeito

df_soma_votos_pref = df_prefeitos.reset_index().groupby(21).sum().iloc[:,-1].reset_index().drop(21, 1) # soma de votos recebidos para prefeito
df_pref_soma = df_nomes_prefeitos.join(df_soma_votos_pref)

df_pref_soma = df_pref_soma.sort_values([23, 22], ascending=[0, 1])
df_pref_soma.rename(columns={22:'Prefeito', 23:'Votos'}, inplace=True)


''' ################# FIM LAMINA 2 ##################### '''


''' #################  GRAVAR EXCEL ##################### '''

arquivo = cidade+".xlsx"
writer = pd.ExcelWriter(arquivo)

df_bv.to_excel(writer,"Boa Vista - Relatorio",index=None)   # LAMINA 1
df_pref_soma.to_excel(writer,"Prefeitos",index=None) # LAMINA 2
writer.save()

''' #################  FIM ##################### '''
