from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# Configurar el servicio del ChromeDriver
service = Service('/Users/arielorozco/code/chrome/chromedriver')
options = Options()

# Inicializar el WebDriver
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.wikipedia.org')


# Test Case 1: Verificar que el título de la página principal es correcto
def test_homepage_title():
    assert "Wikipedia" in driver.title
    print("Test Case 1 Passed: Homepage title is correct")


# Test Case 2: Buscar un término y verificar que la página de resultados muestra el término buscado
def test_search_function():
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Automation")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Esperar a que la página cargue
    assert "Automation" in driver.page_source
    driver.back()  # Regresar a la página principal
    print("Test Case 2 Passed: Search function works correctly")


# Test Case 3: Verificar que el enlace "Wikispecies" en el pie de página redirige correctamente
def test_footer_species_link():
    # Esperar a que el enlace esté presente
    wikispecies_link = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (By.XPATH, "//a[@class='other-project-link' and contains(@href, 'species.wikimedia.org')]"))
    )
    wikispecies_link.click()
    time.sleep(2)  # Esperar a que la página cargue
    assert "Wikispecies" in driver.page_source
    driver.back()  # Regresar a la página principal
    print("Test Case 3 Passed: Wikispecies link redirects correctly")


# Test Case 4: Verificar que se puede cambiar el idioma de la página
def test_change_language():
    language_link = driver.find_element(By.ID, "js-link-box-es")
    language_link.click()
    time.sleep(2)  # Esperar a que la página cargue
    assert "Wikipedia, la enciclopedia libre" in driver.title
    driver.back()  # Regresar a la página principal
    print("Test Case 4 Passed: Language can be changed")


# Test Case 5: Verificar que el enlace a donaciones lleva a la página correcta
def test_donation_link():
    # Esperar a que el enlace esté presente
    donations_link = WebDriverWait(driver, 5).until(
        ec.presence_of_element_located(
            (By.XPATH, "//a[contains(@href, 'donate.wikimedia.org')]"))
    )
    donations_link.click()
    # Cambiar a la nueva pestaña
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)  # Esperar a que la página cargue
    assert "Make your donation now" in driver.title
    driver.close()  # Cerrar la pestaña de donaciones
    driver.switch_to.window(driver.window_handles[0])  # Volver a la pestaña principal
    print("Test Case 5 Passed: Donate link works correctly")


# Test Case 6: Verificar que el link del App Store funciona correctamente
def test_app_store_link():
    # Esperar a que el enlace esté presente
    app_store = WebDriverWait(driver, 5).until(
        ec.presence_of_element_located(
            (By.XPATH, "//a[contains(@href, 'itunes.apple.com')]"))
    )
    app_store.click()
    # Cambiar a la nueva pestaña
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)  # Aumentar el tiempo de espera para asegurar que la página cargue completamente
    assert "app" in driver.page_source
    driver.close()  # Cerrar la pestaña del App Store
    driver.switch_to.window(driver.window_handles[0])  # Volver a la pestaña principal
    print("Test Case 6 Passed: App Store link works correctly")


# Ejecutar los casos de prueba
test_homepage_title()
test_search_function()
test_footer_species_link()
test_change_language()
test_donation_link()
test_app_store_link()

# Cerrar el WebDriver
driver.quit()
