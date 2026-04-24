from tkinterdnd2 import TkinterDnD
from GUI.app import App

def main():
    root = TkinterDnD.Tk()
    root.title("Processador TXT")
    root.geometry("500x400")
    
    app = App(root)
    app.mainloop()


if __name__ == "__main__":    
   main()