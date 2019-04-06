def get_professores(cursor):
    cursor.execute(f'select nome, idprof from professor order by nome;')
    professor = cursor.fetchall()
    cursor.close()
    return professor

def get_titulo(cursor, titulo):
    cursor.execute(f'select professor.nome from professor where professor.Titulacao = {titulo};')
    titulo = cursor.fetchall()
    cursor.close()
    return titulo

def get_detalhes(cursor, professor):
    cursor.execute(f'select professor.nome, professor.DataNasc, professor.NomeMae, professor.Titulacao, disciplina.Nome, disciplina.curso, disciplina.CargaHoraria from professor, disciplina where professor.idprof = "{professor}" and professor.idprof = disciplina.idprof;')
    detalhes = cursor.fetchall()
    cursor.close()
    return detalhes

def get_cic(cursor, cic):
    cursor.execute(f'select disciplina.curso from disciplina where disciplina.curso = "{cic}"; ')
    acic = cursor.fetchall()
    cursor.close()
    return acic
