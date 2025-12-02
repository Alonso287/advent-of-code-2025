import pytest
from parte2 import calcular_veces_por_0

def test_main1():
    assert calcular_veces_por_0(0, 100) == 1
    assert calcular_veces_por_0(75, 100) == 1
    assert calcular_veces_por_0(99, 0) == 0
    assert calcular_veces_por_0(50, 50) == 1
    assert calcular_veces_por_0(0, 50) == 0
    assert calcular_veces_por_0(75, 25) == 1
    assert calcular_veces_por_0(25, 75) == 1
    assert calcular_veces_por_0(0, 99) == 0
    assert calcular_veces_por_0(1, 101) == 1
    assert calcular_veces_por_0(99, 0) == 0
    assert calcular_veces_por_0(99, 2) == 1

def test_main2():
    assert calcular_veces_por_0(0,-1) == 0
    assert calcular_veces_por_0(25, -75) == 1
    assert calcular_veces_por_0(0, -100) == 1
    assert calcular_veces_por_0(1, -2) == 1
    assert calcular_veces_por_0(50,-50) == 1
    assert calcular_veces_por_0(50, -51) == 1
    assert calcular_veces_por_0(99,-100) == 1
