from lib.gui import GUI
from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from lib import logger
from lib.Core import AutoType
from lib.Core import AutoHackMsg
from lib.Core import hook
from lib.Core import AutoTarget


def loop(gui: GUI):
    while not gui.stopped:
        try:
            if 's0urce.io' not in hook.driver.current_url:
                hook.driver.get("http://s0urce.io")
            if gui.AutoTypeEnable.enabled:
                AutoType.call(gui.AutoTypeKeyDelay.value, gui.AutoTypeReturnDelay.value)
            if gui.AutoHackMsgEnable.enabled:
                AutoHackMsg.call()
            """
            if gui.AutoTarget.enabled:
                AutoTarget.call(gui.TargetPriority.get_selected_index())
            """
        except selenium_exceptions.WebDriverException as e:
            logger.warning("Reloading driver due to WebDriverException:{}".format(e))
            hook.driver = webdriver.Chrome("assets\\driver.exe")
