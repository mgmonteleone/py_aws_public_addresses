import unittest
import awspublicranges

class test_public_ranges(unittest.TestCase):
    def test_01_object_create(self):
        out = awspublicranges.AwsIpRanges()
        self.assertIsInstance(out,awspublicranges.AwsIpRanges)


if __name__ == '__main__':
    unittest.main()
