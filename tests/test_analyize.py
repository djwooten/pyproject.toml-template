import subprocess
import unittest


from mypackage import analyze


class TestAnalyzeCLI(unittest.TestCase):
    """Test the command line interface of analyze.py"""
    @classmethod
    def setUpClass(cls):
        path = analyze.__file__
        cls._base_cmd = ['python', path]

    @classmethod
    def _build_cmd(cls, args):
        """Call `python /path/to/analyze.py args`"""
        return cls._base_cmd + args.split()

    def test_average(self):
        """Makes sure cli calculates average correctly"""
        cmd = self._build_cmd('-f average 2 4 5')
        result = subprocess.check_output(cmd)
        self.assertAlmostEqual(float(result), (2+4+5)/3.0)

    def test_median(self):
        """Makes sure cli calculates average correctly"""
        cmd = self._build_cmd('-f median 2 4 5')
        result = subprocess.check_output(cmd)
        self.assertAlmostEqual(float(result), 4)

    def test_exit_on_missing_fucn(self):
        """Makes sure it returns non-zero exit code on failures"""
        cmd = self._build_cmd('2 4 5')
        code = subprocess.call(cmd)
        self.assertNotEqual(code, 0, "Exit status {} should not be 0"
                                     .format(code))

    def test_exit_on_missing_values(self):
        """Makes sure it returns non-zero exit code on failures"""
        cmd = self._build_cmd('-f median')
        code = subprocess.call(cmd)
        self.assertNotEqual(code, 0, "Exit status {} should not be 0"
                                     .format(code))

    def test_sure_to_fail(self):
        """this will totally fail"""
        self.assertTrue(False)
