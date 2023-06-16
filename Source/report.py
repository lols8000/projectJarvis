from win10toast import ToastNotifier


def exibir_notificacao(titulo, mensagem, time):
    toaster = ToastNotifier()
    toaster.show_toast(titulo, mensagem, duration=time)
