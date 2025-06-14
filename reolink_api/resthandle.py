from typing import (
    Dict,
    List,
    Optional
)
import requests
from loguru import logger


class Request:
    proxies = None

    @staticmethod
    def post(url: str, data: List[Dict], params=None) -> Optional[requests.Response]:
        """
        Post request
        :param params:
        :param url:
        :param data:
        :return:
        """
        try:
            headers = {'content-type': 'application/json'}
            r = requests.post(url, verify=False, params=params, json=data, headers=headers,
                              proxies=Request.proxies)
            # if params is not None:
            #     r = requests.post(url, params=params, json=data, headers=headers, proxies=proxies)
            # else:
            #     r = requests.post(url, json=data)
            if r.status_code == 200:
                return r
            else:
                raise ValueError(f"Http Request had non-200 Status: {r.status_code}", r.status_code)
        except Exception as e:
            logger.error("Post Error\n", e)
            raise

    @staticmethod
    def get(url: str, params: Dict, timeout: int = 1) -> Optional[requests.Response]:
        """
        Get request
        :param url:
        :param params:
        :param timeout:
        :return:
        """
        try:
            data = requests.get(url=url, verify=False, params=params, timeout=timeout, proxies=Request.proxies)
            return data
        except Exception as e:
            logger.error("Get Error\n", e)
            raise
