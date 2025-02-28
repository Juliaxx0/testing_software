class Patient:

    def __init__(self, name, year_birth, is_healthy):
        self.name = name
        self.year_birth = year_birth
        self.is_healthy = is_healthy

    def age_category_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Взрослый'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Пожилой'

    def health_status_define(self):
        if self.is_healthy:
            return 'Здоров'
        return 'Болен'

    def show_patient(self):
        return (
            f'{self.name}, '
            f'возраст: {self.age_category_define()}, '
            f'статус: {self.health_status_define()}'
        )


if __name__ == '__main__':
    # Создайте экземпляр класса Patient с необходимыми параметрами.
    # Например, test_old_unhealthy = Patient('Иванов', 1940, False).
    test_old_unhealthy = Patient('Иванов', 1940, False)

    # Напишите assert и в нём проверьте,
    # что метод health_status_define() этого экземпляра возвращает строку "Болен".
    # Во втором assert проверьте, возвращает ли метод age_category_define() значение "Пожилой".
    assert test_old_unhealthy.health_status_define() == 'Болен', (
        'Метод health_status_define работает некорректно'
    )

    assert test_old_unhealthy.age_category_define() == 'Пожилой', (
        'Метод age_category_define работает некорректно'
    )

    # Создайте новый экземпляр с другими параметрами;
    # через assert проверьте, вернут ли и его методы ожидаемый результат.
    test_old_healthy = Patient('Иванов', 1940, True)

    assert test_old_healthy.health_status_define() == 'Здоров', (
        'Метод health_status_define работает некорректно'
    )

    assert test_old_healthy.age_category_define() == 'Пожилой', (
        'Метод age_category_define работает некорректно'
    )

    # Создайте столько экземпляров, сколько нужно,
    # чтобы через разные assert проверить все методы во всех вариантах.
    test_young_unhealthy = Patient('Сергеев', 2000, False)

    assert test_young_unhealthy.health_status_define() == 'Болен', (
        'Метод health_status_define работает некорректно'
    )

    assert test_young_unhealthy.age_category_define() == 'Молодой', (
        'Метод age_category_define работает некорректно'
    )

    test_young_healthy = Patient('Сергеев', 2000, True)

    assert test_young_healthy.health_status_define() == 'Здоров', (
        'Метод health_status_define работает некорректно'
    )

    assert test_young_healthy.age_category_define() == 'Молодой', (
        'Метод age_category_define работает некорректно'
    )

    test_adult_unhealthy = Patient('Петров', 1949, False)

    assert test_adult_unhealthy.health_status_define() == 'Болен', (
        'Метод health_status_define работает некорректно'
    )

    assert test_adult_unhealthy.age_category_define() == 'Взрослый', (
        'Метод age_category_define работает некорректно'
    )

    test_adult_healthy = Patient('Петров', 1949, True)

    assert test_adult_healthy.health_status_define() == 'Здоров', (
        'Метод health_status_define работает некорректно'
    )

    assert test_adult_healthy.age_category_define() == 'Взрослый', (
        'Метод age_category_define работает некорректно'
    )
