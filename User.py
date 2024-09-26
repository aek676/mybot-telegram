from dotenv import load_dotenv, dotenv_values
import requests

class User:

    def __init__(self, name, img):
        self.name = name
        self.img = img
        self.codPastelink = None
        self.linkPastelink = None
        self.linkvertise = None

        
        

