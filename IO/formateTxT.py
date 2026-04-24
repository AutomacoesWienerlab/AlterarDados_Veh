from tkinter import messagebox
from abrirArquivo import AbrirArquivos

class FormateTxt:
        def executar_processamento(self):
            abrirarquivos = AbrirArquivos
            if not self.caminho_arquivo:
                self.process_status.config(text="Nenhum arquivo carregado")
                return

            try:
                caminho_saida = abrirarquivos.processar_arquivos(
                    self.caminho_arquivo,
                    self.separador_var.get(),
                    int(self.campo_var.get()),
                    self.num_var.get(),
                    self.id_var.get()
                )

                self.process_status.config(text="Processado com sucesso")

                messagebox.showinfo(
                    "Concluído",
                    f"Arquivo gerado com sucesso.\n\nLocal:\n{caminho_saida}"
                )

            except Exception as e:
                self.process_status.config(text=f"Erro: {str(e)}")