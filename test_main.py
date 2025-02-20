import pytest
from app.main import soma, multiplica

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_multiplica():
    assert multiplica(2, 3) == 6
    assert multiplica(-2, 3) == -6
