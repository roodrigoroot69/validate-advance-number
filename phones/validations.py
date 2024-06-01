import re

from phones.exceptions import (
    IsNotValidNumberException,
    IsNotValidLengthException,
    InvalidLadaExeception,
    InvalidSignException,
    IsNotValidNumberException
    )


LADAS = {
    '+1': 11,
    '+44': 12,
    '+91': 12,
    '+86': 13,
    '+49': 12
}

def format_number(phone):
    return phone.replace("-","").replace("(","").replace(")", "").replace(" ","").strip()

def is_valid_length(phone: str):
    split_number = separete_number(phone)
    lada = split_number[0]
    number = format_number(phone[1::])
    if not LADAS.get(lada) == len(number):
        raise IsNotValidLengthException("The length is not valid")

def is_valid_lada(lada: str):
    return bool(LADAS.get(lada))

def is_valid_phone_number(phone: str) -> bool:
    pattern = re.compile(r'^[\d\s\-\(\)]+$')
    if not bool(pattern.match(phone[1::])):
        raise IsNotValidNumberException("Is not a valid number")

def separete_number(phone: str):
    if phone.find("-"):
        phone = phone.replace("-", " ")
    return phone.split()


def validate_lada(phone: str):
    split_phone = separete_number(phone)
    lada = split_phone[0]
    if is_valid_lada(lada):
        return True
    raise InvalidLadaExeception("Invalid Lada")

def validate_sign(phone: str):
    if not phone.startswith("+"):
        raise InvalidSignException("Sign missing")
    return True

