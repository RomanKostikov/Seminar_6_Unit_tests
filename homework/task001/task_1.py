"""Программа для сравнения средних значений двух списков."""
from __future__ import annotations


class NumsLists:
    """Класс для сравнения средних значений двух списков."""

    def __init__(self, lst1: list[int | float], lst2: list[int | float]):
        """
        Инициализирует экземпляр класса двумя списками.

        Параметры:
            lst1 (list[int | float]): Первый список.
            lst2 (list[int | float]): Второй список.
        """
        self.lst1 = lst1
        self.lst2 = lst2

    def get_lists_averages(self) -> tuple[float, float]:
        """
        Вычисляет и возвращает средние значения двух списков.

        Возвращает:
            tuple[float, float]: Кортеж, содержащий среднее значение `lst1` и `lst2`.
        """
        avg1 = 0
        if self.lst1:
            avg1 = sum(self.lst1) / len(self.lst1)

        avg2 = 0
        if self.lst2:
            avg2 = sum(self.lst2) / len(self.lst2)

        return avg1, avg2

    def compare_averages(self) -> None:
        """
        Сравнивает средние значения двух списков и выводит результат.

        Этот метод вычисляет средние значения двух списков с помощью метода `get_lists_averages`
        и сравнивает их. Если среднее значение первого списка больше среднего значения второго
        списка, он выводит 'Первый список имеет большее среднее значение'. Если среднее значение
        первого списка меньше среднего значения второго списка, он выводит 'Второй список имеет
        большее среднее значение'. Если средние значения равны, он выводит 'Средние значения равны'.

        Параметры:
            self (ClassName): Экземпляр класса.

        Возвращает:
            None: Этот метод ничего не возвращает.
        """
        avg1, avg2 = self.get_lists_averages()
        if avg1 > avg2:
            print('Первый список имеет большее среднее значение.')
        elif avg1 < avg2:
            print('Второй список имеет большее среднее значение.')
        else:
            print('Средние значения равны.')

# def main():
#     # Create an instance of NumsLists
#     num_lists = NumsLists([1, 2, 3], [4, 5, 6])
#
#     # Get the averages of the lists
#     averages = num_lists.get_lists_averages()
#
#     # Print the averages
#     print(f"The average of list 1 is: {averages[0]}")
#     print(f"The average of list 2 is: {averages[1]}")
#     # Call the compare_averages method
#     num_lists.compare_averages()
#
#
# if __name__ == "__main__":
#     main()
