from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys, os
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity import config_entity
from sensor.components import data_ingestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation
from sensor.components.model_trainer import ModelTrainer
from sensor.components.model_evaluation import ModelEvaluation
from sensor.components.model_pusher import ModelPusher
from sensor.pipeline import start_training_pipeline

if __name__ =="__main__":

    try:
        start_training_pipeline()
    except Exception as e:
        raise SensorException(e, sys)