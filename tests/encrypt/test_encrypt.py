from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, "2") or encrypt_message("message", "key")
    
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("test", 1) == "t_tse"
    assert encrypt_message("message", -1) == "egassem"
    assert encrypt_message("message", 4) == "ega_ssem"
