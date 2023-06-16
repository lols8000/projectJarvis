from commands import *
import keyboard


def main():
    comando = comando_voz_usuario()
    executa_comando(comando)


def atalho_teclado(event):
    if keyboard.is_pressed('Ctrl+Q'):
        main()


keyboard.on_press(atalho_teclado)

# Mantém o programa em execução para continuar monitorando os eventos de teclado
keyboard.wait()
