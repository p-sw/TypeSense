from os import path as file
from lib import logger
from lib.gui import GUI
from lib.Core import core
from threading import Thread

if not file.exists("assets\\driver.exe"):
    raise FileNotFoundError
logger.debug("Driver Exists")

logger.info("GUI Initializing")
gui = GUI()
logger.info("Starting core loop")
core_th = Thread(target=core.loop, args=[gui])
core_th.start()
logger.info("GUI Starting")
gui.run()
core_th.join()
