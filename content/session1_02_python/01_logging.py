#Lukas Steinwender

#%%imports
import logging

logger = logging.getLogger()                    #root logger
local_logger = logging.getLogger(__name__)      #locoal logger
logging.basicConfig(level=logging.WARNING)      #only show warnings
local_logger.setLevel(logging.DEBUG)            #all logged messages

#%%main
def main():
    logger.info("hidden")
    logger.warning("shown")
    local_logger.info("not hidden")
    local_logger.warning("shown")

if __name__ == "__main__":
    main()