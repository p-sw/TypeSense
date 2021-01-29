from lib.gui import GUI
from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from lib import logger
from lib.Core import AutoType
from lib.Core import AutoHackMsg
from lib.Core import hook
from lib.Core import AutoPort
# from lib.Core import AutoTarget


def loop(gui: GUI):
    while not gui.stopped:
        try:
            if 's0urce.io' not in hook.driver.current_url:
                hook.driver.get("http://s0urce.io")
            if gui.AutoTypeEnable.enabled:
                AutoType.call(gui.AutoTypeKeyDelay.value, gui.AutoTypeReturnDelay.value)
            if gui.AutoHackMsgEnable.enabled and not AutoHackMsg.sent_msg:
                AutoHackMsg.call(gui.AutoHackMsgType.get_selected_index())
            """
            if gui.AutoTarget.enabled:
                AutoTarget.call(gui.TargetPriority.get_selected_index())
            """
            if gui.AutoPort.enabled and not AutoPort.port_clicked:
                AutoPort.call(gui.PortSelection.get_selected_index(), gui.PortDelay.value)
        except selenium_exceptions.WebDriverException as e:
            logger.warning("Ignoring WebDriverException:{}".format(e))
