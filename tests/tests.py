import unittest

from main import start_stream


class MyTestCase(unittest.TestCase):

    def test_correct_behavior(self):
        start_stream('tests/correct_input')
        result = self.read_output()

        self.assertEqual(['ES1r2o3', 'RL1u3y2w6'], result)

    def test_order(self):
        start_stream('tests/input_for_test_order')

        result = self.read_output()

        self.assertEqual(['BL2u1e1y1h5', 'AS3r2t5'], result)

    @staticmethod
    def read_output(file='output'):
        result = []
        with open(file, 'r') as f:
            for i in f.readlines():
                result.append(i.replace('\n', ''))

        # BAD CLEARING OUTPUT FILE
        with open(file, 'w') as f:
            pass

        return result


if __name__ == '__main__':
    unittest.main()
