# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
symbol_code = int(input("Введите номер буквы: "))
alfabet = symbol_code + 96
if 96 < alfabet < 123:
    print(symbol_code, '-я буква - это: ', chr(alfabet))
else:
    print("В английском алфавите 26 букв")
