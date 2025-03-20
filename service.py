import json
import requests

import logging


def create_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Создаем обработчик для записи логов в файл
    file_handler = logging.FileHandler('../log.log')
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


class BaseService():

    def delete(self, url, headers):
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None


    def post(self, url, body):
        try:
            headers = {'accept': "application/json", 'Content-Type': 'application/json'}
            response = requests.post(url, data=json.dumps(body), headers=headers)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None


    def put(self, url, body, headers):
        try:
            response = requests.put(url, data=json.dumps(body), headers=headers)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None


    def get(self, url, params=None, headers=None):
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None