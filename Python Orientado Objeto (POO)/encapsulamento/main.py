from basededados import BaseDeDados

bd = BaseDeDados()

bd.inserir_cliente(1, "Tassio")
bd.inserir_cliente(2, "Lucian")
bd.inserir_cliente(3, "Jesus")
bd.apaga_cliente(3)
bd.lista_clientes()

