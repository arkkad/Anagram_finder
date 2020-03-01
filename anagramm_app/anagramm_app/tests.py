import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_dict_creating(self):
        data = {'["foobar", "aabb", "baba", "boofar", "живу", "вижу", "AbbA", "BaBa", "test"]': ''}
        response = self.client.post('/load', data)
        self.assertEqual(response.status_code, 200)

    def test_words(self):
        response_foobar = self.client.get('/get?word=foobar')
        self.assertEqual(response_foobar.content, b'[\'foobar\', \'boofar\']')
        self.assertEqual(response_foobar.status_code, 200)

        response_raboof = self.client.get('/get?word=raboof')
        self.assertEqual(response_raboof.content, b'[\'foobar\', \'boofar\']')
        self.assertEqual(response_raboof.status_code, 200)

        response_abba = self.client.get('/get?word=abba')
        self.assertEqual(response_abba.content,
                         b'[\'aabb\', \'baba\', \'AbbA\', \'BaBa\']')
        self.assertEqual(response_abba.status_code, 200)

        response_test = self.client.get('/get?word=test')
        self.assertEqual(response_test.content,
                         b'[\'test\']')
        self.assertEqual(response_test.status_code, 200)

        response_qwerty = self.client.get('/get?word=qwerty')
        self.assertEqual(response_qwerty.content, b'null')
        self.assertEqual(response_qwerty.status_code, 200)

        response1 = self.client.get('/get?word=живу')
        self.assertEqual(response1.content,
                         b'[\'\xd0\xb6\xd0\xb8\xd0\xb2\xd1\x83\', \'\xd0\xb2\xd0\xb8\xd0\xb6\xd1\x83\']')
        self.assertEqual(response1.status_code, 200)

    def test_details(self):
        response = self.client.get('/clear')
        self.assertEqual(response.status_code, 200)
