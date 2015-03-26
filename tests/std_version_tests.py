#! /usr/bin/env python
# vim: set fileencoding=utf-8: 
"""
Some sanity checks on the changelog and `agenda.version` module.
"""

import agenda.version as proj_version

import pychangelog.tests

class StdVersionTests(pychangelog.tests.StandardVersionTests):
    version_mod = proj_version

