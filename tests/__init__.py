# -*- coding: utf8 -*-

import sys
import os
import pybossa_z3950 as plugin

# Use the PyBossa test suite
sys.path.append(os.path.abspath("./pybossa/test"))


def setUpPackage():
    """Setup the plugin."""
    from default import flask_app
    with flask_app.app_context():
        plugin_dir = os.path.dirname(plugin.__file__)
        plugin.PyBossaZ3950(plugin_dir).setup()
