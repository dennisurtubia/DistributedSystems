# Dennis Felipe Urtubia
# Neste código se encontra a conexão com o Servico que disponibiliza os metodos que são acessados de forma remota

import Pyro4

def main():
    Pyro4.locateNS("127.0.0.1", 9090)
    controller = Pyro4.Proxy("PYRONAME:ControllerService")

    curso = (0, 'Ciencia da Computacao')
    disciplina = ('BCC36C', 'Sistemas Distribuidos', 'Rodrigo Campiolo', 0)
    matricula = (1923196, 'BCC36C', 2019, 2, 100, 0)

    controller.create_curso(curso)
    controller.create_disciplina(disciplina)
    controller.create_matricula(matricula)

    response = controller.get_nota_by_aluno(1923196)
    for row in response:
        print(row)

    print(controller.update_nota(90, 1923196, 'BCC36C'))

    response = controller.get_notas_faltas_by_ano_semestre(2019, 2, 'BCC36C')
    for row in response:
        print(row)

    controller.delete_matricula(1923196, 'BCC36C', 2019, 2)

if __name__ == "__main__":
    main()