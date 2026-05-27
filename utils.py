"""Modul zawierajacy funkcje pomocnicze kalkulatora."""


def add(a: int, b: int) -> int:
    """Zwraca sume dwoch liczb calkowitych."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Zwraca roznice dwoch liczb calkowitych."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Zwraca iloczyn dwoch liczb calkowitych."""
    return a * b


def divide(a: int, b: int) -> float:
    """Zwraca iloraz dwoch liczb calkowitych."""
    if b == 0:
        raise ZeroDivisionError("Nie mozna dzielic przez zero.")
    return a / b


def to_binary(n: float) -> str:
    """Konwertuje liczbe naturalna od 0 do 100 na postac binarna.

    Rzuca ValueError w przypadku blednego zakresu lub typu danych.
    """
    if isinstance(n, float) and not n.is_integer():
        raise ValueError("Liczba musi byc liczba naturalna (calkowita).")

    int_n = int(n)

    if int_n < 0 or int_n > 100:
        raise ValueError("Liczba spoza zakresu [0, 100].")

    return bin(int_n)[2:]
