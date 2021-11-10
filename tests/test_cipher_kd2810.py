from cipher_kd2810 import cipher_kd2810
from cipher_kd2810.cipher_kd2810 import cipher

import pytest

@pytest.mark.parametrize("example_str, example_shift, expected",[
    ("KevIn", 2, "MgxKp"),
    ("PerSAuD", 4, "TivWEyH"),
    ("macHInes", -5, "hVXCDiZn"),
    ("eagle", 9, "njpun"),
    ("EAGLE", -10, "uqwBu"),
    ("DaTa Sci", 2, "FcVc Uek")
])
def test_several_ciphers(example_str, example_shift, expected):
    result = cipher(example_str, example_shift)
    assert (result == expected)