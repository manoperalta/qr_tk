import qrcode

def converter(nome, link):
    nome_qr = nome
    link_qr = link
    imagem_qrcoded = qrcode.make(link_qr)
    path = f"qrcode_{nome_qr}.png"  # Corrigindo esta linha para obter o caminho do arquivo
    imagem_qrcoded.save(path)
    print(path)
    return path
