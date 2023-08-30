import json
from settings import PATH_JSON


class JSONSaver:
    def __init__(self):
        self.vacancies = []

    def save_raw_to_json(self, vacancies_data: list) -> None:
        """
        Запись данных от API или класса Vacancy в файл 'json'
        """
        path_file_json = PATH_JSON
        self.vacancies = vacancies_data
        with open(path_file_json, 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False)
            print(f'Вакансии сохранены в файл {path_file_json}')
        file.close()

    def get_data_from_file(self, path_file_json) -> None:
        """
        Чтение данных из файла с вакансиями
        """
        with open(path_file_json, 'r', encoding='utf-8') as file:  # Открытие файла на чтение
            vacancies_data = json.load(file)    # Чтение данных из файла
            print(f'Загружено {len(list(vacancies_data))} вакансий из файла {path_file_json}')    # Сообщение
            self.vacancies = vacancies_data
        file.close()    # Закрытие файла

