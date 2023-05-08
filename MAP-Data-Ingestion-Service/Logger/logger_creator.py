import logging
import sys

#Remember that when you create the logger object, you can't perform any computing in the info(). You have to log one single value
def create_logger():
    root = logging.getLogger('MAP-DATA-INGESTION-SERVICE')
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    if not root.hasHandlers():
        root.addHandler(handler)
    return root