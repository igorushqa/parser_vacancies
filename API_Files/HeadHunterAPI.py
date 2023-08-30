import requests
from API_Files.AbstractClassAPI import AbstractClass


class HeadHunterAPI(AbstractClass):
    """
    Класс для получения данных с HeadHunter
    """
    def __init__(self):
        self.api_data = ''
        self.required_vacation = ''

    def get_remote_data(self, url, params, **kwargs):
        response = requests.get(url, params=params)
        return response

    def get_vacancies(self, keyword) -> list[dict]:
        """
        Возвращает список с ваканcиями HeadHunter по ключевому слову
        """
        self.required_vacation = keyword
        vacancies_hh = []
        current_page = 0
        url = "https://api.hh.ru/vacancies"
        params = {
            "search_field": "name",
            "text": keyword,
            "page": current_page,
            "per_page": 100}
        start = 1
        count = 0
        while_count = 1
        while while_count:
            data = self.get_remote_data(url, params=params).json()
            if start:
                num_of_vacancies = data["found"]
                if num_of_vacancies == 0:
                    print('Нет таких вакансий на HeadHunter')
                start = 0
                while_count = 0
            vacancies_data = data["items"]
            for i in range(len(vacancies_data)):
                try:
                    vacancies_hh += [{
                        "name": vacancies_data[i]["name"],
                        "vacancy_id": vacancies_data[i]["id"],
                        "source": "hh.ru",
                        "salary_from": vacancies_data[i]["salary"]["from"],
                        "salary_to": vacancies_data[i]["salary"]["to"],
                        "salary_avg": self.salary_avg(vacancies_data[i]["salary"]["from"],
                                                      vacancies_data[i]["salary"]["to"]),
                        "url": vacancies_data[i]["alternate_url"],
                        "area": vacancies_data[i]["area"]["name"]
                    }]
                except TypeError:
                    vacancies_hh += [{
                        "name": vacancies_data[i]["name"],
                        "vacancy_id": vacancies_data[i]["id"],
                        "source": "hh.ru",
                        "salary_from": "0",
                        "salary_to": "0",
                        "salary_avg": "0",
                        "url": vacancies_data[i]["alternate_url"],
                        "area": vacancies_data[i]["area"]["name"]
                    }]
            if count + 1 == int(data["pages"]):
                while_count = 0
                print("цикл проверки HeadHunter закончен, вакансии найдены")
            count += 1
            current_page += 1
        self.api_data = vacancies_hh
        return vacancies_hh


