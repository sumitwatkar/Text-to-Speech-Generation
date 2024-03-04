from src.components.get_accent import get_accent
from src.components.text_to_speech import TTSGeneration

def main():
    try:
        text_input = '''The objective of this project is to enable users to easily convert written text into high-quality, 
                    natural-sounding audio output.'''
        
        accent_input = "American"
        
        accent = get_accent(accent_input)
        
        print("Selected accent:", accent)
        
        TTSGeneration().text_to_speech(text_input, accent)
        
        print("Text to Speech converted successfully.")
    
    except Exception as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    main()