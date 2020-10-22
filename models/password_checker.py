import re
from typing import Optional

from pydantic import BaseModel, root_validator


class PasswordChecker(BaseModel):
    password: Optional[str]
    password_confirm: Optional[str]
    password_strength: Optional[int]

    @root_validator
    def check_password(cls, values):
        pw1, pw2 = values.get('password'), values.get('password_confirm')
        if pw1 is None or pw2 is None:
            raise ValueError('Null password')
        if pw1 != pw2:
            raise ValueError('passwords do not match')
        password_length = len(pw1)
        if password_length < 8:
            raise ValueError('Very short password')
        digit_error = re.search("\d", pw1) is None
        uppercase_error = re.search(r"[A-Z]", pw1) is None
        lowercase_error = re.search(r"[a-z]", pw1) is None
        symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', pw1) is None
        password_ok = not (digit_error or uppercase_error or lowercase_error or symbol_error)
        if not password_ok:
            raise ValueError('Not ok password')
        if password_length < 15:
            password_strength = 'ok'
        elif 15 <= password_length < 20:
            password_strength = 'good'
        else:
            password_strength = 'very good'
        values.update({'password_strength': password_strength})
        return values
