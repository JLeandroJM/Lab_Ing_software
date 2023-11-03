import csv
# El programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# regio,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# El DNI debe ser valido (8 digitos)

class CalculaGanador:
    # 1.Renombrar de variables y metodos
    def leer_datos(self):
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            votos = csv.reader(csvfile) #Renombrrado datareader por votos
            # 2.Extraccion de metodo (en este caso se usa directamente uno de python)
            return list(votos)
    def calcular_ganador(self, data):
        votosxcandidato = {}
        for fila in data:
            # 3.Simplificacion de condicionales
            if self.validar_voto(fila):
                votosxcandidato[fila[4]] = votosxcandidato.get(fila[4], 0) + 1
        
        total_votos = sum(votosxcandidato.values())
        

        ganador_o_segunda_vuelta = []

        for candidato, votos in votosxcandidato.items():
            if votos >= total_votos / 2:
                ganador_o_segunda_vuelta.append(candidato)

                
        # 4.Eliminar codigo duplicado
        self.mostrar_votosxcandidato(votosxcandidato, total_votos)
        return ganador_o_segunda_vuelta
    
    def mostrar_votosxcandidato(self, votosxcandidato, total_votos):
        for candidato, votos in votosxcandidato.items():
            if votos > total_votos / 2:
                return [f'El ganador es: {candidato}']
            print(f'candidato: {candidato} votos validos: {votos}')

    def validar_voto(self, fila):
        return fila[5] == '1' and len(fila[3]) == 8

c = CalculaGanador()
#c.calcularvotos(c.leerdatos())
datatest = [
    ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]
print(c.calcular_ganador(datatest))

#Pruebas unitarias


# Evaluacion del codigo resultante
'''
Para refactorizar el codigo utilizamos diferentes tecnicas:

renombrar variables y funciones: renombramos las funciones y variables para que sean
mas descriptivas.

Optimizacion de lectura de datos: se optimizo l lectura de datos utilikzando directamente la 
fucnion dada por la libreria

Simplificacion de condicionales: Se simplificó la condición dentro del bucle for al verificar si fila[5] 
es igual a '1' en lugar de verificar si no es igual a '0'

Eliminacion del codigo dulicado: se elimino un bucle que estaba de mas y no aportaba al funcionamiento
de la funcion


'''
