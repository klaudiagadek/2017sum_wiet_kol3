import unittest
from FlightSimulator import FlightSimulator
from Generator import Generator

#klaudiagadek tests
class MyTest(unittest.TestCase):
    def setUp(self):
        self.angle = 35
        self.test_instance = FlightSimulator(self.angle)
        self.generator_instance = Generator(self.test_instance)

    def test_correct_angle(self):
        new_angle = self.test_instance.correct_angle()
        self.assertEqual(new_angle, self.test_instance.angle)

    def test_correct_angle_else(self):
        self.test_instance.angle = 150
        new_angle = self.test_instance.correct_angle()
        self.assertEqual(new_angle, self.test_instance.angle % self.test_instance.max_angle)

    def test_correct_angle_new_max_angle(self):
        self.test_instance.max_angle = 130
        self.test_instance.angle = 150
        new_angle = self.test_instance.correct_angle()
        self.assertEqual(new_angle, self.test_instance.angle % self.test_instance.max_angle)

    def test_correct_angle_less(self):
        self.test_instance.angle = 550
        new_angle = self.test_instance.correct_angle()
        self.assertLess(new_angle, 360)

    def test_draw_angle_less(self):
        new_angle = self.test_instance.draw_angle()
        self.assertLess(new_angle, 360)

    def test_correct_angle_another_test_instance(self):
        self.test_instance2 = FlightSimulator('150')
        new_angle = self.test_instance2.correct_angle()
        self.assertNotEqual(new_angle, self.test_instance2.angle)

    def test_correct_angle_another_test_instance_Equal(self):
        self.test_instance2 = FlightSimulator('150')
        new_angle = self.test_instance2.correct_angle()
        self.assertEqual(new_angle, self.test_instance2.angle % self.test_instance2.max_angle)
    #
    # def test_correct_angle_another_test_instance_Equal(self):
    #     self.assertEqual(new_angle, FlightSimulator('alaa'))
    #
    def test_draw_angle_false(self):
        old_angle = self.test_instance.angle
        new_angle = self.test_instance.draw_angle()
        self.assertNotEqual(new_angle, old_angle)

    def test_generator(self):
        old_angle = self.test_instance.angle
        new_angle = Generator(self.test_instance).next()
        self.assertNotEqual(new_angle, old_angle)

if __name__ == '__main__':
    unittest.main()
