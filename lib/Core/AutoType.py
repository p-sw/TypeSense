from selenium.webdriver.common.keys import Keys
from time import sleep
from lib.Core import hook
from json import load
from lib import logger
from lib.Core import AutoHackMsg
from lib.Core import AutoPort


with open("png_data\\info.json", "r") as data_file:
    word_dictionary = load(data_file)
current_word = ''
previous_word = ''


def detect_word():
    global previous_word
    if 'template.png' in hook.get_image_url():
        return ''
    if hook.get_image_url() not in word_dictionary:
        logger.warning('Unregistered word image: '+hook.get_image_url())
        return ''
    logger.info('Get word '+word_dictionary[hook.get_image_url()])
    return word_dictionary[hook.get_image_url()]


def call(key_delay: float, return_delay: float):
    global current_word, previous_word

    typed = hook.input_box.get_attribute('value')
    if not hook.hack_available():
        return

    if current_word == '':
        current_word = detect_word()
        if current_word == '':
            return
    logger.debug("AutoHackMsg AutoPort Initial")
    AutoHackMsg.sent_msg = False
    AutoPort.port_clicked = False
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
