import unittest
from play import TTT

'''
| Method                    | Checks that          |
|---------------------------|----------------------|
| assertEqual(a, b)         | a == b               |
| assertNotEqual(a, b)      | a != b               |
| assertTrue(x)             | bool(x) is True      |
| assertFalse(x)            | bool(x) is False     |
| assertIs(a, b)            | a is b               |
| assertIsNot(a, b)         | a is not b           |
| assertIsNone(x)           | x is None            |
| assertIsNotNone(x)        | x is not None        |
| assertIn(a, b)            | a in b               |
| assertNotIn(a, b)         | a not in b           |
| assertIsInstance(a, b)    | isinstance(a, b)     |
| assertNotIsInstance(a, b) | not isinstance(a, b) |
'''


class TestPlay(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(1+1, 2, '1+1 = 2')

    def test_overwrite(self):
        #setup
        ttt = TTT(2,3)
        ttt.board = [['x','o','x'],['x','x','o'],['o','x','x']]
        ttt.player = 2
        old_board = ttt.board
        ttt.update_move('B1')
        self.assertEqual(ttt.board,old_board)
    
    def test_next_player(self):
        ttt = TTT(2,3)
        ttt.board = [['x','o','x'],['x','x','o'],['o','x','x']]
        ttt.player = 2
        ttt.next_player()
        self.assertEqual(ttt.player, 1)

if __name__ == '__main__':
    unittest.main()
