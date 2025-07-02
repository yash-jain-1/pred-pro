# write test code for hello_world function in hello.py
import pytest

from hello import hello_world


def test_hello_world(capfd):
    hello_world()
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!\n"
