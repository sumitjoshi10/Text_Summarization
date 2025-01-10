from textSummarizer.pipline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipline.stage_04_model_trainer import ModelTrainerPipeline

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


STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_validation = DataValidationPipeline()
    validation_status = data_validation.main()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Completed <<<<<<<<<<<<\n\nX====================X")
except Exception as e:
    raise CustomeException(e,sys)

STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} started <<<<<<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Completed <<<<<<<<<<<<\n\nX====================X")
except Exception as e:
    raise CustomeException(e,sys)


STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} started <<<<<<<<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>>>Stage {STAGE_NAME} Completed <<<<<<<<<<<<\n\nX====================X")
except Exception as e:
    raise CustomeException(e,sys)

