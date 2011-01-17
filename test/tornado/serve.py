#
# Copyright (c) 2011 Thomas Rampelberg
#

"""
Test the janky decorator.
"""

__author__ = 'Thomas Rampelberg'
__author_email__ = 'thomas@saunter.org'

import logging
import time
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options
import tornado.web

import janky_post

class JankySyncHandler(tornado.web.RequestHandler):

    def get(self):
        pass

    @janky_post.handler
    def post(self):
        logging.info(self.get_argument('bar'))
        pass

class JankyAsyncHandler(tornado.web.RequestHandler):
    pass

def config():
    define('port', default=5000, type=int, help='Port to listen on.')
    define('debug', default=False, type=bool,
           help='Start the server in debug mode')
    tornado.options.parse_command_line()

routes = lambda: [(r"/janky", JankySyncHandler),
                  (r"/a/janky", JankyAsyncHandler)]

def start():
    config()
    app = tornado.web.Application(routes(), **{
            "debug": options.debug
            })
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    start()
