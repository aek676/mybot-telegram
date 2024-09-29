from dotenv import load_dotenv, dotenv_values
import requests, pastelink, linkvertise

class User:
    pastelink = pastelink.Pastelink()
    client_linkvertise = linkvertise.Linkvertise()

    def __init__(self, name, img):
        self.name = name
        self.img = img
        self.urlPastelink = None
        self.linkPastelink = "https://pastelink.net/"
        self.linvertise = None
    
    def create_pastelink(self, title, body):
        self.codPastelink = self.pastelink.create_paste(title, body)
        self.pastelink += self.codPastelink

    def edit_body_pastelink(self, paste_url, body):
        print(self.pastelink.edit_body_paste(paste_url, body))

    def delete_paste(self, paste_url):
        print(self.pastelink.delete_paste(paste_url))
        

