from working import convert
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert('')