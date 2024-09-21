#
#
#  Crack password using brute force
#
#

import string

import typer
from pypdf import PdfReader
from pypdf.errors import WrongPasswordError

from utils import brute_force


def _verify_pdf_password(pdf_path, password):
    try:
        reader = PdfReader(pdf_path, password=password)
    except WrongPasswordError:
        return False
    else:
        return True


def _character_set_for_pdf_password():
    # Uppercase letters (A-Z)
    uppercase = string.ascii_uppercase
    # Lowercase letters (a-z)
    lowercase = string.ascii_lowercase
    # Numbers (0-9)
    digits = string.digits
    # Special characters
    special_chars = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~`"

    return uppercase + lowercase + digits + special_chars


def crack_pdf(file_path: str, min_password_length: int | None = None, max_password_length: int | None = None,
         progress: bool = False):
    character_set = _character_set_for_pdf_password()

    for password_to_try in brute_force(character_set, min_password_length, max_password_length, progress=progress):
        if _verify_pdf_password(file_path, password_to_try):
            print(f"Password found: {password_to_try}")
            return


if __name__ == "__main__":
    typer.run(crack_pdf)
