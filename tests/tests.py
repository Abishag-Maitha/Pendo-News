from models import Source, Article
import unittest

class SourceTest(unittest.TestCase):
    '''Testcase to test the Source Class'''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("name","description","url" )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

class ArticleTest(unittest.TestCase):
    '''Testcase to test the Source Class'''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Article("","","","","","")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Article))


if __name__ == '__main__':
    unittest.main()