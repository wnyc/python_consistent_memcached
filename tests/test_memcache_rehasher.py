import unittest

from memcached_rehasher import make_consistent_for_modulus

class TestSimpleCases(unittest.TestCase):
    def test_3(self):
        hosts = list('abc')
        hash = make_consistent_for_modulus(hosts, slots=3)
        
        for host in hosts:
            self.assertTrue(host in hash)
        
    
    
