from tkinter import *
from tkinter import filedialog
from pytube import YouTube

# Diretório de saída
diretorioDeSaida = ""

# Configurações iniciais da janela
janelaPrincipal = Tk()
janelaPrincipal.title("Made by João Mateus")
janelaPrincipal.geometry("700x150")
janelaPrincipal.resizable(False, False)

# Funções
def escolherDiretorio():
    global diretorioDeSaida
    diretorioDeSaida = filedialog.askdirectory()
    textoMostrandoDiretorioEscolhido.config(text=diretorioDeSaida)

def baixarMusica():
    global diretorioDeSaida
    url = localParaColocarUrl.get()
    url = YouTube(url)
    musicaParaBaixar = url.streams.get_audio_only()
    musicaParaBaixar.download(output_path=diretorioDeSaida)

# Elementos
botaoEscolherDiretorio = Button(janelaPrincipal, text="Escolha o diretório", command=escolherDiretorio)
botaoEscolherDiretorio.grid(row=0, column=0, padx=10, pady=10)
textoMostrandoDiretorioEscolhido = Label(janelaPrincipal, text="Nenhum diretório selecionado", state="normal")
textoMostrandoDiretorioEscolhido.grid(row=0, column=1, padx=10, pady=10)

textoDoPrimeiroLabel = Label(janelaPrincipal, text="Coloque a url aqui: ")
textoDoPrimeiroLabel.grid(row=1, column=0, padx=10, pady=10)

botaoBaixarMusica = Button(janelaPrincipal, text="Baixar Música", command=baixarMusica)
botaoBaixarMusica.grid(row=2, column=0, padx=0, pady=15)

localParaColocarUrl = Entry(janelaPrincipal, width=90)
localParaColocarUrl.grid(row=1, column=1, padx=10, pady=10)

# Loop da janela principal
janelaPrincipal.mainloop()
