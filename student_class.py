"""
Program: unit_tests_for_a_class_assignment
Author: Ryan Blankenship
Last date modified: 10/28/2019

The purpose of this program is to demonstrate
 unit testing for classes.
"""


class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname)
                and name_characters.issuperset(fname)
                and name_characters.issuperset(major)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + \
               " has major " + self.major + " with gpa: " + str(self.gpa)
