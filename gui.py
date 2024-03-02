import tkinter as tk
import qrcode
import webbrowser

def gerar_qrcode():
    nome = campo_nome.get()
    url = campo_url.get()
    imagem_qrcoded = qrcode.make(url)
    path = f"qrcode_{nome}.png"
    imagem_qrcoded.save(path)
    webbrowser.open(path)
    label_resultado.config(text=f"{path}")


janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.geometry("250x250")


label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
campo_nome = tk.Entry(janela)
campo_nome.pack(pady=5)


label_url = tk.Label(janela, text="URL:")
label_url.pack()
campo_url = tk.Entry(janela)
campo_url.pack(pady=5)


botao_gerar = tk.Button(janela, text="Gerar QR Code", command=gerar_qrcode)
botao_gerar.pack(pady=10)


label_resultado = tk.Label(janela, text="By Jônathas M. Peralta")
label_resultado.pack()


janela.mainloop()
