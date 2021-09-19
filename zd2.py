#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("aeiouy")
    d = 0

    # ввод строки
    a = input("Введите строку: ")
    for i in a:
        if i in u:
            d += 1
    print("Количество глассных: ", d)
