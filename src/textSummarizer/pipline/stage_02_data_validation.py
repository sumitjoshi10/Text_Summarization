from textSummarizer.configuration.configuration import ConfigurationManager
from textSummarizer.entity import DataValidationConfig
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logger import logger
from textSummarizer.exception import CustomeException
import sys

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            validation_status = data_validation.validate_all_files_exist()

            return validation_status
        except Exception as e:
            raise CustomeException(e,sys)