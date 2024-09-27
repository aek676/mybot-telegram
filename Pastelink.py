from dotenv import load_dotenv, dotenv_values
import requests, readline, json

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
            print(json.dumps(res.json(), indent=2))
            return res.json()['url']
        else:
            print(f"Error to create the paste. Status code: {res.status_code}")
            return res.text
        
    def get_paste(self, paste_url):
        url = f"https://{self.endpoint}/get-paste?url={paste_url}&api_key={self.api_key}"
        res = requests.get(url)
        return res.json()
    
    def get_pastes(self, page, limit, deleted):
        url = f"https://{self.endpoint}/get-pastes?api_key={self.api_key}&page={page}&limit={limit}&deleted={deleted}"
        res = requests.get(url)
        return res.json()

    def edit_body_paste(self, paste_url, body):
        url = f"https://{env['ENDPOINT']}/edit-paste"
        data = {
            'api_key': self.api_key,
            'dry_run': 0,
            'body': body,
            'url': paste_url
        }
        
        res = requests.post(url, data)
        res_text_obj = res.json()

        if res.status_code == 200:
            print(res_text_obj)
            return(res_text_obj['archive_entry_url'])
        else:
            print(f"Error to edit the paste. Status code: {res.status_code}")
            return res.text


    def delete_paste(self, paste_url):
        url = f"https://{self.endpoint}/delete-paste"
        data = {
            'api_key' : self.api_key,
            'url' : paste_url,
            'dry_run' : 0
        }
        res = requests.post(url, data)
        print(json.dumps(res.json(), indent=2))


    def print_paste(self, paste_url):
        return print(f"Paste JSON: \n{json.dumps(self.get_paste(paste_url), indent=2)}")
    
    def print_pastes(self, page, limit, deleted):
        return print(f"Pastes JSON: \n{json.dumps(self.get_pastes(page, limit, deleted), indent=2)}")



# if __name__ == "__main__":
#     api = Pastelink()

#     print("Vas a crear un Pastelink, introduce los siguientes datos:")
#     title = input("Title: ")
#     body = input("Body: ")
#     pasteURL = api.create_paste(title, body)

#     print("Vas a imprimir un pastelink")
#     pasteURL = input("PasteURL: ")
#     api.print_paste(pasteURL)

#     print("Vas a imprimir todos los pastelinks que tienes")
#     page = input("Page: ")
#     limit = input("Limit: ")
#     deleted = input("Deleted: ")
#     api.print_pastes(page, limit, deleted)

#     print("Vas a editar un pastelink")
#     pasteURL = input("PasteURL: ")
#     pasteToEdit = api.get_paste(pasteURL)
#     title = pasteToEdit['title']
#     body = pasteToEdit['body']

#     print(f"Title: {title}")
#     readline.set_startup_hook(lambda: readline.insert_text(f"{body}\n"))
#     try:
#         body = input("Add content:\n").replace("\\n", "\n")
#     finally:
#         readline.set_startup_hook()
    
#     api.edit_body_paste(pasteURL, body)

#     print("Comprobamos lo editado")
#     pasteEdited = api.get_paste(pasteURL)
#     print(f"Title: {pasteEdited['title']}")
#     print(f"Body: \n{pasteEdited['body']}")

#     print("Eliminas un paste")
#     pasteURL = input("PasteURL: ")
#     api.delete_paste(pasteURL)