from lib.Core import hook
from lib.globalvar import GV
from lib import globalvar as gv

sent_msg = False


def call(t):
    if hook.target_msg.is_displayed():
        if not GV.sent_msg:
            if t == 0:
                hook.target_msg.send_keys('You are hacked by {} {} {}.'.format(gv.APPNAME, gv.VERSION, gv.APPTYPE))
            if t == 1:
                hook.target_msg.send_keys('http://github.com/sserve-kr/TypeSense')
            if t == 2:
                hook.target_msg_window_close.click()
            hook.target_msg_btn.click()
            GV.sent_msg = True
            return
