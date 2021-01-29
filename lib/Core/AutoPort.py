from lib.Core import hook
from lib import logger
from random import randint
from time import sleep

port_rotate_count = 0
port_clicked = False


def call(t, d):
    global port_clicked
    if not hook.hack_available() and not port_clicked:
        port = select_port(t)
        if port.is_displayed() and port.is_enabled():
            sleep(d)
            port.click()
            port_clicked = True


def select_port(t):
    global port_rotate_count
    if 0 <= t <= 2:
        return return_port(t)
    if t == 3:
        rand = randint(0, 2)
        return return_port(rand)


def return_port(c):
    if c == 0:
        logger.debug("PORT A SELECTED")
        return hook.portA
    if c == 1:
        logger.debug("PORT B SELECTED")
        return hook.portB
    if c == 2:
        logger.debug("PORT C SELECTED")
        return hook.portC
