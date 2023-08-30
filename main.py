from API_Files.HeadHunterAPI import HeadHunterAPI
from API_Files.JSONSaver import JSONSaver
from API_Files.SuperJobAPI import SuperJobAPI
from API_Files.Vacancies import Vacancy

hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()
j_saver = JSONSaver()
vacancy = Vacancy


def user_interaction():
    print(f'Добро пожаловать в программу работы с вакансиями с сайтов HeadHunter и SuperJob')
    start_menu()


def start_menu() -> None:
    profession = input('Введите название вакансии:\n')
    hh_data = hh_api.get_vacancies(profession)
    sj_data = sj_api.get_vacancies(profession)
    data = vacancy.vacancy_data_splitter(hh_data, sj_data)
    j_saver.save_raw_to_json(data)
    vacancy.get_vacancies(j_saver.vacancies)
    second_menu()


def second_menu() -> None:
    while True:
        print("=======================================================================================")
        print(f"Для работы с вакансиями выбирете действие:")
        print(f"1 - Показать несколько вакансий или все вакансии")
        print(f"2 - Сортировать вакансии по минимальной зарплате и показать ТОП")
        print(f"3 - Добавить вакансию")
        print(f"4 - Удалить вакансию")
        print(f"5 - Сохранить вакансии в файл")
        answer = input('Введите Exit для выхода\n')
        if answer.lower() in ("1", "2", "3", "4", "5", "exit"):
            if answer == "1":
                vac_number = input(
                    "Введите количество вакансий для вывода, или нажмите Enter - показать все вакансии\n")
                if vac_number.isdigit():
                    vacancy.show_n_vacancies(int(vac_number))
                elif vac_number == '':
                    vacancy.show_n_vacancies()
                else:
                    print('Некорректный ввод, повторите попытку\n')
            elif answer == "2":
                vacancies = vacancy.get_json_from_vacancy()
                sorted_vacancies = vacancy.get_vacancy_by_salary(vacancies)
                vacancy.get_vacancies(sorted_vacancies)
                vacancies_for_show = input('Введите число ТОП-вакансий для показа\n')
                if vacancies_for_show.isdigit():
                    vacancy.show_n_vacancies(int(vacancies_for_show))
                elif vacancies_for_show == '':
                    vacancy.show_n_vacancies()
                else:
                    print('Некорректный ввод, повторите попытку\n')
            elif answer == "3":
                name = input("Введите название вакансии\n")
                vacancy_id = input("Введите ID вакансии\n")
                source = input("Введите платформу\n")
                url = input("Введите ссылку на вакансию\n")
                salary_from = input("Введите минимальную з/п для вакансии\n")
                salary_to = input("Введите максимальную з/п для вакансии\n")
                salary_avg = input("Введите среднюю з/п для вакансии\n")
                area = input("Введите город вакансии\n")
                vacancy.add_vacancy(name, vacancy_id, source, url, salary_from, salary_to, salary_avg, area)
                print(f'Вакансия {repr(vacancy.all[-1])} успешно добавлена')
            elif answer == "4":
                vacancy_to_del = input('Введите ID вакансии для удаления:\n')
                vacancy.delete_vacancy(vacancy_to_del)
            elif answer == "5":
                j_saver.save_raw_to_json(vacancy.get_json_from_vacancy())
            else:
                exit()
        else:
            print('Некорректный ввод, проверьте раскладку клавиатуры и введите один из предлагаемых вариантов\n')


if __name__ == "__main__":
    user_interaction()
