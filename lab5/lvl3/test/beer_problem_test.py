import unittest

from lab5.lvl3.src.beer_problem import beer_problem_answer


class BeerProblemTest(unittest.TestCase):

    def test_from_task(self):
        num_people = 6
        num_beer_type = 3
        beer_pref = ["YNN", "YNY", "YNY", "NYY", "NYY", "NYN"]
        self.assertEqual(beer_problem_answer(num_people, num_beer_type, beer_pref), 2)

    def test_form_task_2(self):
        num_people = 2
        num_beer_type = 2
        beer_pref = ["YN", "NY"]
        self.assertEqual(beer_problem_answer(num_people, num_beer_type, beer_pref), 2)

    def test_case(self):
        num_people = 7
        num_beer_type = 5
        beer_pref = ["NYNYN", "YYNNN", "YYNNN", "YNYNN", "YNYNN", "YNYNN", "NNYNY"]
        self.assertEqual(beer_problem_answer(num_people, num_beer_type, beer_pref), 2)
