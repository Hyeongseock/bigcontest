import csv_utils
import logging as log
import pandas as pd
import mask
log.basicConfig(level=log.DEBUG)

if __name__ == "__main__" :
    log.info("main start")
    pd.DataFrame = mask.apply_masks()

    # 파일 경로
    root_path ="E:/NCsoft/champion_data/"
