
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a_1,b_2,c_3):
    """classification of triangle"""
    # require that the input values be >= 0 and <= 200
    if a_1 > (200 or 0) or b_2 > (200 or 0) or c_3 > (200 or 0):
        return 'InvalidInput'
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a_1 >= (b_2 + c_3)) or (b_2 >= (a_1+ c_3)) or (c_3 >= (a_1 + b_2)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if a_1 == b_2 and b_2 == c_3 and c_3==a_1:
        return 'Equilateral'
    if (((a_1 * a_1) + (b_2 *b_2)) == (c_3 * c_3)) or \
            (((b_2*b_2) + (c_3*c_3)) == (a_1*a_1)) or \
            (((a_1*a_1) + (c_3*c_3)) == (b_2*b_2)):
        return 'Right'
    if (a_1 != b_2) and  (b_2 != c_3) and (c_3 != a_1):
        return 'Scalene'
    return 'Isoceles'
