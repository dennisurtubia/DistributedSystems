# Dennis Felipe Urtubia
# Neste código se encontram os Schemas que compõe o banco de dados,
# a funcao que retorna uma conexão com o banco e por fim a criacao das tableas

import sqlite3

sql_create_curso_table = """ CREATE TABLE IF NOT EXISTS Curso (
                                    codigo integer,
                                    nome text,

                                    PRIMARY KEY(codigo)
                                ); """

sql_create_disciplina_table = """ CREATE TABLE IF NOT EXISTS Disciplina (
                                    codigo text,
                                    nome text,
                                    professor text,
                                    cod_curso integer,

                                    PRIMARY KEY(codigo, cod_curso),
                                    FOREIGN KEY(cod_curso) REFERENCES Curso(codigo)
                                ); """

sql_create_aluno_table = """ CREATE TABLE IF NOT EXISTS Aluno (
                                    ra integer,
                                    nome text,
                                    periodo integer,
                                    cod_curso integer,

                                    PRIMARY KEY(ra, cod_curso),
                                    FOREIGN KEY(cod_curso) REFERENCES Curso(codigo)
                                ); """

sql_create_matricula_table = """ CREATE TABLE IF NOT EXISTS Matricula (
                                    ra integer,
                                    cod_disciplina text,
                                    ano integer,
                                    semestre integer,
                                    nota real,
                                    faltas integer,

                                    PRIMARY KEY(ra, cod_disciplina, ano, semestre),
                                    FOREIGN KEY(ra) REFERENCES Aluno(ra),
                                    FOREIGN KEY(cod_disciplina) REFERENCES Disciplina(codigo)
                                ); """

class Database:
    def create_connection(self):
        try:
            conn = sqlite3.connect('notas.db')
        except:
            print('Erro ao conectar ao banco de dados')

        return conn

    def create_table(self):
        conn = self.create_connection()

        self.cursor = conn.cursor()
        self.cursor.execute(sql_create_curso_table)
        self.cursor.execute(sql_create_disciplina_table)
        self.cursor.execute(sql_create_aluno_table)
        self.cursor.execute(sql_create_matricula_table)
