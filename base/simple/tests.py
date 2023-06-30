from django.test import TestCase


class TestSimple(TestCase):
    def test_main(self):
        response = self.client.get('/')  # получаем ответ браузера
        self.assertEquals(response.status_code, 200)  # простая проверка кода ответа

    def test_main_contains(self):
        response = self.client.get('/')  # получаем ответ браузера
        self.assertIn('My message', response.content.decode())  #  получаем контент в байтах и декодируем в строку