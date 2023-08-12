import unittest
from fox_hex_utils_ren import *


class FoxHexUtilsTest(unittest.TestCase):

    def test_ubyte_to_hex(self):
        tests = [(0, '00'), (15, '0f'), (240, 'f0'), (255, 'ff')]

        for test in tests:
            val = fox_ubyte_to_hex(test[0])
            self.assertEqual(val, test[1])

        self.assertRaises(Exception, fox_ubyte_to_hex, 256)

    def test_ubytes_to_hex(self):
        input = [0, 15, 240, 255]
        value = fox_ubytes_to_hex(input, '0x', True)
        expect = '0x000FF0FF'

        self.assertEqual(value, expect)

        self.assertRaises(Exception, fox_ubytes_to_hex, 33)

    def test_int_to_hex(self):
        self.assertEqual(fox_int_to_hex(255), 'ff')
        self.assertEqual(fox_int_to_hex(255, 6, '#', True), '#0000FF')
        self.assertEqual(fox_int_to_hex(65535), 'ffff')
        self.assertEqual(fox_int_to_hex(4294967295), 'ffffffff')
        self.assertRaises(Exception, fox_int_to_hex, "hello")
        self.assertRaises(Exception, fox_int_to_hex, -1)
        self.assertRaises(Exception, fox_int_to_hex, 10, -1)
        self.assertEqual(fox_int_to_hex(0, 2), '00')

    def test_hex_to_ubytes(self):
        input = 'FFffFF'
        tests = [255, 255, 255]
        value = fox_hex_to_ubytes(input)

        self.assertEqual(len(value), len(tests))

        for i in range(len(tests)):
            self.assertEqual(value[i], tests[i])

        input = '#FFf00F00'
        tests = [255, 240, 15, 0]
        value = fox_hex_to_ubytes(input, '#')
        self.assertEqual(len(value), len(tests))
        for i in range(len(tests)):
            self.assertEqual(value[i], tests[i])

        self.assertLessEqual(fox_hex_to_ubytes(''), [])

        self.assertRaises(Exception, fox_hex_to_ubytes, 'apples')

    def test_hex_to_int(self):
        input = '0xFFffFFff'
        value = fox_hex_to_int(input, '0x')
        self.assertEqual(value, 4294967295)

        self.assertRaises(Exception, fox_hex_to_int, '')

    def test_hex_is_valid(self):
        self.assertFalse(fox_hex_is_valid(3))
        self.assertFalse(fox_hex_is_valid('apples'))
        self.assertTrue(fox_hex_is_valid('fedcba9876543210'))
