#Cantidad de jugadores por universidad
def prueba():
    return """(select uni.nombre as universidad, count(jug.nombre) as cantidad
        from universidad uni join jugador jug on (jug.id_universidad = uni.id)
        where uni.nombre <> 'None'
        group by uni.nombre
        order by cantidad desc
        limit 40)
        """

def edad_partidos():
    return """select tempo.edad as edad, count(tempo.p_jugados) as cantidad
        from temporada tempo
        group by tempo.edad
        order by tempo.edad desc"""

def net_rating():
    return """select eq.nombre as equipo, avg(tempo.net_rating) as cantidad
    from temporada tempo join equipo eq on(tempo.id_equipo = eq.id)
    group by eq.nombre
    order by eq.nombre asc"""
    
def puntos_por_jugador():
    return """select jug.nombre, round(avg(tempo.puntos)) as puntos
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by puntos desc"""
    
def rebotes_por_jugador():
    return """select jug.nombre, round(avg(tempo.rebotes)) as rebotes
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by rebotes desc"""
    
def asistencias_por_jugador():
    return """select jug.nombre, round(avg(tempo.asistencias)) as asistencias
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by asistencias desc"""
    
def net_rating_por_jugador():
    return """select jug.nombre, round(avg(tempo.net_rating)) as net_rating
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by net_rating desc"""
    

def reb_ofensivo_por_jugador():
    return """"""

# Consultas Giancarlo

def nacionalidad_1996():
    return """select pa.nombre as pais, count(pa.id) as total
    from pais pa join jugador ju on (pa.id=ju.id_pais) join temporada tem on (ju.id=tem.id_jugador)
    where tem.anio = '1996-97'
    group by pais
    order by total desc
limit 5"""



def nacionalidad_2008():
    return """select pa.nombre as pais, count(pa.id) as total
    from pais pa join jugador ju on (pa.id=ju.id_pais) join temporada tem on (ju.id=tem.id_jugador)
    where tem.anio = '2008-09'
    group by pais
    order by total desc
limit 10"""

def nacionalidad_2019():
    return """select pa.nombre as pais, count(pa.id) as total
    from pais pa join jugador ju on (pa.id=ju.id_pais) join temporada tem on (ju.id=tem.id_jugador)
    where tem.anio = '2019-20'
    group by pais
    order by total desc
limit 10"""


def estatura_rebotes():
    return """select  avg(rebotes) as rebotes, estatura as estatura
        from temporada
        group by estatura
        order by estatura asc"""


def net_rating():
    return """select eq.nombre as equipo, avg(tempo.net_rating) as cantidad
    from temporada tempo join equipo eq on(tempo.id_equipo = eq.id)
    group by eq.nombre
    order by eq.nombre asc"""


def puntos_por_jugador():
    return """select jug.nombre, round(avg(tempo.puntos)) as puntos
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by puntos desc"""


def rebotes_por_jugador():
    return """select jug.nombre, round(avg(tempo.rebotes)) as rebotes
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by rebotes desc"""


def asistencias_por_jugador():
    return """select jug.nombre, round(avg(tempo.asistencias)) as asistencias
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by asistencias desc"""


##
def net_rating_por_jugador():
    return """select jug.nombre, round(avg(tempo.net_rating)) as net_rating
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by net_rating desc"""


def reb_def_por_jugador():
    return """select jug.nombre, avg(tempo.reb_defensivo) as reb_defensivo
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by reb_defensivo desc"""


def reb_ofensivo_por_jugador():
    return """select jug.nombre, avg(tempo.reb_ofensivo) as reb_ofensivo
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by reb_ofensivo desc"""


def uso():
    return """select jug.nombre, avg(tempo.participacion) as participacion
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by participacion desc"""


def tiro_real():
    return """select jug.nombre, avg(tempo.tiro_real) as tiro_real
    from jugador jug join temporada tempo on (tempo.id_jugador = jug.id)
    group by jug.nombre
    order by tiro_real desc"""


########
def univ_net_rating():
    return """(select uni.nombre as universidad, avg(tempo.net_rating) as cantidad
        from universidad uni join jugador jug on (jug.id_universidad = uni.id)
 		join temporada tempo on (jug.id = tempo.net_rating)
        group by uni.nombre
        order by cantidad desc)"""


def univ_puntos():
    return """(select uni.nombre as universidad, avg(tempo.puntos) as puntos
        from universidad uni join jugador jug on (jug.id_universidad = uni.id)
 		join temporada tempo on (jug.id = tempo.net_rating)
        group by uni.nombre
        order by puntos desc)"""


def univ_rebs():
    return """(select uni.nombre as universidad, avg(tempo.rebotes) as rebotes
        from universidad uni join jugador jug on (jug.id_universidad = uni.id)
 		join temporada tempo on (jug.id = tempo.net_rating)
        group by uni.nombre
        order by rebotes desc)"""


def univ_asis():
    return """(select uni.nombre as universidad, avg(tempo.asistencias) as asistencias
        from universidad uni join jugador jug on (jug.id_universidad = uni.id)
 		join temporada tempo on (jug.id = tempo.net_rating)
        group by uni.nombre
        order by asistencias desc)"""


def univ_pj():
    return """(select uni.nombre as universidad, avg(tempo.p_jugados) as p_jugados
        from universidad uni join jugador jug on (jug.id_universidad = uni.id)
 		join temporada tempo on (jug.id = tempo.net_rating)
        group by uni.nombre
        order by p_jugados desc)"""


def univ_uso():
    return """(select uni.nombre as universidad, avg(tempo.participacion) as participacion
        from universidad uni join jugador jug on (jug.id_universidad = uni.id)
 		join temporada tempo on (jug.id = tempo.net_rating)
        group by uni.nombre
        order by participacion desc)"""


















