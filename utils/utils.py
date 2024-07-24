from src.hh_api import HeadHunter
from src.vacancy import Vacancy
from src.json_classes import JSONSaver

def user_part():
    """ Функция для работы с пользователем и записи в json-файл """

    keyword = input("Какая профессия Вас интересует?\n").lower()
    per_page = int(input("Сколько вакансий вывести?\n"))

    hh_api = HeadHunter()
    vacancies = hh_api.get_vacancies(keyword, per_page)
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies, reverse=True)


    print("Топ выбранных вакансии с 'HeadHunter' по зарплате: \n")
    for i in sorted(vacancies, reverse=True):
        print(i)


    vacancies = [vacancy.to_dict() for vacancy in vacancies]
    saver = JSONSaver()
    saver.write_data(vacancies)
    saver.get_data()
    print("Данные записаны в json-файл")



# def get_salary():
#
#     while True:
#         salary = input('Введите диапозон зарплат в формате "минимальная зарплата - максимальная зарплата": ')
#         try:
#             min_salary_str, max_salary_str = salary.split(' - ')
#             min_salary = int(min_salary_str)
#             max_salary = int(max_salary_str)
#             if min_salary > max_salary:
#                 raise ValueError
#             return min_salary, max_salary
#         except ValueError:
#             print('Неправильно введен диапозон. Пожалуйста, введите зарплаты в формате "минимальная зарплата - максимальная зарплата"')
#
#
# def get_vacancies_by_salary(min_salary, max_salary):
#     result = []
#     saver = JSONSaver()
#     all_vacancies = saver.get_vacancies()
#
#     for vac in all_vacancies:
#         salary_from = vac.salary_from
#         salary_to = vac.salary_to
#
#         if salary_from >= min_salary and salary_to <= max_salary:
#             result.append(vac)
#     return result