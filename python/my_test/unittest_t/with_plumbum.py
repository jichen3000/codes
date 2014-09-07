import unittest
import random

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def _print_out_failed_result(self):
        print
        print (' Got expected Error when testing %s ' % self._testMethodName).center(80, '=')
        # print self.out.strip()
        print '='*80

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        self.assertEqual('jc','jc1')
        # self._print_out_failed_result()
        # print self._testMethodName

        # should raise an exception for an immutable sequence
        # print random.shuffle((1,2,3))
        # self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
    @classmethod
    def self_run(cls):
        suite = unittest.TestLoader().loadTestsFromTestCase(cls)
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    import plumbum
    import sys
    from minitest import *

    print "in main"

    python_run = plumbum.local['python']
    test_method = ['unittest_t/with_plumbum.py', 'TestSequenceFunctions.%s' % sys.argv[-1]]
    test_method.p()
    python_run[test_method] & plumbum.FG

    # import sys
    # from plumbum import local, FG

    # python = local['python']
    # python = python['-m', 'unittest', '-v']
    # test_case = 'apollo.websvcs.swdownload.swdclient.test.test_integration.TestSwClientDaemon.%s' % sys.argv[-1]
    # python[test_case] & FG    
