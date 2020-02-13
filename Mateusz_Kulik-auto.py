from selenium import webdriver
import exrex
import unittest


class SalesTracker(unittest.TestCase):

    def setUp(self) -> None:
        # directing to url
        self.driver = webdriver.Firefox()
        self.driver.get("http://serwer1419259.home.pl/tester/index.php/site/form/52")

    def test_form(self):
        driver = self.driver

        # filling boxes without format
        all_class_boxes = driver.find_elements_by_css_selector('input[type="text"]')

        # filling input boxes with all characters
        for box in all_class_boxes:
            special_char = "aąbc./1@"
            if box.is_displayed():
                box.send_keys(special_char)
                if box.get_attribute('value'):
                    print(f"{box.get_attribute('data-key')}: {special_char}")
                else:
                    test_input = 'Testinput'
                    box.send_keys("Testinput")
                    print(f"{box.get_attribute('data-key')}: {test_input}")

        # pesel regex
        pesel_regex = exrex.getone(r'\d{11}')
        pesel_box = driver.find_element_by_css_selector('input[data-key="pesel"]')
        pesel_box.send_keys(pesel_regex)

        # nip regex
        nip_regex = exrex.getone(r'\d{10}')
        nip_box = driver.find_element_by_css_selector('input[data-key="nip"]')
        nip_box.send_keys(nip_regex)

        # doctor_no regex
        dr_regex = exrex.getone(r'\d{10}')
        dr_box = driver.find_element_by_css_selector('input[data-key="doctor_no"]')
        dr_box.send_keys(dr_regex)

        # phone number regex
        phone_regex = exrex.getone(r'\d{9}')
        phone_box = driver.find_element_by_css_selector('input[data-key="phone"]')
        phone_box.send_keys(phone_regex)

        # post adress regex
        post_regex = exrex.getone(r'\d{2}-\d{3}')
        post_box = driver.find_element_by_css_selector('input[data-key="post_code"]')
        post_box.send_keys(post_regex)

        # email regex
        email_regex = exrex.getone(r'[a-z]{4}\.[a-z]{4}@[a-z]{4}\.[a-z]{3}')
        email_box = driver.find_element_by_css_selector('input[data-key="email"]')
        email_box.send_keys(email_regex)

        # checking checkboxes
        driver.find_element_by_id('id_1_3_2').click()
        driver.find_element_by_id('id_1_5_3').click()
        driver.find_element_by_id('id_1_7_10').click()
        driver.find_element_by_id('id_1_10_12').click()
        driver.find_element_by_id('id_1_11_13').click()
        driver.find_element_by_id('id_2_27_23').click()
        driver.find_element_by_id('id_2_28_31').click()
        driver.find_element_by_id('id_3_32_32').click()
        driver.find_element_by_id('id_3_33_35').click()
        driver.find_element_by_id('id_3_34_37').click()
        driver.find_element_by_id('id_3_36_40').click()
        driver.find_element_by_id('id_3_37_42').click()
        driver.find_element_by_id('id_3_38_44').click()
        driver.find_element_by_id('id_3_39_46').click()

        # filling 'miejsce pracy'
        driver.find_element_by_id('id_2_30').send_keys('Testowe miejsce pracy')

        # sending file
        driver.find_element_by_id('id_1_43').send_keys(r'C:\Users\Mateusz\Desktop\plik_testowy.jpg')

        # sending final form
        driver.find_element_by_css_selector('input[type="submit"').click()

        # asserting test success
        assert 'Formularz został poprawnie zapisany.' in driver.page_source

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


