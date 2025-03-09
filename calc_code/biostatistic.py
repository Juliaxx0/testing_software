import scipy.stats as stats
import numpy as np

class Calculation_Biostatistic():

    def __init__(self):
        
        self.result = {}
    
    def binomial_confidence(
        self,
        num_successes: float,
        num_all: float,
        significance_level: float = 0.05
    ) -> dict:
        '''
        Программа расчета доверительных границ 
        к частоте (на основе биномиального распределения)
        num_all: Число наблюдений
        num_successes: Число успехов
        significance_level: уровень значимости
        '''
        if num_all == 0:
            raise ZeroDivisionError('Не могу делить на ноль')
        frequency =  num_successes / num_all
        significance = stats.norm.ppf(1 - significance_level / 2)
        border = significance * np.sqrt((frequency * (1 - frequency)) / num_all)
        upper_bound = min(1, (frequency + border))
        lower_bound = max(0, (frequency - border))
        error_rate_plus = upper_bound - frequency
        error_rate_minus = frequency - lower_bound
        self.result.update(
            {'frequency': frequency,
             'lower_bound': lower_bound,
             'upper_bound': upper_bound,
             'error_rate_plus': error_rate_plus,
             'error_rate_minus': error_rate_minus}
        )
        return self.result

    def poisson_confidence_interval(self, event: float,
                                    confidence: float = 0.95) -> dict:
        """
        Вычисление доверительного интервала Пуассона.

        :param event: Наблюдаемое значение (среднее число событий)
        :param confidence: Уровень доверия, например, 0.95 для 95%.
        :return: (lower_bound, upper_bound) - Доверительные границы.
        """
        if event is None or confidence is None:
            return None
        if event < 0:
            raise ValueError("'event' должно быть больше или равно нулю.")
        if not (0 < confidence < 1):
            raise ValueError("'confidence' должно быть в диапазоне (0, 1).")
        alpha = 1 - confidence
        lower_bound = stats.poisson.ppf(alpha / 2, event)
        upper_bound = stats.poisson.ppf(1 - alpha / 2, event)
        self.result.update(
            {'lower_bound': lower_bound,
             'upper_bound': upper_bound}
        )
        return self.result
