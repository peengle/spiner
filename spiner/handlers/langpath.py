# -*- coding: utf-8 -*-
"""Base handler for root path when we have lang specific index pages

You should define lang specific routes:

_LANG_PREFIX = '/<lang:[a-z]{2}>'

routes = [
    RedirectRoute(
        '{}'.format(_LANG_PREFIX), redirect_to_name='index_langpath'),
    PathPrefixRoute(
        _LANG_PREFIX,
        [
            Route('/', handler=<Handler>, name='index_langpath'),
        ]),
]
"""

import webapp2
from spiner.config import getenv
from spiner.trans import get_prefered_lang


class Handler(webapp2.RequestHandler):
    def get(self):
        lang = self._get_prefered_lang()
        self.redirect(webapp2.uri_for('index_langpath', lang=lang))

    def _get_prefered_lang(self):
        return get_prefered_lang(
            self.request.headers['Accept-Language'],
            getenv('SUPPORTED_LANGUAGES'))