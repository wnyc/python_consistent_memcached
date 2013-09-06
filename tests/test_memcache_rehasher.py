import unittest

from memcached_rehasher import make_consistent_buckets, make_consistent_weighted_buckets

class TestSimpleCases(unittest.TestCase):
    def test_3(self):
        hosts = list('abc')
        hash = make_consistent_buckets(hosts, slots=3)
        
        for host in hosts:
            self.assertTrue(host in hash)
        
    
class TestWeighted(unittest.TestCase):
    def test_3(self):
        hosts = [('a', 3), ('b', 1), ('c', 1)]
        hash = make_consistent_weighted_buckets(hosts, slots=3)
        
        self.assertEquals(hash.count('a'), 3)
        
    
    
