from tkinter import messagebox
from .abrirArquivo import processar_arquivos

class FormateTxt:
        def __init__(self, app):
             self.app = app
             
        def executar_processamento(self):
  
            if not self.app.caminho_arquivo:
                self.app.process_status.config(text="Nenhum arquivo carregado")
                return

            try:
                caminho_saida = processar_arquivos(
                    self.app.caminho_arquivo,
                    self.app.separador_var.get(),
                    int(self.app.campo_var.get()),
                    self.app.num_var.get(),
                    self.app.id_var.get()
                )

                self.app.process_status.config(text="Processado com sucesso")

                messagebox.showinfo(
                    "Concluído",
                    f"Arquivo gerado com sucesso.\n\nLocal:\n{caminho_saida}"
                )

            except Exception as e:
                self.app.process_status.config(text=f"Erro: Algum campo não foi preenchido corretamente! \n{str(e)}")