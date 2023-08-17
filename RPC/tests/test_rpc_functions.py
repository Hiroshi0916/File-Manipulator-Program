import unittest
import sys

sys.path.append('..')
from rpc_server import floor, nroot, reverse, validAnagram, sort

class TestRPCFunctions(unittest.TestCase):

    def test_floor(self):
        self.assertEqual(floor(3.6), 3)
        print("floor function passed")
        self.assertEqual(floor(-3.6), -4)

    def test_nroot(self):
        self.assertAlmostEqual(nroot(2, 4), 2)
        print("nroot function passed")
        self.assertAlmostEqual(nroot(3, 27), 3)

    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")
        print("reverse function passed")

    def test_validAnagram(self):
        self.assertTrue(validAnagram("listen", "silent"))
        print("validAnagram function passed")
        self.assertFalse(validAnagram("hello", "world"))

    def test_sort(self):
        self.assertEqual(sort(["banana", "apple", "cherry"]), ["apple", "banana", "cherry"])
        print("sort function passed")
        
# カスタムテストランナーを定義します。
class CustomTextTestRunner(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        # エラーや失敗がない場合、カスタムの出力を非表示にします。
        if not result.failures and not result.errors:
            self.stream.write("\n")
        return result
    
if __name__ == '__main__':
    unittest.main()
