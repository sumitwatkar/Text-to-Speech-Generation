from dataclasses import dataclass
import os
from src.constants import *

# Get the current working directory
CURRECT_DIR = os.getcwd()

# Defining a dataclass for text-to-speech configuration
@dataclass
class ttsConfig:
    app_name: str = APPLICATION_NAME
    artifact_dir: str = os.path.join(CURRECT_DIR, app_name, ARTIFACT_DIR_KEY)
    audio_dir: str = os.path.join(artifact_dir, AUDIO_DIR)
    text_dir:str = os.path.join(artifact_dir, TEXT_DIR)