import shutil

def is_git_installed() -> bool:
    """
    Данная функция проверяет скачан ли git, так как большинство OSINT модулей находятся только на GITHUB
    Прямой поддержки из PyPy нет, поэтому будем довольствоваться тем, что есть.
    :return: Возвращает правду, если git скачан, в ином случае ложь.
    """
    return shutil.which('git') is not None

print(is_git_installed())