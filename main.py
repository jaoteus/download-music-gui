from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox

# Diretório de saída
diretorioDeSaida = ""
mensagemDeErro = '''
Something went wrong...
Please check if you have internet access or if you forgot to fill in the URL and choose the directory!
'''

# Configurações iniciais da janela
janelaPrincipal = Tk()
janelaPrincipal.title("Music Downloader")
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
botaoEscolherDiretorio = Button(janelaPrincipal, text="Choose the directory", command=escolherDiretorio)
botaoEscolherDiretorio.grid(row=0, column=0, padx=10, pady=10)
textoMostrandoDiretorioEscolhido = Label(janelaPrincipal, text="No directory selected", state="normal")
textoMostrandoDiretorioEscolhido.grid(row=0, column=1, padx=10, pady=10)

textoDoPrimeiroLabel = Label(janelaPrincipal, text="Enter the URL: ")
textoDoPrimeiroLabel.grid(row=1, column=0, padx=10, pady=10)

botaoBaixarMusica = Button(janelaPrincipal, text="Download", command=baixarMusica)
botaoBaixarMusica.grid(row=2, column=0, padx=0, pady=15)

textoComMeuNome = Label(janelaPrincipal, text="Made by Mateus", font=("Arial", 7, "italic"))
textoComMeuNome.place(relx=0.41,rely=0.3, relheight=1.2, relwidth=1.05)

localParaColocarUrl = Entry(janelaPrincipal, width=90)
localParaColocarUrl.grid(row=1, column=1, padx=10, pady=10)

# Loop da janela principal
janelaPrincipal.mainloop()
