import unittest
class IntegerArithmeticTestCase(unittest.TestCase):
    def testa(self):  # test method names begin with 'test'
        '''用例说明：aaa'''
        #测试用例要以test开头
        print("aaaaaaaaaa")
        a = "admin"#实际结果
        b = "admin1"#期望结果
        # self.assertTrue(a==b)
        # self.assertTrue(a not in b)
        # self.assertTrue(a!=b)
        # self.assertNotEqual(a,b)
        # self.assertIn(a,b)
        # self.assertNotIn(a,b)
    def testA(self):  # test method names begin with 'test'
        #测试用例要以test开头
        '''用例说明：AAA'''
        print("AAAAAA")
        self.assertEqual((1 + 2), 3)
        # print("hello world")
        self.assertEqual(0 + 1, 1)
    @classmethod#类方法
    def setUpClass(cls):
        print("用例前，只执行一次")
    def test1(self):  # test method names begin with 'test'
        #测试用例要以test开头
        '''用例说明：111'''
        print("1111111111111")
        self.assertEqual((1 + 2), 3)
        # print("hello world")
        self.assertEqual(0 + 1, 1)
    def test2(self):
        '''用例说明：222'''
        print("2222222222")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()
