from datetime import datetime

# Define constants related to the application
APPLICATION_NAME = "text_to_speech"
ARTIFACT_DIR_KEY = "artifact"
AUDIO_DIR = "audio_file"
TEXT_DIR = "text_file"
TEXT_FILE_NAME = "user_input.txt"

time_stamp = "%Y-%m-%d %H%M%S"
CURRENT_TIME_STAMP = f"{datetime.now().strftime(time_stamp)}"