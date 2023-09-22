# DIO | Desafio Python | Enriquecedor CSV

Pipeline ETL que tem objetivo de enriquecer um arquivo (cvs) de clientes, com dados de telefone oriundos de outro arquivo (csv) cruzando dados de CPF existem em ambos. É utilizada IA do GPT-4 da OpenAI também para gerar uma mensagem personalizada a cada cliente, sendo por fim gerado novo arquivo contendo dados de telefone e mensagem personalizada direcionada a cada cliente.

## 📚 CSV Necessários

|Nome Arquivo|Estrutura|
|-----|-------|
|SDW2023_CLIENTES.csv|UserID,Nome,CPF|
|SDW2023_TEL.csv|UserID,Telefone,CPF|


