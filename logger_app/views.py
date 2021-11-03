import logging
from django.shortcuts import HttpResponse
from django.views import View

logger = logging.getLogger(__name__)


class HomePage(View):
    def get(self, request):
        logger.info("This is info level log")
        logger.error("This is error level log")
        logger.critical("This is critical log")
        logger.debug("Hello This is a logger")
        return HttpResponse("Okay")
