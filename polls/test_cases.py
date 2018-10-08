__author__ = 'johanna gutierres - nestor romero'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('D:\\chromedriver.exe')
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_titulo_1(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('BuscoAyuda', self.browser.title)

    def test_registrar_independiente(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Camilo')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Mojica')

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('5551234')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jc.mojicap@uniandes.edu.co')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('3')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador']").click()

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('D:\\POL03.png')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('jc.mojica')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('password')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Camilo Mojica - Desarrollador"]')
        self.assertIn('Juan Camilo Mojica - Desarrollador', span.text)

    def test_detalle_trabajador(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Camilo Mojica - Desarrollador"]')
        span.click()
        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Camilo Mojica - Desarrollador"]')
        self.assertIn('Juan Camilo Mojica - Desarrollador', h2.text)
