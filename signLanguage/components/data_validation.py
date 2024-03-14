import os
import sys
import shutil
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import DataValidationConfig
from signLanguage.entity.artifacts_entity import (DataIngestionArtifact,
                                                  DataValidationArtifact)


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig = DataValidationConfig()
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SignException(e, sys)

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(
                self.data_ingestion_artifact.feature_store_path)
            os.makedirs(
                self.data_validation_config.data_validation_dir, exist_ok=True)
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    break
                else:
                    validation_status = True
            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                f.write(f"Validation Status: {validation_status}")
            return validation_status

        except Exception as e:
            raise SignException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        logging.info(
            "Entered data validation artifact method of DataValidation Class.")
        try:
            status = self.validate_all_files_exist()

            data_validation_artifact = DataValidationArtifact(
                validation_status=status
            )

            logging.info(
                "Exited initiate_data_validation_method of DataValidation Class")
            logging.info(
                f"Data validation artifact: {data_validation_artifact}")

            if status:
                shutil.copy(
                    self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact
        except Exception as e:
            raise SignException(e, sys)
