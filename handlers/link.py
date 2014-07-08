from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)

class LinkHandler(BaseHandler):
	def get(self):
		self.render("base.html")