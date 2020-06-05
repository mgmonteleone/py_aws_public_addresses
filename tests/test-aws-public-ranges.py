import unittest
from awspublicranges.ranges import AwsIpRanges

class test_public_ranges(unittest.TestCase):
    def test_01_object_create(self):
        out =AwsIpRanges()
        self.assertIsInstance(out,AwsIpRanges)


if __name__ == '__main__':
    unittest.main()
