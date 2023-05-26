from model.editora import Editora
from database.conexao_factory import ConexaoFactory

class EditoraDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()

    def listar(self) -> list[Editora]:
        editoras = list ()

        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM editoras")
        resultados = cursor.fetchall()

        for result in resultados: 
            edi = Editora(result[1], result[2], result[3])
            edi.id = result[0]
            editoras.append(edi)
    
        cursor.close()
        conexao.close() 

        return editoras
    
    def adicionar(self, editora: Editora) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("""
                        INSERT INTO editoras  (nome, endereco, telefone ) VALUES (%(nome)s, %(endereco)s, %(telefone)s)
                        """,
                       ({'nome': editora.nome, 'endereco': editora.endereco, 'telefone' : editora.telefone, }))
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, editora_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM editoras WHERE id = %s", (editora_id,))

        editora_removidas = cursor.rowcount

        conexao.commit()
        cursor.close()
        conexao.close()

        if (editora_removidas == 0 ):
            return False
        return True

        
    def buscar_por_id(self, editora_id) -> Editora:
        edi = None

        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, endereco, telefone FROM editoras WHERE id = %s", (editora_id,))
        resultado = cursor.fetchone()

        if (resultado):
            edi = Editora(resultado[1], resultado[2], resultado[3])
            edi.id = resultado[0]
        
        cursor.close()
        conexao.close()

        return edi 
