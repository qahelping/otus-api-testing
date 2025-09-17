import pytest
import requests

import logging


def create_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Создаем обработчик для записи логов в файл
    file_handler = logging.FileHandler('log.log')
    file_handler.setLevel(logging.INFO)

    # Форматирование логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Добавляем обработчики к логгеру
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = create_logger()

@pytest.mark.parametrize("status_code", [
    # 200,  # OK
    # 300,  # Multiple Choices
    # 400,  # Bad Request
    404,  # Not Found
    # 500  # Internal Server Error
])
def test_logger(status_code):
    url = f'https://httpbin.org/status/{status_code}'
    response = requests.get(url)
    try:
        response.raise_for_status()
        logger.info("OK. URL: %s, Code: %d", url, response.status_code)
        assert True
    except requests.exceptions.HTTPError as err:
        logger.error("Error. %s", str(err))
        assert False