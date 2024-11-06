import re


def get_reg_data() -> dict:
    """
    Возвращает список паттернов регулярных выражений
    для проверки пользовательских данных

    :return: список паттернов
    """
    patterns_list = {
        'name_pattern': r'^[a-zA-Zа-яА-ЯёЁ]+$',
        'phone_pattern': r'^\+\d{1,3}\(\d{2}\)\d{7}$',
        'email_pattern': r'^[a-zA-Z0-9]+@yandex\.ru$'
    }

    return patterns_list


def reg_check(user_data: str, reg_pattern: str, users_list: list) -> str:
    """ 
    Возвращает аргумент user_data, если он прошел все 
    проверки

    :param user_data: пользовательские данные для проверки
    :param reg_pattern: паттерн регулярки для проверки данных
    :param users_list: список уже созданных пользователей
    :data_to_check:
    :return: user_data
    """
    check_reg = bool(re.match(reg_pattern, user_data))
    check_unique = check_unique_data(user_data, users_list)

    if check_reg and check_unique:
        return user_data

    


def check_unique_data(user_data: str, users_list: list):
    """ 
    Проверяет уникальность введенного номера телефона 
    и адреса email

    :param user_data: пользовательские данные для проверки
    :param 
    """
    if user_data not in users_list:
        return True
