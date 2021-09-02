from unittest import TestCase
from server import Request


class RequestTestCase(TestCase):
    def test_init_with_valid_path(self):
        req = Request("dog/1")
        self.assertTrue(req.valid)

    def test_init_valid_path_assigns_resource(self):
        req = Request("dog/1")
        self.assertIsNotNone(req.resource)

    def test_init_valid_path_assigns_id(self):
        req = Request("dog/1")
        self.assertIsNotNone(req.id)

    def test_path_must_be_a_string(self):
        with self.assertRaises(TypeError):
            req = Request(1)

    def test_path_has_two_elements(self):
        with self.assertRaises(ValueError):
            req = Request("dog/lover/1")

    def test_path_first_element_is_string(self):
        with self.assertRaises(ValueError):
            req = Request("1/2")

    def test_path_second_element_is_numeric(self):
        with self.assertRaises(ValueError):
            req = Request("dog/lover")
