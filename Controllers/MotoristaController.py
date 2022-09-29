import services.bd_contato as db;


def incluir(motorista):
    count = db.cursor.execute("""
    INSERT INTO contato_msg (nome_motorista, cpf_motorista, cel_motorista) 
    VALUES (?,?,?)""",
    motorista.nome_motorista, motorista.cpf_motorista, motorista.cel_motorista).rowcount
    db.conn.commit()

