from linkvertise import LinkvertiseClient
from dotenv import load_dotenv, dotenv_values

load_dotenv()
env = dotenv_values()

class Linkvertise:
    userID = env['USER_ID']
    client = LinkvertiseClient()

    def create_linkvertise(self, url):
        return self.client.linkvertise(self.userID, url)
    

if __name__ == "__main__":
    client = Linkvertise()
    link = client.create_linkvertise("www.ual.es")
    print(link)
