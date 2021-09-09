"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
 из чисел в диапазоне от 2 до 9.
"""
str_out = {}
interval_natural = (n for n in range(2, 100))
for natural in interval_natural:
    interval_decimal = (n for n in range(2, 10))
    for dec in interval_decimal:
        if not natural % dec:
            if str_out.get(dec) is not None:
                str_out.setdefault(dec, str_out.pop(dec) + 1)
            else:
                str_out.setdefault(dec, 1)
for key in str_out.keys():
    print(f"{key}-и(м) кратно {str_out[key]} чисел из дапазона 2-99")
