def from_gibrish_to_hebrew_fix(string):

    if string is None or len(string) == 0:
        return None

    if ord(string[0]) < 128: #english
        return string
    if ord(string[0]) < 255: #gibrish
        return string.encode('cp1252').decode('cp1255', errors='replace')
	#if ord(str[0]) > 256 : #unicode already


def is_number(num_string):
    try:
        float(num_string)
        return True
    except ValueError:
        return False
