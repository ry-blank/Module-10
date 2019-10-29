import unittest
from class_definitions import student_class as sc


class MyStudentClass(unittest.TestCase):
    def setUp(self):
        self.student = sc.Student('Blankenship', 'Ryan', 'Web Development', 2.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Blankenship')
        self.assertEqual(self.student.first_name, 'Ryan')

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name, 'Blankenship')
        self.assertEqual(self.student.first_name, 'Ryan')
        self.assertEqual(self.student.major, 'Web Development')
        self.assertEqual(self.student.gpa, 2.0)


if __name__ == '__main__':
    unittest.main()
