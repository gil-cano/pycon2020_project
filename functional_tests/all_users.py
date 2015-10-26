# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_add_a_track(self):
        # Alicia visita la aplciación
        self.browser.get('http://localhost:8000')

        # ella nota que el titulo y encabezado mencionan pycon 2020
        self.assertIn('Pycon 2020', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Pycon 2020', header_text)

        # ella entra en la seccion de sesiones
        tracks_menu = self.browser.find_element_by_id('tracks')
        tracks_menu.send_keys(Keys.ENTER)

        # ella intenta ingresar una sesion
        newlink = self.browser.find_element_by_id('new_item')
        newlink.send_keys(Keys.ENTER)

        titlebox = self.browser.find_element_by_id('id_title')
        titlebox.send_keys('Lunes')

        placebox = self.browser.find_element_by_id('id_place')
        placebox.send_keys('Salon 5')
        placebox.send_keys(Keys.ENTER)

if __name__ == '__main__':
    unittest.main()
