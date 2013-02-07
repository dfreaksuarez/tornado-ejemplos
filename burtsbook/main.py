import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

from tornado.options import define, options
define("port", default=8000, help="este es el puerto", type=int)


class Application(tornado.web.RequestHandler):
	def __init__(self):
		handlers=[(r"/", MainHandler)]
		settings=dict(
			template_path=os.path.join(os.path.dirname(__file__),"templates"),
			static_path=os.path.join(os.path.dirname(__file__),"static"),
			debug=True,
			)
		tornado.web.Application.__init__(selfm handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render(
			"index.html",
			page_title="Daniel's Books | Home",
			header_text="Welcome to Daniel's Books",
			)


if __name__ == "__main__":
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
