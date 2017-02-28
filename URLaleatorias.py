# Servidor url aleatorias

import webapp
import random

class randURL(webapp):

    def process(self, parsedRequest):

        url = random.randint(0,999999)
        answer = "<html><head><a href="http://localhost:1234/"+ str(url)+ ">Dame otra</a"+<head></html>", 'utf-8'))



