from django.conf import settings
from random import choice
from string import ascii_letters, digits


'''
    random.choice random return item of sequence
    choice("abc") > "a"
    choice("abc") > "c"
    choice(['a','b','c']) > 'b'
'''


'''
    if "MAXIMUM_URL_CHARS" in settings:
        return settings.MAXIMUM_URL_CHARS
    else:
        return 7
'''
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

'''
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_letters = ascii_lowercase + ascii_uppercase
    digits = '0123456789'
'''
AVAILABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAILABLE_CHARS):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )
    
def create_shortened_url(model_instance):
    random_code = create_random_code()
    model_class = model_instance.__class__
    
    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortened_url(model_instance)

    return random_code