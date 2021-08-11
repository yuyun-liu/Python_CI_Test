import unittest
import app

class TestApp(unittest.TestCase):
    def __init__(self, methodName: str):
        super().__init__(methodName=methodName)

    def test_hellow_world(self):
        self.assertEqual(app.Application.hello_world(), 'Hello World!')
    
    def test_say_hello(self):
        self.assertEqual(app.Application.say_hello(), 'Say Hello!')
    
if __name__ == '__main__':
    unittest.main()
