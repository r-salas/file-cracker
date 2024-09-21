#
#
#   File cracker
#
#

import typer


def main(file_path: str, min_password_length: int | None = None, max_password_length: int | None = None,
         progress: bool = False):
    if file_path.endswith(".pdf"):
        from pdf_cracker import crack_pdf
        crack_pdf(file_path, min_password_length, max_password_length, progress)
    elif file_path.endswith(".zip"):
        from zip_cracker import crack_zip
        crack_zip(file_path, min_password_length, max_password_length, progress)
    else:
        print("Unsupported file type")
        raise typer.Exit()


if __name__ == "__main__":
    typer.run(main)
