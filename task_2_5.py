"""5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером
 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме:
  по десять пар "код-символ" в каждой строке.
"""
START_CODE = 32
FINISH_CODE = 128
out_list = ''
step_out = 10
codes_symbols = {str(code):chr(code) for code in range(START_CODE, FINISH_CODE)}
for id, code_symbol in enumerate(codes_symbols):
    if id < step_out:
        out_list = out_list + f"{code_symbol}-{codes_symbols[code_symbol]} "
    else:
        print(out_list)
        out_list = f"{code_symbol}-{codes_symbols[code_symbol]} "
        step_out += 10
print(out_list)
