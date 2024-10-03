from abc import ABC, abstractmethod

import requests


class WorkingWithAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class GetVacanciesFromHH(WorkingWithAPI):
    """Класс для получения вакансий через API"""

    text_for_search: str

    def __init__(self, text_for_search: str):
        if isinstance(text_for_search, str):
            self.__text_for_search = text_for_search
        else:
            raise TypeError('Текст должен быть "str"')
        self.__url = 'https://hh.ru/vacancy'
        self.__params = {'text': self.__text_for_search}

    def __get_vacancies_from_API(self):
        try:
            response = requests.get(self.__url, self.__params)
            status_code = response.status_code
            if status_code == 200:
                vacancies = response.json()['items']
        except requests.exceptions.ConnectionError:
            print('Проверьте ваше соединение с сетью')
            return []
        except requests.exceptions.Timeout:
            print('Время ожидания запроса истекло. Повторите попытку позже.')
            return []
        except requests.exceptions.RequestException:
            print('Произошла ошибка.')
            return []
        else:
            return vacancies

    @property
    def get_vacancies(self):
        return self.__get_vacancies_from_API()


first = GetVacanciesFromHH('Python')
data = first.get_vacancies
print(data)
