import os, sys
from src.exception import CustomException
from src.logger import logger
from src.constants import TEXT_FILE_NAME, CURRENT_TIME_STAMP
from src.entity.config_entity import ttsConfig
from gtts import gTTS
import base64


class TTSapplication():
    def __init__(self, app_config=ttsConfig()) -> None:
        """
        Constructor for TTSapplication class.
        Initializes class attributes based on provided configuration.

        Args:
            app_config (ttsConfig, optional): Configuration entity for the application. Defaults to ttsConfig().
        """
        try:
            self.app_config = app_config
            self.artifact_dir = app_config.artifact_dir
            self.audio_dir = app_config.audio_dir
            self.text_dir = app_config.text_dir
        
        except Exception as e:
            raise CustomException(e, sys)
    
    
    def text2speech(self, text, accent):
        """
        Convert text to speech.

        Args:
            text (str): Input text to be converted.
            accent (str): Accent or dialect for the speech.

        Returns:
            bytes: Base64 encoded representation of the converted audio file.
        """
        try:
            text_filename = TEXT_FILE_NAME
            text_file_path = os.path.join(self.text_dir, text_filename)
            os.makedirs(self.text_dir, exist_ok=True)
            with open(text_file_path, "a+") as file:
                file.write(f'\n{text}')
            
            # Convert text to speech using gTTS library
            tts = gTTS(text=text, lang='en', tld=accent, slow=False)
            
            file_name = f"converted_file{CURRENT_TIME_STAMP}.mp3"
            os.makedirs(self.audio_dir, exist_ok=True)
            audio_path = os.path.join(self.audio_dir, file_name)

            tts.save(audio_path)

            with open(audio_path, "rb") as file:
                my_string = base64.b64encode(file.read())
            
            return my_string
        
        except Exception as e:
            raise CustomException(e, sys)