import json
from abc import ABC, abstractmethod
from src.hh_api import HeadHunter

class Filesaver(ABC):

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def write_data(self, vacancies):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_data(self):
        pass


class JSONSaver(Filesaver):
    """"Класс для записи в json-файл"""

    def __init__(self, filename = "user_vacancies.json"):
        super().__init__(filename)

    def write_data(self, vacancies):
        """ Запись данных в json """

        data = self.get_data()
        data.extend(vacancies)

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def get_data(self):
        """ Получение данных json """

        try:
            return json.load(open(self.filename))
        except FileNotFoundError:
            return []

    def del_data(self):
        """ Удаление данных из файла """

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)