import random

import requests
from requests.packages.urllib3.util import retry  # type: ignore

from src.config.base import WORDGENERATOR_URL

_BASE_SESSION = requests.Session()
_RETRIES = retry.Retry(total=5, backoff_factor=1, status_forcelist=(429, 500, 502, 503, 504))
_ADAPTER = requests.adapters.HTTPAdapter(max_retries=_RETRIES)  # type: ignore
DEFAULT_SESSION = requests.Session()
DEFAULT_SESSION.mount('https://', _ADAPTER)
DEFAULT_SESSION.mount('http://', _ADAPTER)


def _get_pre_generated_paragraphs():
    session = _BASE_SESSION
    response = session.get(WORDGENERATOR_URL)
    return response.json()


def generate_paragraphs(paragraph_count: int) -> list[str]:
    paragraphs = _get_pre_generated_paragraphs()['data']
    paragraphs_len = len(paragraphs)
    response = []
    for _ in range(paragraph_count):
        response.append(paragraphs[random.randint(0, paragraphs_len)])
    return response

