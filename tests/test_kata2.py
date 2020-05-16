import pytest
import string

from kata2.rpg import RandomPasswordGenerator

def test_longitud_15():
	assert(len(RandomPasswordGenerator(15)) == 15)

def test_longitud_10():
	assert(len(RandomPasswordGenerator(10)) == 10)

def test_longitud_8():
	assert(len(RandomPasswordGenerator(8)) == 8)

def test_contraseña_contiene_letras():
	assert(chr in RandomPasswordGenerator(15) for chr in string.ascii_letters)

def test_contraseña_contiene_numeros():
	assert(chr in RandomPasswordGenerator(15) for chr in string.digits)

def test_contraseña_contiene_caracteres_especiales():
	assert(chr in RandomPasswordGenerator(15) for chr in string.punctuation)
    
def test_contraseña_contiene_letras():
	characters = string.ascii_letters + string.digits + string.punctuation
	assert(chr in RandomPasswordGenerator(15) for chr in characters)

def test_contraseña_compleja():
	characters = string.ascii_letters + string.digits + string.punctuation
	assert(chr in RandomPasswordGenerator(15) for chr in characters)
