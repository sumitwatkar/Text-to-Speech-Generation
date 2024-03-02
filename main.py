from src.components.get_accent import get_accent, get_accent_message


accent_list = get_accent_message()

print(accent_list)

accent = accent_list[2]

tld = get_accent(accent)

print(tld)