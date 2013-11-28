from django.http import HttpResponseRedirect

import settings
from .models import LanguagePack
from config.models import Settings
from settings import LOG as logging


class SessionLanguage:
    def process_request(self, request):
        """
        Process requests to set language, redirect to the same URL to continue processing
        without leaving the "set" in the browser history.
        """

        # Set the set of available languages
        if "language_choices" not in request.session:
            request.session["language_choices"] = list(LanguagePack.objects.all())

        # Set the current language, and redirect (to clean browser history)
        if request.is_admin and request.GET.get("set_default_language"):
            Settings.set("default_language", request.GET["set_default_language"])
            request.session["default_language"] = request.GET["set_default_language"]
            logging.debug("setting default language to %s" % request.GET["set_default_language"])

            request.session["django_language"] = request.GET["set_default_language"]
            logging.debug("setting session language to %s" % request.session["django_language"])
            return HttpResponseRedirect(request.path)

        elif request.GET.get("set_language"):
            request.session["django_language"] = request.GET["set_language"]
            logging.debug("setting session language to %s" % request.session["django_language"])
            return HttpResponseRedirect(request.path)

        # Process the current language
        if "default_language" not in request.session:
            request.session["default_language"] = Settings.get("default_language") or settings.LANGUAGE_CODE
        if "django_language" not in request.session:
            request.session["django_language"] = request.session["default_language"]
            logging.debug("setting session language to %s" % request.session["django_language"])

        # each request can get the language from the querystring, or from the currently set session language
        request.language = request.session["django_language"]

class VideoLanguage:
    """SessionLanguage must be called first"""
    def process_request(self, request):
        request.video_language = request.GET.get("lang") or request.session["django_language"]
