import time
import functions as f
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

credenciais = f.abrirJS()
chamado = f.chamado_final2()

while True:
    
    
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")    
    driver = webdriver.Chrome(options=options)


    
    url = "https://ca.grupocarbel.com.br/SSM/Account/LogOn?opcao=logoff"

    driver.get(url)
    time.sleep(1)

    buton = driver.find_elements(By.ID,"UserName")
    buton[0].send_keys(credenciais['user'])
    buton = driver.find_elements(By.ID,"Key")
    buton[0].send_keys(credenciais['pass'])
    time.sleep(1)
    
    buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"btnContinuar")))
    buton.click()    
    # buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"buscaRapida")))
    # buton.send_keys(822642)
    # buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@onclick='buscaRapida();']")))
    # buton.click()

    buton = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.ID,"opcaoBoxNovoChamado")))    
    buton.click() 

    buton = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.ID,"abrirSelecaoSolicitante")))    
    buton.click()    

    buton = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@class='k-link' and normalize-space(text())='Login']/preceding-sibling::a[@class='k-grid-filter']")))    
    buton.click()    

    buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,"//input[@data-bind='value:filters[0].value']")))
    buton.click()
    buton.send_keys(chamado['usuario']) 

    time.sleep(5)   
    
    buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH,"//button [@type='submit']")))
    buton.click()
    

    buton = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//span[contains(@class, 'k-icon') and contains(@class, 'k-i-tick')]")))     
    buton.click()    

    buton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
    By.XPATH, "//span[contains(@class, 'k-in') and contains(normalize-space(.), 'TI')]")))
    buton.click()

    buton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
    By.XPATH, "//span[contains(@class, 'k-in') and contains(normalize-space(.), 'Pastas de Rede')]")))
    buton.click()
    
    buton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
    By.XPATH, "//span[contains(@title, 'Pastas de Rede - Dúvidas') and contains(normalize-space(.), 'Dúvidas')]")))
    buton.click()

    buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//textarea[@id='Motivo']")))
    buton.send_keys(chamado['descricao'])

    buton = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((
    By.XPATH, "//span[contains(@id, 'Salvar') and contains(normalize-space(.), 'Salvar')]")))
    buton.click()  
       

    buton = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@id='Realizar']")))    
    buton.click()

    buton = WebDriverWait(
    driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='StatusDaAtividadeDoChamadoTipoDeStatusDeAtividadeId_input' and @class='k-input']")))
    buton.click()
    buton.send_keys("Solucionar Chamado")

    # --- Finalização d chamado, já na tela de solucionar
    buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
    By.XPATH,"//textarea[@name='DescricaoStatusDaAtividade']")))
    buton.send_keys(chamado['finalizar'])

    buton = WebDriverWait(driver,10).until(EC.presence_of_element_located((
    By.XPATH,"//span[@id='Salvar' and @data-i18n='Salvar' and @comando='Salvar' and text()='Salvar']")))
    buton.click()

    time.sleep(5)
    
    break