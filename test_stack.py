from stack import Stack
import pytest
import unittest
import untested

class TestStackInit(unittest.TestCase):
    def test_init(self):
        self.assertEqual(len(Stack(data=[0,1,2])), 3)
        
    def test_init_none(self):
        self.assertEqual(len(Stack()), 0)
        
    def test_init_except(self):
        with self.assertRaises(TypeError):
            Stack(1)
            
class TestStackMethods(unittest.TestCase):
    
    # def setUp(self) -> None:
    #    self.stack = Stack()
       
    def test_add(self):
        stack = Stack()
        stack.add(1)
        self.assertEqual(len(stack), 1)
        stack.add(2)
        self.assertEqual(len(stack), 2)
        
    def test_peek(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()
        item = 3
        stack.add(item)
        length_before = 1
        self.assertEqual(stack.peek(), item)
        self.assertEqual(len(stack), length_before)
    
    def test_pop(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        items = [1, 2, 3, 4, 5]
        stack = Stack(data=items)
        self.assertEqual(stack.pop(), items[-1])
        self.assertEqual(stack.pop(), items[-2])
        self.assertEqual(len(stack), 3)
        
    def test_isEmpty(self):
        stack = Stack()
        self.assertFalse(stack.isEmpty()) # Broke intentionally
        stack.add(1)
        self.assertFalse(stack.isEmpty())
        
