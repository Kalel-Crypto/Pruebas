from calculadora import Calculadora

def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

def test_imprimir(capsys):
    calc = Calculadora()
    calc.imprimir("Hola, mundo!")
    captured = capsys.readouterr()
    assert captured.out == "Hola, mundo!\n"


    