import json
import unittest
from StringIO import StringIO

from gwlfe import gwlfe, Parser


class TestGMSWriter(unittest.TestCase):
    def test_gms_writer(self):
        """
        Test that GmsWriter is able to replicate the sample GMS created
        from MapShed.
        """
        input_file = open('unittests/input_4.gms', 'r')
        z = Parser.GmsReader(input_file).read()

        output = StringIO()
        writer = Parser.GmsWriter(output)
        writer.write(z)

        ground_truth = open('input_4.gmsout', 'r')
        output.seek(0)

        self.assertGmsEqual(ground_truth, output)

    def assertGmsEqual(self, gms1, gms2):
        """
        Assert that 2 GMS files match.
        """
        left = Parser.iterate_csv_values(gms1)
        right = Parser.iterate_csv_values(gms2)

        done = False
        counter = 0
        while not done:
            print(counter)
            try:
                a, y1, x1 = left.next()
            except StopIteration:
                done = True

            try:
                b, y2, x2 = right.next()
            except StopIteration:
                if done:
                    # The first file must have ended.
                    continue
                else:
                    self.fail('GMS files did not end at the same time')

            if done:
                # The first file must have ended, but the second file didn't.
                self.fail('GMS files did not end at the same time')

            self.assertEqual(y1, y2)
            self.assertEqual(x1, x2)
            self.assertEqualFuzzy(a, b)
            counter += 1

    def assertEqualFuzzy(self, a, b):
        """
        Assert that 2 values match. The purpose of doing a fuzzy comparison
        is to ignore slight formatting differences between VB and Python.
        """
        # Test that floats like ".06" match "0.06".
        try:
            f1 = float(a)
            f2 = float(b)
            self.assertEqual(f1, f2)
            return
        except ValueError:
            pass
        self.assertEqual(a, b)
