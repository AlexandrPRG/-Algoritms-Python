"""1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


def get_hash(line_s: str):
    def alfabet_hash():
        return [hashlib.sha1(chr(smb).encode('utf-8')).hexdigest() for smb in range(97, 124)]
    """
    :param s: строка
    :return: количество подстрок
    """
    for symb in line_s:
        if not hashlib.sha1(symb.encode('utf-8')).hexdigest() in alfabet_hash():
            print("Строка содерижт неподдерживаемые символы")
            return -1
    return sum([1 for len_sub_line in range(1, len(line_s) + 1)
                    for start_sub_line in range(len_sub_line)]) - 1


if __name__ == '__main__':
    print(get_hash('sde'))