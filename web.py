from selenium.webdriver.common.by import By
from selenium import webdriver

from crud import add_notebook, fabricante, excel


class Web:
    def __init__(self, marca, banco):
        self.nomes = []
        self.banco = banco
        self.marca = marca
        self.site = "https://www.kabum.com.br/computadores/notebooks$marca$".replace("$marca$", f"{self.marca}")
        self.map = {
            "nome": {
                "xpath": "/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/main/div[$num$]/a/div/button/div/h2/span"
            },
            "valor": {
                "xpath": "/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/main/div[$num$]/a/div/div[1]/span[2]"
            },
        }
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.varrer_site()
        self.driver.close()

    def varrer_site(self):
        self.driver.get(self.site)
        nome_lista=[]
        marca_lista=[]
        valor_lista=[]
        i = 0
        while True:
            i += 1
            if len(self.nomes) == 10:
                break
            try:
                nome = self.driver.find_element(By.XPATH, self.map["nome"]["xpath"].replace("$num$", f"{i}")).text
                if nome in self.nomes:
                    continue
                else:
                    self.nomes.append(nome)
                    nomea = nome.split(",")[0]
                    nomeb = nome.split(" ")[0:4]
                    fabri = fabricante(nomeb)
                    valor = self.driver.find_element(By.XPATH, self.map["valor"]["xpath"].replace("$num$", f"{i}")).text
                    add_notebook(nomea, fabri, valor, self.banco)
                    nome_lista.append(nomea) 
                    marca_lista.append(fabri)
                    valor_lista.append(valor)
                   
            except:
                break
        dados = excel(nome_lista, marca_lista, valor_lista)
        dados.to_excel(f"C:/Users/52211545874/Desktop/salvar/{self.marca}.xlsx")
        dados.to_csv(f"C:/Users/52211545874/Desktop/salvar/{self.marca}.csv", sep=";")
        nome_lista.clear
        marca_lista.clear
        valor_lista.clear

        
        





# /html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/main/div[1]/a/div/button/div/h2/span
# /html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/main/div[2]/a/div/button/div/h2/span


# /html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/main/div[2]/a/div/div[1]/span[2]
# /html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/main/div[1]/a/div/div[1]/span[2]



