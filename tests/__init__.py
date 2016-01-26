# -*- coding: utf8 -*-

import sys
import os
import pybossa_z3950 as plugin

# Use the PyBossa test suite
sys.path.append(os.path.abspath("./pybossa/test"))

from default import Test


def setUpPackage():
    """Setup the plugin."""
    from default import flask_app
    with flask_app.app_context():
        settings = os.path.abspath('./settings_test.py')
        flask_app.config.from_pyfile(settings)
        plugin_dir = os.path.dirname(plugin.__file__)
        plugin.PyBossaZ3950(plugin_dir).setup()


class TestPlugin(Test):

    def test_blueprint_registered(self):
        assert 'z3950' in self.flask_app.blueprints
