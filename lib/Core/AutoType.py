from selenium.webdriver.common.keys import Keys
from time import sleep
from lib.Core import hook
from json import load
from lib import logger
from lib import globalvar as gv


with open("png_data\\info.json", "r") as data_file:
    word_dictionary = load(data_file)
current_word = ''
previous_word = ''


def get_image_url():
    return hook.word_img.get_attribute('src')


def hack_available():
    if 'template.png' in get_image_url():
        return False
    elif not hook.console.is_displayed():
        return False
    elif not hook.input_box.is_enabled():
        return False
    else:
        return True


def detect_word():
    global previous_word
    if 'template.png' in get_image_url():
        return
    if get_image_url() not in word_dictionary:
        logger.error('Unregistered word image: '+get_image_url())
        return
    logger.info('Get word '+word_dictionary[get_image_url()])
    return word_dictionary[get_image_url()]


def call(key_delay: float, return_delay: float):
    global current_word, previous_word

    typed = hook.input_box.get_attribute('value')
    if not hack_available():
        return

    if current_word == '':
        current_word = detect_word()
        if current_word is None:
            return
    gv.sent_msg = False
    try:
        if current_word == typed or len(typed) >= len(current_word):
            hook.input_box.send_keys(Keys.RETURN)
            logger.debug('Word Returned')
            previous_word = current_word
            current_word = ''
            sleep(return_delay)
    except TypeError:
        return
    else:
        for i, c in enumerate(list(current_word)):
            if i + 1 > len(typed):
                hook.input_box.send_keys(c)
                logger.debug('Sent key '+c)
                sleep(key_delay)
                return
