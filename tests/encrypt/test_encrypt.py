import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("hello world", 3) == "leh_dlrow ol"
    assert encrypt_message("hello world", 5) == "olleh_dlrow "

    assert encrypt_message("hello world", 13) == "dlrow olleh"

    with pytest.raises(TypeError):
        encrypt_message("hello world", "invalid_key")
    with pytest.raises(TypeError):
        encrypt_message(123, 3)
