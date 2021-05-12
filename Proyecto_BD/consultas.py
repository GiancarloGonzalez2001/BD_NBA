#Cantidad de jugadores por universidad
def prueba():
    return """select uni.nombre as universidad, count(jug.nombre) as cantidad
        from universidad uni join jugador jug on (jug.id_universidad = uni.id)
        group by uni.nombre
        order by cantidad desc"""

# def consulta():
#     return """consulta escrita en sql"""