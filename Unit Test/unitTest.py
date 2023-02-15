#LETS GET IT!!!!!!
#run terminal with 
#run terminal in git bash with python -m unittest unitTest.py

import unittest
from Student import Assignment, Student, Event
from testData import ASSIGNMENTS, EVENTS, MATTHEW_POGUE

class TestAssignment(unittest.TestCase):
   def test_getPercentage(self):
    for eachAssignment in range(len(ASSIGNMENTS)):
        assignment = Assignment(
            ASSIGNMENTS[eachAssignment]['name'],
            ASSIGNMENTS[eachAssignment]['points'],
            ASSIGNMENTS[eachAssignment]['maxPoints']
        )
        percentage = (assignment.points / assignment.maxPoints) * 100
        expected_percentage = ASSIGNMENTS[eachAssignment]['points'] / ASSIGNMENTS[eachAssignment]['maxPoints'] * 100
        self.assertEqual(expected_percentage, percentage)


class TestStudent(unittest.TestCase):
    def setUp(self):
        # Creating a student and adding some events and assignments to their record
        self.student = Student('Matthew Pogue', 'h735f787', 'alex', [], ASSIGNMENTS)
        self.events = [Event(event['title'], event['eventType'], event['entryFee']) for event in EVENTS]
        self.student.addEvent(self.events)

        #                                               addEvent Unit test
    def test_addEvent(self):
        # Add a new event to the student's record and assert that it's in the record
        expected_event = self.events[2]
        self.student.addEvent([expected_event])
        self.assertIn(expected_event, self.student.events)

        #                                               countEvents test
    def test_countEvents(self):
        # Count the number of meetings in the student's record
        expected_count = sum(event.eventType == 'meeting' for event in self.student.events)
        actual_count = self.student.countMeetings()
        self.assertEqual(actual_count, expected_count)

        #                                               getGrade test
    def test_getGrade(self):
        # Add some assignments to the student's record
        self.student.assignments = [Assignment(**assignment) for assignment in ASSIGNMENTS]

        # Calculate the expected grade
        total_points = sum(assignment.points for assignment in self.student.assignments)
        max_points = sum(assignment.maxPoints for assignment in self.student.assignments)
        expected_grade = round(total_points / max_points, 1)

        # check the actual grade from the student object
        actual_grade = round(self.student.getGrade(), 1)
        self.assertEqual(actual_grade, expected_grade)

        #                                               getLetterGrade test
    def test_getLetterGrade(self):
        # Add some assignments to the student's record
        self.student.assignments = [Assignment(**assignment) for assignment in ASSIGNMENTS]

        # Calculate the expected letter grade
        total_points = sum(assignment.points for assignment in self.student.assignments)
        max_points = sum(assignment.maxPoints for assignment in self.student.assignments)
        expected_grade = round(total_points / max_points, 1)
        expected_letter_grade = 'F'
        if expected_grade >= .6 and expected_grade < .7:
            expected_letter_grade = 'D'
        elif expected_grade >= .7 and expected_grade < .8:
            expected_letter_grade = 'C'
        elif expected_grade >= .8 and expected_grade < .9:
            expected_letter_grade = 'B'
        elif expected_grade >= .9 and expected_grade < 1:
            expected_letter_grade = 'A'
        elif expected_grade == 1:
            expected_letter_grade = 'A+'

        # Check the actual letter grade from the student object
        actual_letter_grade = self.student.getLetterGrade(expected_grade)
        self.assertEqual(actual_letter_grade, expected_letter_grade)

        

         

