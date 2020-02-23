#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 7</font>
# 
# ## Download: http://github.com/dsacademybr

# ## Missão: Analisar o Comportamento de Compra de Consumidores.

# ## Nível de Dificuldade: Alto

# Você recebeu a tarefa de analisar os dados de compras de um web site! Os dados estão no formato JSON e disponíveis junto com este notebook.
# 
# No site, cada usuário efetua login usando sua conta pessoal e pode adquirir produtos à medida que navega pela lista de produtos oferecidos. Cada produto possui um valor de venda. Dados de idade e sexo de cada usuário foram coletados e estão fornecidos no arquivo JSON.
# 
# Seu trabalho é entregar uma análise de comportamento de compra dos consumidores. Esse é um tipo de atividade comum realizado por Cientistas de Dados e o resultado deste trabalho pode ser usado, por exemplo, para alimentar um modelo de Machine Learning e fazer previsões sobre comportamentos futuros.
# 
# Mas nesta missão você vai analisar o comportamento de compra dos consumidores usando o pacote Pandas da linguagem Python e seu relatório final deve incluir cada um dos seguintes itens:
# 
# ** Contagem de Consumidores **
# 
# * Número total de consumidores
# 
# 
# ** Análise Geral de Compras **
# 
# * Número de itens exclusivos
# * Preço médio de compra
# * Número total de compras
# * Rendimento total
# 
# 
# ** Informações Demográficas Por Gênero **
# 
# * Porcentagem e contagem de compradores masculinos
# * Porcentagem e contagem de compradores do sexo feminino
# * Porcentagem e contagem de outros / não divulgados
# 
# 
# ** Análise de Compras Por Gênero **
# 
# * Número de compras
# * Preço médio de compra
# * Valor Total de Compra
# * Compras for faixa etária
# 
# 
# ** Identifique os 5 principais compradores pelo valor total de compra e, em seguida, liste (em uma tabela): **
# 
# * Login
# * Número de compras
# * Preço médio de compra
# * Valor Total de Compra
# * Itens mais populares
# 
# 
# ** Identifique os 5 itens mais populares por contagem de compras e, em seguida, liste (em uma tabela): **
# 
# * ID do item
# * Nome do item
# * Número de compras
# * Preço do item
# * Valor Total de Compra
# * Itens mais lucrativos
# 
# 
# ** Identifique os 5 itens mais lucrativos pelo valor total de compra e, em seguida, liste (em uma tabela): **
# 
# * ID do item
# * Nome do item
# * Número de compras
# * Preço do item
# * Valor Total de Compra
# 
# 
# ** Como considerações finais: **
# 
# * Seu script deve funcionar para o conjunto de dados fornecido.
# * Você deve usar a Biblioteca Pandas e o Jupyter Notebook.
# 

# In[1]:


# Imports
import pandas as pd
import numpy as np


# In[31]:


# Carrega o arquivo
load_file = "dados_compras.json"
purchase_file = pd.read_json(load_file, orient = "records")
purchase_file.head()


# # Informações Sobre os Consumidores

# ### Número total de consumidores

# In[17]:


total_consumers = purchase_file.groupby(['Login'], as_index=False).size().count()

print('O número total de consumidores é:', total_consumers)


# # Análise Geral de Compras

# ### Número de itens exclusivos

# In[22]:


count_exclusive_itens = purchase_file.groupby(['Item ID'], as_index=False).size().count()

print('O número de itens exclusivos é:', count_exclusive_itens)


# ### Preço médio de compra

# In[16]:


average_purchase_price = purchase_file['Valor'].mean()

print('O preço médio da compra é: {:0.3f}'.format(average_purchase_price))


# ### Número total de compras

# In[33]:


purchase_file.groupby(['Login', 'Item ID'], as_index=False).size()


# ### Rendimento total

# In[ ]:





# ## Análise Demográfica

# In[ ]:


# Implemente aqui sua solução


# ## Informações Demográficas Por Gênero

# In[ ]:


# Implemente aqui sua solução


# ## Análise de Compras Por Gênero

# In[ ]:


# Implemente aqui sua solução


# ## Consumidores Mais Populares (Top 5)

# In[ ]:


# Implemente aqui sua solução


# ## Itens Mais Populares

# In[ ]:


# Implemente aqui sua solução


# ## Itens Mais Lucrativos

# In[ ]:


# Implemente aqui sua solução


# ## Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
