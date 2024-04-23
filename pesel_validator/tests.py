from django.test import TestCase
from datetime import datetime
from .utils import check_control_digit, get_pesel_data

class UtilsTestCase(TestCase):
    def test_check_control_digit_valid(self):
        pesels = ['70040498246',
                '81030825146',
                '68120223275',
                '67070416144',
                '62020838751',
                '54052523376',
                '51010769771',
                '59073181196',
                '93081931569',
                '91091261313',
                ]
        for pesel in pesels:
            self.assertTrue(check_control_digit(pesel))

    def test_check_control_digit_invalid(self):
        pesels = ['70040498244',
                '81030825142',
                '68120223273',
                '67070416145',
                '62020838755',
                '54052523378',
                '51010769772',
                '59073181199',
                '93081931568',
                '91091261312',
                ]
        for pesel in pesels:
            self.assertFalse(check_control_digit(pesel))

    def test_get_pesel_data_old_woman(self):
        pesel = '02070803628'
        expected_result = ('02070803628', datetime(1902, 7, 8).date(), 'K')
        self.assertEqual(get_pesel_data(pesel), expected_result)

    def test_get_pesel_data_new_men(self):
        pesel = '00220325697'
        expected_result = ('00220325697', datetime(2000, 2, 3).date(), 'M')
        self.assertEqual(get_pesel_data(pesel), expected_result)
