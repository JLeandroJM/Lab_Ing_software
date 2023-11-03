import unittest
from prueba import CalculaGanador

class TestApp(unittest.TestCase):
    def test_calcular_ganador(self):
    # Se verifica que se calcule una ganador correctamente.  
    # Debería retornar el nombre del ganador "Aundrea Grace".    
        c = CalculaGanador()
        dataset = [['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]

        ganador = c.calcular_ganador(dataset)
        self.assertEqual(ganador, ['Aundrea Grace'])


    def test_empate(self):
        self.c = CalculaGanador()
        # Se verifica que se calcule una ganador correctamente.  
        # En este caso, como es un empate, aambos candidatos deberían ir a segunda vuelta
        dataset = [['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]

        ganadores = self.c.calcular_ganador(dataset)
        self.assertEqual(['Eddie Hinesley','Aundrea Grace'],ganadores)
        
    def dni_invalido(self):
        self.c = CalculaGanador()

        dataset = [['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017', 'Aundrea Grace', '1']
        ]

        ganadores = self.c.calcular_ganador(dataset)
        self.assertEqual(['Eddie Hinesley'],ganadores)
        

if __name__ == '__main__':
    unittest.main()