from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():
    assert encrypt_message("Message", 10) == "egasseM"
    assert encrypt_message("Message", 3) == "seM_egas"
    assert encrypt_message("Message", 4) == "ega_sseM"

    with raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Abcdef", None)

    with raises(TypeError, match="tipo inválido para message"):
        encrypt_message(None, 1)
