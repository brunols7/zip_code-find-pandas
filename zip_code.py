from selenium import webdriver as navigator
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd


#CEP number
num_cep = int(input('Enter the zip code: '))

sleep(1)

nav =  navigator.Chrome()
nav.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

sleep(4)

#start program
nav.find_element(By.NAME, "endereco").send_keys(num_cep)
sleep(3)
nav.find_element(By.NAME, "btn_pesquisar").click()
sleep(2)

#results
street = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
neighb = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
city = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
cep = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text

#Results on notes
df = pd.DataFrame({'street':[street],
                   'neighborhood':[neighb],
                   'city':[city],
                   'CEP':[cep]})

df.to_csv('cep_data.txt', sep='\t', index=False)