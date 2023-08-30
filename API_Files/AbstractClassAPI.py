from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def get_remote_data(self, url, params, headers):
        pass

    @abstractmethod
    def get_vacancies(self, keyword) -> list[dict]:
        pass

    @staticmethod
    def salary_avg(a, b):
        """
        метод определения средней зар.платы
        """
        if a != 0 and b != 0:
            return (a + b) / 2
        elif a != 0 and b == 0:
            return a
        elif a == 0 and b == 0:
            return "0"
        else:
            return b
