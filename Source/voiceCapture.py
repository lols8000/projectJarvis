import speech_recognition as sr
import pyttsx3
from Source.report import exibir_notificacao

audio = sr.Recognizer()
maquina = pyttsx3.init()


def comando_voz_usuario():
    while True:
        try:
            with sr.Microphone() as source:
                voz = audio.listen(source)
                comando_reconhecido = audio.recognize_google(voz, language='pt-BR').lower()

                if 'adeus' in comando_reconhecido:
                    maquina.say('Até mais!')
                    maquina.runAndWait()
                    source.stop()
                    break

                elif 'ok cortana' in comando_reconhecido:
                    exibir_notificacao("Cortana", "Estou ouvindo...", 1)
                    maquina.say('Estou ouvindo...')
                    maquina.say('Me diga o que você precisa?')
                    maquina.runAndWait()

                    voz_comando = audio.listen(source)
                    comando = audio.recognize_google(voz_comando, language='pt-BR').lower()

                    if 'cortana' in comando:
                        comando = comando.replace('cortana', '')
                        maquina.say('Executando' + comando)
                        maquina.runAndWait()
                        return comando

        except sr.RequestError:
            exibir_notificacao("Alerta!", "Erro na solicitação ao serviço de reconhecimento de fala.", 3)

        except sr.UnknownValueError:
            pass
