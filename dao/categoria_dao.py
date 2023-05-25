from model.categoria import Categoria
from database.conexao_factory import ConexaoFactory

class CategoriaDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()
        self.__categorias: list[Categoria] = list()

    def listar(self) -> list[Categoria]:
        return self.__categorias

    def adicionar(self, categoria: Categoria) -> None:
        conexao = self.__conexao_factory.get_conexao()
        """ self.__categorias.append(categoria)"""
        cursor = conexao.cursor()
        cursor.execute("""
                        INSERT INTO categorias (nome) VALUES (%(nome)s)
                        """,
                       ({'nome': categoria.nome, }))
        conexao.commit()
        cursor.close()
        conexao.close()

    

    def remover(self, categoria_id: int) -> bool:
        encontrado = False
        for c in self.__categorias:
            if (c.id == categoria_id):
                index = self.__categorias.index(c)
                self.__categorias.pop(index)
                encontrado = True
                break
        return encontrado

    def buscar_por_id(self, categoria_id) -> Categoria:
        cat = None
        for c in self.__categorias:
            if (c.id == categoria_id):
                cat = c
                break
        return cat
    