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
        "--splunkuri", dest="splunkuri", metavar="splunk http input service uri", action="store", default=None,
        help=""
    )
    group._addoption(
        "--splunktoken", dest="splunktoken", metavar="splunk http input security token", action="store", default=None,
        help=""
    )


def pytest_configure(config):
    if not config.pluginmanager.hasplugin("splunk"):
        config.pluginmanager.register(SplunkPlugin(config))


class SplunkPlugin(object):
    def __init__(self, config):
        self.config = config

        assert hasattr(self.config, "splunkuri")
        assert hasattr(self.config, "splunktoken")

        self.authentication_header = {"Authorization": "Splunk %s" % self.config.splunktoken}

    def pytest_terminal_summary(self, terminalreporter):

        # send summary report to splunk
        try:
            url = self.config.splunkuri + HTTPINPUT
            headers = {"Content-Type": "json"}
            headers.update(self.authentication_header)

            event = {
                "passed": len(terminalreporter.stats["passed"]),
                "failed": len(terminalreporter.stats["failed"])
            }

            data = json.dumps({"event": event})
            requests.post(url, headers=headers, data=data, verify=False)
        except Exception, e:
            print e
