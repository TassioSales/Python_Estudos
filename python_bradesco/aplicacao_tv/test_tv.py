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
        if controle.sintoniza_canal(canal):
            print(f"✓ Canal {canal} sintonizado")
    
    # Mostra informações iniciais
    print("\n=== Informações da TV ===")
    print(minha_tv)
    
    # Testa troca de canais
    print("\n=== Testando troca de canais ===")
    for canal in ["SBT", "Globo", "Canal Inexistente"]:
        if controle.troca_canal(canal):
            print(f"✓ Mudou para o canal {canal}")
        else:
            print(f"✗ Não foi possível mudar para o canal {canal}")
    
    # Testa controle de volume
    print("\n=== Testando controle de volume ===")
    print(f"Volume atual: {minha_tv.volume}")
    
    print("Aumentando volume em 5...")
    novo_volume = controle.aumenta_volume(5)
    print(f"Novo volume: {novo_volume}")
    
    print("Diminuindo volume em 3...")
    novo_volume = controle.diminui_volume(3)
    print(f"Novo volume: {novo_volume}")
    
    print("\n=== Estado final da TV ===")
    print(minha_tv)

if __name__ == "__main__":
    testar_televisor()
