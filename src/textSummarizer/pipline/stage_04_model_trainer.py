from textSummarizer.configuration.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logger import logger
from textSummarizer.exception import CustomeException
import sys

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:   
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise CustomeException(e,sys)