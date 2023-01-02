from sensor.exception import SensorException
import sys, os
from sensor.pipeline.training_pipeline import start_training_pipeline

if __name__ =="__main__":

    try:
        start_training_pipeline()
    except Exception as e:
        raise SensorException(e, sys)