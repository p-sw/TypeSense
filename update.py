from requests import get
from requests.exceptions import Timeout
from threading import Thread
from lib import logger
from os import listdir
import json

update_path = 'png_data\\'
samplepath = 'sample\\'
dir_list = listdir(samplepath)
if 'info.json' not in dir_list:
    raise FileNotFoundError
del dir_list[dir_list.index('info.json')]
with open(samplepath+"info.json", "r") as f:
    word_dict_sample = json.load(f)
word_e = {}
word_m = {}
word_h = {}
word_dict_to_dump = {}


def update_words(level: str):
    url_end = False
    url_num = 0
    if level == "e":
        selfdict = word_e
    elif level == "m":
        selfdict = word_m
    elif level == "h":
        selfdict = word_h
    else:
        return
    while not url_end:
        url = 'http://s0urce.io/client/img/word/' + level + '/' + str(url_num)
        try:
            response = get(url, timeout=3)
        except Timeout:
            print('TIMEOUT ON THREAD '+level)
            url_end = True
        if url_end is False:
            curr_img = response.content
            curr_filename = level+'_'+str(url_num)+'.png'
            curr_filename_full = update_path + curr_filename
            file = open(curr_filename_full, "wb")
            file.write(curr_img)
            file.close()
            print("Download finished: " + curr_filename)
            print("Word Detecting..")
            for file in dir_list:
                img_f = open(samplepath + file, 'rb')
                img_dt = img_f.read()
                img_f.close()
                if img_dt == curr_img:
                    cw = word_dict_sample[file]
                    selfdict[url] = cw
                    print('Word detected: {}'.format(cw))
        url_num += 1


def process_start():
    e = Thread(target=update_words, args=['e'])
    m = Thread(target=update_words, args=['m'])
    h = Thread(target=update_words, args=['h'])
    e.start()
    m.start()
    h.start()
    e.join()
    m.join()
    h.join()
    print("CREATING INFO FILE")
    with open(update_path+"info.json", "w+") as db:
        json.dump(dict(word_e, **word_m, **word_h), db)
    print("INFO FILE CREATED")


print("Process Starting")
process_start()
print('Process Finished')
