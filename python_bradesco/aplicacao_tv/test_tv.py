from tv import Televisor, ControleRemoto

def testar_televisor():
    # Cria uma nova TV e controle remoto
    print("=== Inicializando TV e Controle Remoto ===")
    minha_tv = Televisor("Samsung", "Smart TV 4K")
    controle = ControleRemoto(minha_tv)
    
    # Sintoniza alguns canais
    print("\n=== Sintonizando canais ===")
    canais = ["Globo", "SBT", "Record", "Band", "RedeTV"]
    for canal in canais:
        if controle.sintonizaCanal(canal):
            print(f"✓ Canal {canal} sintonizado")
    
    # Mostra informações iniciais
    print("\n=== Informações da TV ===")
    print(f"TV {minha_tv.fabricante} {minha_tv.modelo}")
    print(f"Canal atual: {controle.getCanalAtual() or 'Nenhum'}")
    print(f"Volume: {controle.getVolume()}")
    print(f"Canais disponíveis: {', '.join(controle.getListaCanais()) or 'Nenhum'}")
    
    # Testa troca de canais
    print("\n=== Testando troca de canais ===")
    for canal in ["SBT", "Globo", "Canal Inexistente"]:
        controle.trocaCanal(canal)
        canal_atual = controle.getCanalAtual()
        if canal_atual == canal:
            print(f"✓ Mudou para o canal {canal}")
        else:
            print(f"✗ Não foi possível mudar para o canal {canal}")
    
    # Testa controle de volume
    print("\n=== Testando controle de volume ===")
    print(f"Volume atual: {controle.getVolume()}")
    
    print("Aumentando volume...")
    controle.aumentaVolume()
    print(f"Novo volume: {controle.getVolume()}")
    
    print("Diminuindo volume...")
    controle.diminuiVolume()
    print(f"Novo volume: {controle.getVolume()}")
    
    print("\n=== Estado final da TV ===")
    print(f"TV {minha_tv.fabricante} {minha_tv.modelo}")
    print(f"Canal atual: {controle.getCanalAtual() or 'Nenhum'}")
    print(f"Volume: {controle.getVolume()}")
    print(f"Canais disponíveis: {', '.join(controle.getListaCanais()) or 'Nenhum'}")

if __name__ == "__main__":
    testar_televisor()
