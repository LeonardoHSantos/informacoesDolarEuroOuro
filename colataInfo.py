from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


lista_cotacao_dolar = []
lista_cotacao_euro = []
lista_cotacao_ouro = []
valores_lista_cotacoes = {}
arq_drive = "Chromedriver.exe"

# cotação DÓLAR


def cotacao_dolar():
    navegador = webdriver.Chrome(arq_drive)
    navegador.get('https://www.google.com/')
    navegador.find_element_by_xpath(
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

    navegador.find_element_by_xpath(
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
    valor_dolar = navegador.find_element_by_xpath(
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    if valor_dolar != "":
        lista_cotacao_dolar.append(valor_dolar)
    else:
        lista_cotacao_dolar.append("Valor dólar não atribuido")


# cotação EURO
def cotacao_euro():
    navegador = webdriver.Chrome(arq_drive)
    navegador.get('https://www.google.com/')
    navegador.find_element_by_xpath(
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

    navegador.find_element_by_xpath(
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
    valor_euro = navegador.find_element_by_xpath(
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    if valor_euro != "":
        lista_cotacao_euro.append(valor_euro)
    else:
        lista_cotacao_euro.append("Valor não atribuido")


# cotação OURO
def cotacao_ouro():
    navegador = webdriver.Chrome(arq_drive)
    navegador.get('https://www.melhorcambio.com/ouro-hoje')
    valor_ouro = navegador.find_element_by_xpath(
        '//*[@id="comercial"]').get_attribute('value')

    if valor_ouro != "":
        valor_ouro = valor_ouro.replace(",", ".")
        lista_cotacao_ouro.append(valor_ouro)
    else:
        lista_cotacao_ouro.append("Valor ouro nãoa atribuido")


# converte valores_lista_cotacoes para arquivo CSV
def coverte_para_arquivo_csv():
    valores_lista_cotacoes = {
        "Dólar": lista_cotacao_dolar,
        "Euro": lista_cotacao_euro,
        "Ouro": lista_cotacao_ouro
    }
    valores_lista_cotacoes = pd.DataFrame(valores_lista_cotacoes)
    valores_lista_cotacoes.to_csv("BaseProdutosAtualizada.csv")

    valores_lista_cotacoes = pd.read_csv("BaseProdutosAtualizada.csv")
    valores_lista_cotacoes = valores_lista_cotacoes.drop("Unnamed: 0", axis=1)
    valores_lista_cotacoes['Soma'] = valores_lista_cotacoes['Dólar'] + \
        valores_lista_cotacoes['Euro'] + valores_lista_cotacoes['Ouro']

    print(valores_lista_cotacoes)


cotacao_dolar()
cotacao_euro()
cotacao_ouro()
coverte_para_arquivo_csv()
