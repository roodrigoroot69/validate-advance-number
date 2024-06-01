from phones.validations import (
    validate_sign,
    validate_lada,
    is_valid_phone_number,
    is_valid_length,
    format_number
)


INVALID_PHONE = "Invalid"


def check_number(phones: list) -> str:
    result_phones = []
    for phone in phones:
        try:
            validate_sign(phone)
            validate_lada(phone)
            is_valid_phone_number(phone)
            is_valid_length(phone)

        except Exception as error:
            print(f"Error: {error}")
            result_phones.append(INVALID_PHONE)
        result_phones.append(format_number(phone))
    return result_phones
