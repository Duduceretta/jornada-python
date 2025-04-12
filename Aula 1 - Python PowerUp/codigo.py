import pyautogui
import time
import os
import sys

# pyautogui.click -> clica em algum lugar
# pyautogui.press -> Aperta 1 tecla
# pyautogui.write -> escreve um texto
# pyautogui.hotkey -> apertar uma combinacao de teclas

pyautogui.PAUSE = 0.5

#Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#espera 3 segundos
time.sleep(3)

#Passo 2: Fazer login
#Preencher email
pyautogui.click(x=781, y=612)
pyautogui.write('12345aaa@gmail.com')

#Preencher senha
#pyautogui.click(x=781, y=761)
pyautogui.press('tab')
pyautogui.write('1234567890@senhaPika')
pyautogui.press('tab')
pyautogui.press('enter')

#espera 3 segundos
time.sleep(3)

#Passo 3: importar a base de dados
import pandas

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_path, 'produtos.csv')

tabela = pandas.read_csv(csv_path)
print(tabela)

#Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=781, y=439)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)

    pyautogui.press('tab') #Passa para o proximo campo
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)

    pyautogui.press('tab')
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)

    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    pyautogui.press('tab')
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)

    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)

    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])

    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')

    #Volta para o inicio da pagina
    pyautogui.scroll(10000)

#Passo 5: Repetir para todos os produtos
# NaN -> Not a Number
# pyautogui -> Fazer automacoes com python
