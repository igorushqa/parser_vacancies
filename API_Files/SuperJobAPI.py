from abc import ABC

import requests
from API_Files.AbstractClassAPI import AbstractClass


class SuperJobAPI(AbstractClass, ABC):
    """
    Класс для получения данных с SuperJob
    """
    def __init__(self):
        self.api_data = ''
        self.required_vacation = ''

    def get_remote_data(self, url, params, headers):
        response = requests.get(url, headers=headers, params=params)
        return response

    def get_vacancies(self, keyword) -> list[dict]:
        """
        Возвращает список с ваканcиями SuperJob по ключевому слову
        """
        self.required_vacation = keyword
        vacancies_sj = []
        current_page = 0
        pages_number = 1
        url = "https://api.superjob.ru/2.0/vacancies/"
        headers = {
            "X-Api-App-Id":
                "v3.r.137775982.96e04a316545c64a45907f2b3d042b985abd6555.6a2efa2ebbefa66ae2697c536423324e9cf67020"}
        params = {
            "keyword": keyword,
            "page": current_page,
            "count": 100}
        start = 1
        count = 0
        while_count = 1
        while while_count:
            data = self.get_remote_data(url, headers=headers, params=params).json()
            if start:
                num_of_vacancies = data["total"]
                pages_number = num_of_vacancies // 100
                if num_of_vacancies == 0:
                    print('Нет таких вакансий на SuperJob')
                start = 0
                while_count = 0
            vacancies_data = data["objects"]
            for i in range(len(vacancies_data)):
                vacancies_sj += [{
                    "name": vacancies_data[i]["profession"],
                    "vacancy_id": vacancies_data[i]["id"],
                    "source": "sj.ru",
                    "salary_from": vacancies_data[i]["payment_from"],
                    "salary_to": vacancies_data[i]["payment_to"],
                    "salary_avg": self.salary_avg(vacancies_data[i]["payment_from"],
                                                  vacancies_data[i]["payment_to"]),
                    "url": vacancies_data[i]["link"],
                    "area": vacancies_data[i]["town"]["title"]
                }]
            if count + 1 == pages_number:
                while_count = 0
                print("цикл проверки SuperJob закончен, вакансии найдены")
            count += 1
            current_page += 1
        self.api_data = vacancies_sj
        return vacancies_sj
