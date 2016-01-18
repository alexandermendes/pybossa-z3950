# -*- coding: utf8 -*-
"""Blueprint module for pybossa-z3950."""

from flask import Blueprint


class Z3950Blueprint(Blueprint):
    """Blueprint to support Z39.50 API.

    Parameters
    ----------
    **kwargs
        Arbitrary keyword arguments.
    """

    def __init__(self, **kwargs):
        """Initialise blueprint instance and add all URL rules."""
        defaults = {'name': 'z3950', 'import_name': __name__}
        defaults.update(kwargs)

        super(Z3950Blueprint, self).__init__(**defaults)

        url_map = self._url_map()

        for url, view_func in url_map.iteritems():
            self.add_url_rule(url, view_func=view_func, methods=['GET'])


    def _url_map(self):
        """Return all required URLs and view functions."""
        return {}
