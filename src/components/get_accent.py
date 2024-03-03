from src.exception import CustomException
from src.logger import logger
import sys

# Define a function to get the top-level domain (TLD) based on the user's input accent
def get_accent(user_input):
    
    try:
        accent_input = {
    
            'American': 'us',
            'Australian': 'com.au',
            'British': 'co.uk',
            'Canadian': 'ca',
            'Indian': 'co.in',
            'Spanish': 'es'
        }

        tld = accent_input.get(user_input)
        return tld
    
    except Exception as e:
        raise CustomException ( e, sys)


# Define a function to get the list of available accents
def get_accent_message():
    
    try:
        accent = ['American', 'Australian', 'British', 
                  'Canadian', 'Indian', 'Spanish']
        return accent
    
    except Exception as e:
        raise CustomException ( e, sys)