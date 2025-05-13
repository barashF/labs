import re

phone_pattern = re.compile(
    r'^(\+7|8)(?:'
    r'\(\d{3}\)\d{3}-\d{2}-\d{2}'  # Формат со скобками: +7(XXX)XXX-XX-XX
    r'|'                            # ИЛИ
    r'[\s-]\d{3}[\s-]\d{3}[\s-]\d{2}[\s-]\d{2}'  # Формат с пробелами/тире
    r')$'
)

# Примеры валидных номеров:
valid_numbers = [
    "+7(912)345-67-89",
    "8 912 345 67 89",
    "+7-912-345-67-89",
    "8(912)345-67-89"
]

# Примеры невалидных номеров:
invalid_numbers = [
    "+79123456789",      # Отсутствуют разделители
    "8(091)234-56-78",   # Код начинается с 0
    "+7(912)345-6X-89",  # Содержит букву
    "7(912)345-67-89"    # Начинается с 7 вместо +7 или 8
]

for num in valid_numbers:
    assert phone_pattern.match(num), f"Ошибка: {num} считается невалидным"

for num in invalid_numbers:
    assert not phone_pattern.match(num), f"Ошибка: {num} считается валидным"


email_pattern = re.compile(
    r'^[a-zA-Z0-9](?:[a-zA-Z0-9._-]*[a-zA-Z0-9])?'  # Имя пользователя
    r'@' 
    r'(?:[a-zA-Z0-9-]+\.)+'                          # Домен
    r'[a-zA-Z]{2,6}$'                                 # Доменная зона
)

# Примеры валидных email:
valid_emails = [
    "test.email@example.com",
    "user_name-123@sub.domain.org",
    "u@a.co"
]

# Примеры невалидных email:
invalid_emails = [
    ".test@example.com",
    "user..name@example.com",
    "user@.com"
]

for email in valid_emails:
    assert email_pattern.match(email), f"Ошибка: {email} считается невалидным"

for email in invalid_emails:
    assert not email_pattern.match(email), f"Ошибка: {email} считается валидным"


ip_pattern = re.compile(
    r'\b(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)'  # Числа от 0 до 255
    r'(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}\b'
)

def replace_ip(text):
    return ip_pattern.sub("***.***.***.***", text)

# Пример:
input_text = "User connected from 192.168.1.5 at 14:23, backup from 10.0.0.1 also logged."
output_text = replace_ip(input_text)
print(output_text)  # User connected from ***.***.***.*** at 14:23, backup from ***.***.***.*** also logged.



def parse_url_params(url):
    params = {}
    query = re.search(r'\?(.*?)(#|$)', url)  # Игнорируем часть после #
    if not query:
        return params
    
    pairs = re.findall(r'([^&=]+)=([^&]*)', query.group(1))
    for key, value in pairs:
        key = re.sub(r'%[0-9A-Fa-f]{2}', lambda m: chr(int(m.group(0)[1:], 16)), key)
        value = re.sub(r'%[0-9A-Fa-f]{2}', lambda m: chr(int(m.group(0)[1:], 16)), value)
        if key in params:
            params[key].append(value)
        else:
            params[key] = [value]
    return params

# Пример:
url = "https://my.site/page?id=42&id=43&user=test#anchor"
print(parse_url_params(url))  # {'id': ['42', '43'], 'user': ['test']}