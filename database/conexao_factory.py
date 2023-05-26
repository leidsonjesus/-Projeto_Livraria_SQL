import psycopg2


class ConexaoFactory:

    def get_conexao(self):
        return psycopg2.connect(host='silly.db.elephantsql.com', database='htownnkj', user='htownnkj', password='iAM2Dq-jgf4NWB3uw5qhJQIZSsifi9N4')
    

