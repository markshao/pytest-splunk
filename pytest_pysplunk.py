# -*- coding: utf-8 -*-

import requests
import json

HTTPINPUT = "/services/collector/event"
REPORTPROTOCOL = {
    "total_test_case_number": 0,
}


def pytest_addoption(parser):
    group = parser.getgroup('splunk')
    group._addoption(
        "--splunkuri", dest="splunkuri", metavar="splunk http input service uri",
        action="store",
        help=""
    )
    group._addoption(
        "--splunktoken", dest="splunktoken", metavar="splunk http input security token", action="store",
        help=""
    )


def pytest_configure(config):
    if not config.pluginmanager.hasplugin("splunk"):
        config.pluginmanager.register(SplunkPlugin(config))


class SplunkPlugin(object):
    def __init__(self, config):
        self.config = config

    def pytest_terminal_summary(self, terminalreporter):
        pass