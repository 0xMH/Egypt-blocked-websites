import sys
import requests
import os
from subprocess import Popen, PIPE
from selenium import webdriver
from urllib.parse import urlparse

abspath = lambda *p: os.path.abspath(os.path.join(*p))
ROOT = abspath(os.path.dirname(__file__))


def do_screen_capturing(url, screen_path):
    driver = webdriver.PhantomJS()
    # driver.set_script_timeout(30)
    # if width and height:
    #     driver.set_window_size(width, height)
    driver.get(url)
    driver.save_screenshot(screen_path)

def get_screen_shot(**kwargs):
    url = kwargs['url']
    width = int(kwargs.get('width', 1024)) # screen width to capture
    height = int(kwargs.get('height', 768)) # screen height to capture
    filename = kwargs.get('filename', 'screen.png') # file name e.g. screen.png
    path = kwargs.get('path', ROOT) # directory path to store screen

    screen_path = abspath(path, filename)
    do_screen_capturing(url, screen_path)

    return screen_path

if __name__ == '__main__':
    notworking = []
    print('pics are being saved in: {}'.format(ROOT + '/200'))

    with open(sys.argv[1], 'r') as filehandle:  
        for line in filehandle:
            # remove linebreak which is the last character of the string
            url = line[:-1].replace('https://','').replace('https//','')

            try:
                xf = "http://"+url
                print ( "Checking: {}..".format(xf))
                x = requests.get(xf)
                if x.status_code == 200:
                    picdir = ROOT + '/200'
                    if not os.path.exists(picdir):
                        os.makedirs(picdir)
                    filena = filename=urlparse(xf).netloc + '.png'
                    screen_path = get_screen_shot(
                    url=xf,filename=filena,path=picdir )
            except:
               notworking.append(url)
        print("Websites Not Workings:")
        for web in notworking:
            print(web)
