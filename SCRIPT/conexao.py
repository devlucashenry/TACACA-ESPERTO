import fdb

def conectar():
    return fdb.connect(
        dsn=r"C:\TACACA&ESPETO\BANCO\DADOS.FDB",
        user="SYSDBA",
        password="masterkey"
    )
