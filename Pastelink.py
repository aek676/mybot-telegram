from dotenv import load_dotenv, dotenv_values
import requests, readline

load_dotenv()
env = dotenv_values()

class Pastelink:
    def __init__(self):
        self.endpoint = env['ENDPOINT']
        self.api_key = env['API_KEY']

    def create_paste(self, title, body, visiblity='hidden', password=None, dry_run=0):
        url = f"https://{self.endpoint}/create-paste"
        data = {
            'api_key': self.api_key,
            'dry_run': dry_run,
            'title': title,
            'body': body,
            'option_visibility': visiblity,
            'access_password': password,
            'option_links': 'show',
            'option_referrer': 'public',
            'option_security': 'none'
        }
        
        res = requests.post(url, data)

        if res.status_code == 200:
            print(res.json())
            return res.json()['url']
        else:
            print(f"Error to create the paste. Status code: {res.status_code}")
            return res.text
        
    def edit_paste(self, paste_url):
        paste = requests.get(f"https://{self.endpoint}/get-paste?url={paste_url}&api_key={self.api_key}").json()
        title = paste['title']
        body = paste['body']

        print(f"Title: {title}")
        readline.set_startup_hook(lambda: readline.insert_text(body))
        try:
            body = input("Add content: ")
        finally:
            readline.set_pre_input_hook

        print(body)
        url = f"https://{env['ENDPOINT']}/edit-paste"
        data = {
            'api_key': self.api_key,
            'dry_run': 0,
            'body': str(body),
            'url': paste_url
        }
        
        res = requests.post(url, data)
        res_text_obj = res.json()
        print(res_text_obj)



api = Pastelink()

new_paste_url = 'lbsmqy9w'
api.edit_paste(new_paste_url)



