from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox

# Diretório de saída
diretorioDeSaida = ""
mensagemDeErro = '''
Algo de errado ocorreu...
Verifique se você está conectado a internet ou se você esqueceu de preencher a URL e escolher o diretório!
'''

# Configurações iniciais da janela
janelaPrincipal = Tk()
janelaPrincipal.title("Baixar Músicas")
janelaPrincipal.geometry("700x150")
janelaPrincipal.resizable(False, False)

# Funções
def escolherDiretorio():
    global diretorioDeSaida
    diretorioDeSaida = filedialog.askdirectory()
    textoMostrandoDiretorioEscolhido.config(text=diretorioDeSaida)

def baixarMusica():
    global diretorioDeSaida
    try:
            url = localParaColocarUrl.get()
            url = YouTube(url)
            musicaParaBaixar = url.streams.get_audio_only()
            musicaParaBaixar.download(output_path=diretorioDeSaida)
    except:
        messagebox.showerror(title="ERROR", message=mensagemDeErro)

# Elementos
botaoEscolherDiretorio = Button(janelaPrincipal, text="Escolha o diretório", command=escolherDiretorio)
botaoEscolherDiretorio.grid(row=0, column=0, padx=10, pady=10)
textoMostrandoDiretorioEscolhido = Label(janelaPrincipal, text="Nenhum diretório selecionado", state="normal")
textoMostrandoDiretorioEscolhido.grid(row=0, column=1, padx=10, pady=10)

textoDoPrimeiroLabel = Label(janelaPrincipal, text="Coloque a url aqui: ")
textoDoPrimeiroLabel.grid(row=1, column=0, padx=10, pady=10)

botaoBaixarMusica = Button(janelaPrincipal, text="Baixar Música", command=baixarMusica)
botaoBaixarMusica.grid(row=2, column=0, padx=0, pady=15)

textoComMeuNome = Label(janelaPrincipal, text="Made by João Mateus")
textoComMeuNome.place(relx=0.41,rely=0.3, relheight=1.2, relwidth=0.99)

localParaColocarUrl = Entry(janelaPrincipal, width=90)
localParaColocarUrl.grid(row=1, column=1, padx=10, pady=10)

# Loop da janela principal
janelaPrincipal.mainloop()
