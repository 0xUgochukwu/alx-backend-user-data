#!/usr/bin/env python3
''' Personal Data
'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, seprator: str) -> str:
    ''' Returns messages obsuscated.
    '''
    for field in fields:
        message = re.sub(f'{field}=.+?{seprator}',
                         f'{field}={redaction}{seprator}', message)
    return message
