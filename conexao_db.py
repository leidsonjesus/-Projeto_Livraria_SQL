import psycopg2

if __name__ == '__main__':
    conexao = psycopg2.connect(host='silly.db.elephantsql.com', database='htownnkj', user='htownnkj', password='iAM2Dq-jgf4NWB3uw5qhJQIZSsifi9N4')
    print('Connectado no banco de dados')
    conexao.close()

