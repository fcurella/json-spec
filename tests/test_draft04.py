"""
    tests.tests_dratf04
    ~~~~~~~~~~~~~~~~~~~~~~

    Test against `Common test suite`_.

    .. _`Common test suite`:: https://github.com/json-schema/JSON-Schema-Test-Suite
"""

from jsonspec.validators import load, ValidationError, CompilationError
from jsonspec.reference.providers import SpecProvider, ProxyProvider
from jsonspec import driver as json

import io
import os
import pytest
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
here = os.path.dirname(os.path.abspath(__file__))


def contents(*paths):
    fullpath = os.path.join(here, 'suite', *paths)
    d = len(fullpath)
    for filepath in Path(fullpath).glob('**/*.json'):
        with filepath.open('r', encoding='utf-8') as file:
            yield json.load(file), filepath.as_posix()[d:].lstrip('/')


provider = ProxyProvider(SpecProvider())
for data, src in contents('remotes'):
    provider[os.path.join('http://localhost:1234', src)] = data


def scenarios(draft):
    skip = []

    for data, src in contents('tests', draft):
        if src in skip:
            continue

        for block in data:
            for test in block['tests']:
                yield (block['schema'], test['description'],
                       test['data'], test['valid'], src)


@pytest.mark.parametrize('schema, description, data, valid, src',
                         scenarios('draft4'))
def test_common(schema, description, data, valid, src):
    try:
        load(schema, provider=provider).validate(data)
        if not valid:
            assert False, description
    except (ValidationError, CompilationError) as error:
        if valid:
            logger.exception(error)
            assert False, description
