import pandas as pd
import openai
import time

df_clientes = pd.read_csv('SDW2023_CLIENTES.csv', sep =',', dtype=str)

df_tel = pd.read_csv('SDW2023_TEL.csv', sep =',', dtype=str)

df_cleintes_x_tel = pd.merge(df_clientes,df_tel, left_on=['CPF'], right_on=['CPF'])

df_cleintes_x_tel = pd.DataFrame(df_cleintes_x_tel, columns=['UserID_x','Nome','CPF','Telefone']).rename(columns={'UserID_x': 'UserID'})

df_cleintes_x_tel.insert(4,'Mensagem Personalizada','')

# Substitua o texto TODO por sua API Key da OpenAI, ela será salva como uma variável de ambiente.
openai_api_key = 'TODO'
openai.api_key = openai_api_key

rows = df_cleintes_x_tel.shape[0] 

contador = 0 
while contador < rows:
    print ("Aguarde Gerando Mensagens Personalizadas")
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      messages=[
          {
              "role": "system",
              "content": "Você é um especialista em investimentos."
          },
          {
             "role": "user", 
             "content": f"Crie uma mensagem contendo o nome de {df_cleintes_x_tel.iloc[contador,1]} lhe aconselhando sobre a importância dos investimentos (máximo de 100 caracteres)"
          }
      ] 
    )
    df_cleintes_x_tel.iloc[contador,4] = completion.choices[0].message.content.strip ('\"')
    time.sleep(20)
    contador = contador + 1

print(df_cleintes_x_tel)
df_cleintes_x_tel.to_csv('arquivo_clintes.csv',sep =',', encoding='utf-16', index= False)






