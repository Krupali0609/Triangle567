# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangle(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral','100,100,100 should be equilateral')

    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(5,5,4),'Isoceles','5,5,4 is a Isoceles triangle')

    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(100,100,50),'Isoceles','100,100,50 is a Isoceles triangle')

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(100,150,60),'Scalene','100,150,60 is a Scalene triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(110,123,50),'Scalene','110,123,50 is a Scalene triangle')

    def testScaleneTriangleC(self): 
        self.assertEqual(classifyTriangle(2,4,3),'Scalene','2,4,3 is a Scalene triangle')
    
    def testNotTriangleA(self): 
        self.assertEqual(classifyTriangle(150,100,50),'NotATriangle','150,100,50 cannot form a triangle')

    def testNotTriangleB(self): 
        self.assertEqual(classifyTriangle(150,100,40),'NotATriangle','150,100,40 cannot form a triangle')

    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(250,100,150),'InvalidInput','250,100,150 is an invalid input as values greater than 200')

    def testInvalidInputA1(self): 
        self.assertEqual(classifyTriangle(300,100,250),'InvalidInput','300,100,250 is an invalid input as values greater than 200')
    
    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(0,23,56),'InvalidInput','0,23.56 is an invalid input as ONE value is 0 ')

    def testInvalidInputB1(self): 
        self.assertEqual(classifyTriangle(0,0,56),'InvalidInput','0,0,56 is an invalid input as TWO value is 0 ')

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(1.2,5,6),'InvalidInput','1.2,5,6 is an invalid input as all the values are not integer ')

    def testInvalidInputC1(self): 
        self.assertEqual(classifyTriangle(1.2,5.4,6),'InvalidInput','1.2,5.4,6 is an invalid input as all the values are not integer ')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()