#
#
#   Zip cracker
#
#

import pyzipper
import typer
import string

from utils import brute_force


def _character_set_for_zip_password():
    # Uppercase letters (A-Z)
    uppercase = string.ascii_uppercase
    # Lowercase letters (a-z)
    lowercase = string.ascii_lowercase
    # Numbers (0-9)
    digits = string.digits
    # Special characters
    special_chars = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~`"

    return uppercase + lowercase + digits + special_chars


def _verify_zip_password(zip_path, password):
    with pyzipper.AESZipFile(zip_path) as zf:
        zf.setpassword(password.encode())

        try:
            zf.testzip()
        except RuntimeError:
            return False
        else:
            return True


def crack_zip(file_path: str, min_password_length: int | None = None, max_password_length: int | None = None,
              progress: bool = False):
    character_set = _character_set_for_zip_password()

    for password_to_try in brute_force(character_set, min_password_length, max_password_length, progress=progress):
        if _verify_zip_password(file_path, password_to_try):
            print(f"Password found: {password_to_try}")
            return


if __name__ == "__main__":
    typer.run(crack_zip)
