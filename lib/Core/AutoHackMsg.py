from lib.Core import hook
from lib import globalvar as gv
from lib import logger

sent_msg = False


def call(t):
    global sent_msg
    if hook.target_msg.is_displayed():
        if not sent_msg:
            logger.debug("AutoHackMsg Sent")
            if t == 0:
                hook.target_msg.send_keys('You are hacked by {} {} {}.'.format(gv.APPNAME, gv.VERSION, gv.APPTYPE))
            if t == 1:
                hook.target_msg.send_keys('http://github.com/sserve-kr/TypeSense')
            if t == 2:
                hook.target_msg_window_close.click()
            logger.debug("AutoHackMsg clicked")
            hook.target_msg_btn.click()
            sent_msg = True
            return
