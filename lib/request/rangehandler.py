#!/usr/bin/env python

"""
Copyright (c) 2006-2021 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.exception import SqlmapConnectionException
from thirdparty.six.moves import urllib as _urllib

class HTTPRangeHandler(_urllib.request.BaseHandler):
    """
    Handler that enables HTTP Range headers.

    Reference: http://stackoverflow.com/questions/1971240/python-seek-on-remote-file
    """

    def http_error_206(self, req, fp, code, msg, hdrs):
        # 206 Partial Content Response
        r = _urllib.response.addinfourl(fp, hdrs, req.get_full_url())
        r.code = code
        r.msg = msg
        return r

    def http_error_416(self, req, fp, code, msg, hdrs):
        errMsg = (
            "there was a problem while connecting "
            + "target ('406 - Range Not Satisfiable')"
        )

        raise SqlmapConnectionException(errMsg)
