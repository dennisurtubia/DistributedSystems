# Dennis Felipe Urtubia
# Neste código se encontra as implementacoes dos métodos que são acessados de forma remota

import Pyro4
from Database import Database

@Pyro4.expose
class Controller:
    database = Database()
    database.create_table()

    def create_curso(self, curso):
        conn = self.database.create_connection()
        cursor = conn.cursor()

        sql = ''' INSERT INTO `Curso` (codigo, nome) VALUES (?, ?); '''

        cursor.execute(sql, curso)
        conn.commit()
        conn.close()
        return cursor.lastrowid

    def create_disciplina(self, disciplina):
        conn = self.database.create_connection()
        cursor = conn.cursor()

        sql = ''' INSERT INTO `Disciplina` (codigo, nome, professor, cod_curso)
                    VALUES (?, ?, ?, ?); '''

        cursor.execute(sql, disciplina)
        conn.commit()
        conn.close()
        return cursor.lastrowid

    def create_matricula(self, matricula):
        conn = self.database.create_connection()
        cursor = conn.cursor()

        sql = ''' INSERT INTO `Matricula` (ra, cod_disciplina, ano, semestre, nota, faltas)
                    VALUES (?, ?, ?, ?, ?, ?); '''

        cursor.execute(sql, matricula)
        conn.commit()
        conn.close()
        return cursor.lastrowid

    def get_nota_by_aluno(self, ra):
        conn = self.database.create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT cod_disciplina, nota FROM `Matricula` WHERE ra=?", (ra, ))
        rows = cursor.fetchall()
        return rows

    def update_nota(self, nota, ra, cod_disciplina):
        conn = self.database.create_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE `Matricula` SET nota = ? WHERE ra = ? AND cod_disciplina = ?", (nota, ra, cod_disciplina, ))
        conn.commit()

        return "SUCCESS"

    def get_notas_faltas_by_ano_semestre(self, ano, semestre, disciplina):
        conn = self.database.create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT faltas, nota FROM `Matricula` WHERE ano=? AND semestre=? AND cod_disciplina=?", (ano, semestre, disciplina, ))
        rows = cursor.fetchall()
        return rows

    def delete_matricula(self, ra, cod_disciplina, ano, semestre):
        conn = self.database.create_connection()
        cursor = conn.cursor()

        sql = ''' DELETE FROM `Matricula` WHERE ra = ? AND cod_disciplina = ? AND ano = ? AND semestre = ? '''

        cursor.execute(sql, (ra, cod_disciplina, ano, semestre, ))
        conn.commit()
