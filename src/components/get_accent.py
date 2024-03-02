from src.exception import CustomException
from src.logger import logger
import sys

# Define a function to get the top-level domain (TLD) based on the user's input accent
def get_accent(user_input):
    
    try:
        accent_input = {
            'Irish': 'ie',
            'South African': 'co.za',
            'Indian': 'co.in',
            'Australian': 'com.au',
            'Canadian': 'ca',
            'British': 'co.uk',
            'Spanish': 'es'
        }
        tld = accent_input.get(user_input)
        return tld
    
    except Exception as e:
        raise CustomException ( e, sys)


# Define a function to get the list of available accents
def get_accent_message():
    
    try:
        accent = ['Irish', 'South Africa',  'Indian','Australian', 
                  'Canadian',  'British','Spanish' ]
        return accent
    
    except Exception as e:
        raise CustomException ( e, sys)