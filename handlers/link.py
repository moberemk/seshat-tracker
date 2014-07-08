from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)

from settings import DEBUG

class LinkHandler(BaseHandler):
	def get(self):
		# Redirect the user to the appropriate link (using 302 for testing)
		if DEBUG:
			self.set_status(302)
		else:
			self.set_status(301)

		self.set_header("Location", "https://publicsectordigest.com/img/psd_logo_new.png")