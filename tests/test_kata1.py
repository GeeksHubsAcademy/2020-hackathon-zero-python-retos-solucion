import pytest

from kata1.rps import quienGana

def test_no_sensible_minusculas():
    assert(quienGana('PiEdRa', 'PaPeL') == 'Perdiste!')

def test_piedra_vs_piedra():
	assert(quienGana('Piedra', 'Piedra') == 'Empate!')

def test_papel_vs_papel():
	assert(quienGana('Papel', 'Papel') == 'Empate!')

def test_tijeras_vs_tijeras():
	assert(quienGana('Tijeras', 'Tijeras') == 'Empate!')

def test_piedra_vs_papel():
	assert(quienGana('Piedra', 'Papel') == 'Perdiste!')

def test_papel_vs_tijeras():
	assert(quienGana('Papel', 'Tijeras') == 'Perdiste!')

def test_tijeras_vs_piedra():
	assert(quienGana('Tijeras', 'Piedra') == 'Perdiste!')

def test_piedra_vs_tijeras():
	assert(quienGana('Piedra', 'Tijeras') == 'Ganaste!')

def test_papel_vs_piedra():
	assert(quienGana('Papel', 'Piedra') == 'Ganaste!')

def test_tijeras_vs_papel():
	assert(quienGana('Tijeras', 'Papel') == 'Ganaste!')
    