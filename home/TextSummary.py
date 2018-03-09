import requests
import json
from gensim.summarization import summarize

class TextSummary:

    def getSummary(self, text, Summary_ratio = 0.4):
        return summarize(text,ratio = Summary_ratio)
