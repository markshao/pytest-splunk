# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('splunk')
    group._addoption(
        "--bcservice", dest="bcservice", metavar="battle cat service uri",
        action="store",
        help=""
    )
    group._addoption(
        "--bctoken", dest="bctoken", metavar="battle cat token", action="store",
        help=""
    )


def pytest_configure(config):
    pass


class SplunkPlugin(object):
    def __init__(self):
        pass
