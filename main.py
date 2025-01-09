from textSummarizer.pipline.stage_01_data_ingestion import DataIngestionPipeline

from textSummarizer.logger import logger
from textSummarizer.exception import CustomeException

import sys

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Completed <<<<<<<<<<<<\n\nX====================X")
except Exception as e:
    raise CustomeException(e,sys)


