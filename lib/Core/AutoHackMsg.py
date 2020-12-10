from time import sleep
from lib.Core import hook
from lib import globalvar as gv


def call():
    if hook.target_msg.is_displayed():
        if not gv.sent_msg:
            hook.target_msg.send_keys('You are hacked by {} {} {}.'.format(gv.APPNAME, gv.VERSION, gv.APPTYPE))
            hook.target_msg_btn.click()
            gv.sent_msg = True
            return
