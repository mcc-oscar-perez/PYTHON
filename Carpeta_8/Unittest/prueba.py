import unittest
import cambia_texto

class probarCambiaTexto(unittest.TestCase):
    
    def test_mayusculas(self):
        palabra  = 'Buen dia'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado,'BUEN DIA')
        
if __name__ == '__main__':
    unittest.main()
    