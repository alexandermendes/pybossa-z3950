# -*- coding: utf8 -*-
"""Main package for pybossa-z3950."""

from flask import current_app as app
from flask.ext.plugins import Plugin
from flask.ext.z3950 import Z3950Manager

__plugin__ = "PyBossaZ3950"
__version__ = "0.0.1"


class PyBossaZ3950(Plugin):
    """A PyBossa plugin for Z39.50 integration."""

    def setup(self):
        """Setup plugin."""
        try:
        	if app.config.get('Z3950_DATABASES'):
        		Z3950Manager.init_app(app)
        		self.setup_blueprint()
        except Exception as inst:  # pragma: no cover
            print type(inst)
            print inst.args
            print inst
            print "Z39.50 plugin disabled"
            log_message = 'Z39.50 plugin disabled: %s' % str(inst)
            app.logger.info(log_message)


    def setup_blueprint(self):
        """Setup blueprint."""
        from .blueprint import Z3950Blueprint
        blueprint = Z3950Blueprint()
        app.register_blueprint(blueprint, url_prefix="/z3950")