from dotenv import load_dotenv, dotenv_values
import requests

import os
import io

load_dotenv()
env = dotenv_values()

def main():
    
    # Create paste
    url = f"https://{env['ENDPOINT']}/create-paste"
    data = {
        'api_key' : env['API_KEY'],
        'body' : 'Pastelink test submission body',
        'title' : 'Pastelink test submission title',
        'option_visibility' : 'private',
        'access_password' : 'pass',
        'option_links' : 'show',
        'option_referrer' : 'hide',
        'option_security' : 'captcha',
        'font_name' : 'lato',
        'font_weight' : 600,
        'font_size' : 22,
        'edit_code' : 'sdf9h843h98fdg54gdg54sef',
        #'custom_url' : '1234567',
        'dry_run' : 0
    }
    res = requests.post(url, data)
    res_text_obj = res.json()
    new_paste_url = res_text_obj['url']
    print(new_paste_url)
    
    ####################################################################
        
    # Get paste
    ## If dry_run above is set to 1, this will return paste not found
    url = f"https://{env['ENDPOINT']}/get-paste?url={new_paste_url}&api_key={env['API_KEY']}"
    res = requests.get(url)
    res_text_obj = res.json()
    print(res_text_obj)
    
    ####################################################################
    
    # Get pastes
    ## If dry_run above is set to 1, this will return no pastes found unless you have prevously created pastes already
    page = 1
    limit = 1000
    deleted = 0
    url = f"https://{env['ENDPOINT']}/get-pastes?api_key={env['API_KEY']}&page={page}&limit={limit}&deleted={deleted}"
    res = requests.get(url)
    res_text_obj = res.json()
    print(res_text_obj)
    
    ####################################################################
    
    # Edit paste
    url = f"https://{env['ENDPOINT']}/edit-paste"
    data = {
        'api_key' : env['API_KEY'],
        'body' : 'Pastelink test submission body updated',
        'title' : 'Pastelink test submission title updated',
        'option_visibility' : 'private',
        'access_password' : 'pass',
        'option_links' : 'show',
        'option_referrer' : 'hide',
        'option_security' : 'captcha',
        'font_name' : 'lato',
        'font_weight' : 600,
        'font_size' : 22,
        #'custom_url' : '1234567',
        'url' : new_paste_url,
        'dry_run' : 0
    }
    res = requests.post(url, data)
    res_text_obj = res.json()
    print(res_text_obj)
    
    ####################################################################
    
    # Delete paste
    url = f"https://{env['ENDPOINT']}/delete-paste"
    data = {
        'api_key' : env['API_KEY'],
        'url' : new_paste_url,
        'dry_run' : 0
    }
    res = requests.post(url, data)
    res_text_obj = res.json()
    print(res_text_obj)

    
if __name__ == "__main__":
    main()