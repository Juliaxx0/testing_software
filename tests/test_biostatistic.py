import unittest
from calc_code.biostatistic import Calculation_Biostatistic

class TestCalc(unittest.TestCase):
    """Тестируем Calculation_Biostatistic."""

    @classmethod
    def setUpClass(cls):
        """Подготовка прогона теста. Вызывается перед каждым тестом."""
        # Arrange - подготавливаем данные для каждого теста.
        cls.calc = Calculation_Biostatistic()

    def test_one(self):
        res = self.calc.binomial_confidence(50, 100)
        self.assertIsInstance(res, dict)
    
    def test_two(self):
        res = self.calc.poisson_confidence_interval(0.67)
        self.assertIsInstance(res, dict)