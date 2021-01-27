from lib.Core import hook
from lib import logger
from random import randint


def call(TargetPriorityIndex):
    if not hook.hack_available():
        if hook.target_list_window.is_displayed():
            if TargetPriorityIndex == 0:  # First in list
                loop_click(hook.target_list, 0, 1)
            if TargetPriorityIndex == 1:  # Last in list
                loop_click(hook.target_list, -1, -1)
            if TargetPriorityIndex == 2:  # Random
                while True:
                    random_target_index = randint(0, len(hook.target_list) - 1)
                    if target_clicked(hook.target_list[random_target_index]):
                        break
                    else:
                        del hook.target_list[random_target_index]
                    if len(hook.target_list) == 0:
                        logger.debug("Can't AutoTarget because there's no target can be clicked")
                        break
        else:
            logger.debug("Can't AutoTarget because there's no target list window")
    else:
        logger.debug("Can't AutoTarget because you are already hacking")


def target_clicked(target):
    if target.is_displayed() and target.is_enabled():
        target.click()
        return True
    else:
        return False


def loop_click(target_list, start, step):
    current_target_index = start
    while True:
        if target_clicked(target_list[current_target_index]):
            break
        if current_target_index >= len(target_list):
            logger.debug("Can't AutoTarget because there's no target can be clicked")
            break
        current_target_index += step
