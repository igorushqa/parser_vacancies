class Vacancy:
    """
    Класс для работы с вакансиями
    """
    all = []

    def __init__(self, name, vacancy_id, source, url, salary_from, salary_to, salary_avg, area) -> None:
        self.name = name
        self.vacancy_id = vacancy_id
        self.source = source
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_avg = salary_avg
        self.area = area
        self.all = self.all.append(self)

    def __repr__(self) -> str:
        """
        Вывод полной информации о вакансии
        """
        if self.salary_from == '0':
            salary_from_show = 'не указана'
        else:
            salary_from_show = self.salary_from
        if self.salary_to == '0':
            salary_to_show = 'не указана'
        else:
            salary_to_show = self.salary_to
        if self.salary_avg == '0':
            salary_avg_show = 'не расчитана'
        else:
            salary_avg_show = self.salary_avg
        return f"id: {self.vacancy_id}, name: {self.name}, link: {self.url}, " \
               f"Зарплата: {salary_from_show} - {salary_to_show}, средняя - {salary_avg_show}, " \
               f"Город: {self.area}, api - {self.source}"

    def __str__(self):
        return f"Вакансия: {self.name} со сред. З/П: {self.salary_avg} в городе {self.area}"

    def __eq__(self, other) -> bool:
        if self.salary_from == other.salary_from:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        if self.salary_from < other.salary_from:
            return True
        else:
            return False

    def __le__(self, other) -> bool:
        if self.salary_from <= other.salary_from:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        if self.salary_from > other.salary_from:
            return True
        else:
            return False

    def __ge__(self, other) -> bool:
        if self.salary_from >= other.salary_from:
            return True
        else:
            return False

    @classmethod
    def get_json_from_vacancy(cls) -> list:
        """
        Класс-метод выгружает данные из экземпляров класса
        Vacancy
        """
        vacancies_data = []
        for vacancy in cls.all:
            vacancies_data.append({'name': vacancy.name, 'vacancy_id': vacancy.vacancy_id, 'source': vacancy.source,
                                   'url': vacancy.url, 'salary_from': vacancy.salary_from,
                                   'salary_to': vacancy.salary_to, 'salary_avg': vacancy.salary_avg,
                                   'area': vacancy.area})
        return vacancies_data

    @classmethod
    def delete_vacancy(cls, element_id: str) -> None:
        """
        Класс-метод поиска и удаления экземпляра класса Vacancy
        по id вакансии
        """
        length_of_list = len(cls.all)
        for vacancy in range(len(cls.all) - 1):
            if cls.all[vacancy].vacancy_id == element_id:
                print(f'!!!Запись - {repr(cls.all[vacancy])} удалена!!!')
                cls.all.pop(vacancy)
                break
        if length_of_list == len(cls.all):
            print('Запись с таким ID не найдена')

    @classmethod
    def get_vacancies(cls, vacancies_data) -> None:
        """
        Класс-метод создания экземпляров класса
        Vacancy, инициализируемых данными vacancies_data
        """
        cls.all.clear()
        for it in vacancies_data:
            cls(it['name'], it['vacancy_id'], it['source'], it['url'], it['salary_from'], it['salary_to'],
                it['salary_avg'], it['area'])

    @classmethod
    def show_n_vacancies(cls, number_to_show=10000) -> None:
        """
        Класс-метод вывода заданного количества вакансий
        """
        if number_to_show == 10000:
            number_to_show = len(cls.all)
        else:
            if number_to_show > len(cls.all):
                print(f"В списке только {len(cls.all)}")
                number_to_show = len(cls.all)
        for numbers in range(number_to_show):
            print(repr(cls.all[numbers]))

    @classmethod
    def add_vacancy(cls, name, vacancy_id, source, url, salary_from, salary_to, salary_avg, area) -> None:
        """
        Класс-метод для добавления вакансии пользователем
        """
        cls.all.append(cls(name, vacancy_id, source, url, salary_from, salary_to, salary_avg, area))

    @staticmethod
    def vacancy_data_splitter(hh_data: list, sj_data: list) -> list:
        """
        Класс-метод, для создания общего json списка вакансий с HeadHunter и SuperJob
        """
        all_vacancies = hh_data
        all_vacancies.extend(sj_data)
        return all_vacancies

    @staticmethod
    def get_vacancy_by_salary(vacancies_data):
        """
        Функция сортировки данных вакансий по убыванию начальной з|п
        """
        vacancies = sorted(vacancies_data, key=lambda vacancy: int(vacancy['salary_from']), reverse=True)
        return vacancies
