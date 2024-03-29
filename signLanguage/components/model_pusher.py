import sys
from signLanguage.configuration.s3_operations import S3Operation
from signLanguage.entity.artifacts_entity import (ModelPusherArtifact,
                                                  ModelTrainerArtifact)
from signLanguage.entity.config_entity import ModelPusherConfig
from signLanguage.exception import SignException
from signLanguage.logger import logging


class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig,
                 model_trainer_artifact: ModelTrainerArtifact,
                 s3: S3Operation):
        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifact = model_trainer_artifact
        self.s3 = s3

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        """
        Method name: initiate_model_pusher

        Description: This method initiates the model pusher.

        Returns:
            ModelPusherArtifact: Model pusher artifact
        """
        logging.info(
            "Entered initiate_model_pusher method of ModelPusher class")
        try:
            # Uploading the best model to s3
            self.s3.upload_file(
                self.model_trainer_artifact.trained_model_file_path,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME,
                remove=False
            )
            logging.info("Uploading the best model to s3 bucket")
            logging.info("Exited the initiate_model_pusher method of ModelPusher class")
            
            
            # Saving the model pusher artifacts
            model_pusher_artifact = ModelPusherArtifact(
                bucket_name=self.model_pusher_config.BUCKET_NAME,
                s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH
            )
            return model_pusher_artifact
        except Exception as e:
            raise SignException(e, sys)
