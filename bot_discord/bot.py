from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

#automação para roletar e pegar cartas no mudae
# entrando no discord 
email = input('Email: ').strip()
senha = input('Senha: ').strip()
username = input('seu username (@...): ').strip()
op = webdriver.ChromeOptions() 
op.add_argument('--headless=new')

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service, options=op)
nav.get('https://discord.com/login')

while len(nav.find_elements(By.NAME, 'email'))<1:
    sleep(1)

elem = nav.find_element(By.NAME, 'email')
elem.send_keys(email)
elem = nav.find_element(By.NAME, 'password')
elem.send_keys(senha)
sleep(2)
elem = nav.find_element(By.NAME, 'password')
elem.send_keys(Keys.RETURN)

while len(nav.find_elements(By.CLASS_NAME, 'searchBarComponent__22760'))<1:
    sleep(1)
nav.find_element(By.CLASS_NAME, 'searchBarComponent__22760').click()
sleep(2)
nav.find_element(By.CLASS_NAME, 'input__848cd').click()
sleep(2)
nav.find_element(By.CLASS_NAME, 'input__848cd').send_keys("os preguiçosos de plantão ")
classe = nav.find_elements(By.CLASS_NAME, 'match_a540b5')
try:
    for itens in classe:
        if itens.text in 'os preguiçosos de plantão':
            sleep(2)
            itens.click()
except:
    pass
sleep(2)

nav.find_element(By.CLASS_NAME, 'link__95dc0').click()
nav.find_element(By.CLASS_NAME, 'link__95dc0').send_keys('$wl', Keys.ENTER)
elem = nav.find_elements(By.CLASS_NAME, 'grid_c7c4e6')
 
welem = (elem[-1].text).split()
#pega a lista wish
data_wish = ''
welem_metade = (welem[0][0:5])

if f'{username[0:5]}' in welem_metade:
    data_wish = welem #o nome das minhas wish que esta na lista 
#so para confirmar se e a minha consulta de wl
sleep(3)
nav.find_element(By.CLASS_NAME, 'link__95dc0').send_keys('$ru', Keys.ENTER)

sleep(5)
tu = nav.find_elements(By.CLASS_NAME, 'messageContent__21e69')
rolls = tu[-1] # pega o ultimo resultado de $ru
#ActionChains(nav).context_click(a).perform()
ultimo = tu[-1].text #texto do ultimo $ru
dividido = ultimo.split()
rolls_div = int(dividido[2])
if rolls_div == 0:
        pass
#testar agr/ ok funcionou
else:
    for c in range(1, rolls_div+1):
            nav.find_element(By.CLASS_NAME, 'link__95dc0').click()
            sleep(1)
            nav.find_element(By.CLASS_NAME, 'link__95dc0').send_keys("$wa", Keys.ENTER)
            lost = nav.find_element(By.CLASS_NAME, 'grid_c7c4e6')
            if lost.text[0] in data_wish:# se o nome da personagem estiver na lista wl
                    ActionChains(nav).context_click(lost).perform()
                    nav.find_element(By.CLASS_NAME, 'customItem__7173b').click()
