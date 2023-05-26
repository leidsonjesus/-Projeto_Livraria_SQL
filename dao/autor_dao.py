from model.autor import Autor
from database.conexao_factory import ConexaoFactory

class AutorDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()
        self.__autores: list[Autor] = list()

    def listar(self) -> list[Autor]:
        autores = list ()

        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM autores")
        resultados = cursor.fetchall()

        for result in resultados: 
            act = Autor(result[1], result[2], result[3], result[4])
            act.id = result[0]
            autores.append(act)
    
        cursor.close()
        conexao.close() 

        return autores

    def adicionar(self, autor: Autor) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
                        INSERT INTO autores  (nome, email, telefone, bio ) VALUES (%(nome)s, %(email)s, %(telefone)s, %(bio)s)
                        """,
                       ({'nome': autor.nome, 'email': autor.email, 'telefone' : autor.telefone, 'bio': autor.bio, }))
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, autor_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM autores WHERE id = %s", (autor_id,))

        autor_removidas = cursor.rowcount

        conexao.commit()
        cursor.close()
        conexao.close()

        if (autor_removidas == 0 ):
            return False
        return True

    def buscar_por_id(self, autor_id) -> Autor:
        act = None

        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, telefone, bio  FROM autores WHERE id = %s", (autor_id,))
        resultado = cursor.fetchone()

        if (resultado):
            act = Autor(resultado[1], resultado[2], resultado[3], resultado[4])
            act.id = resultado[0]
        
        cursor.close()
        conexao.close()

        return act 
    