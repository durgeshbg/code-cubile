from working import convert
import pytest

def test_convert_dayshift():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 4:47 PM") == "10:30 to 16:47"
    
def test_convert_nightshift():
    assert convert("11 PM to 7 AM") == "23:00 to 07:00"
    assert convert("10:30 PM to 5:47 AM") == "22:30 to 05:47"
 