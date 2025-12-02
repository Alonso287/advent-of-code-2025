import pytest
from part2 import part2

def test_main1():
    assert part2(0, 100) == 1
    assert part2(75, 100) == 1
    assert part2(99, 0) == 0
    assert part2(50, 50) == 1
    assert part2(0, 50) == 0
    assert part2(75, 25) == 1
    assert part2(25, 75) == 1
    assert part2(0, 99) == 0
    assert part2(1, 101) == 1
    assert part2(99, 0) == 0
    assert part2(99, 2) == 1

def test_main2():
    assert part2(0,-1) == 0
    assert part2(25, -75) == 1
    assert part2(0, -100) == 1
    assert part2(1, -2) == 1
    assert part2(50,-50) == 1
    assert part2(50, -51) == 1
    assert part2(99,-100) == 1
