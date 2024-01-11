#!/usr/bin/env python3
''' Personal Data Module
'''
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    ''' Returns messages obsuscated. '''
    for field in fields:
        message = re.sub(f'{field}=*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
