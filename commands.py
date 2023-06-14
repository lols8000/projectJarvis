from voiceCapture import *
from comandShell import *
import datetime
import wikipedia
import pywhatkit
#teste
def comando_voz_usuario():
    # comando = executa_comando()
    comando = 'toque guns n roses, november rain'

    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()

    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        pywhatkit.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()

    elif 'execute o comando' in comando:
        descricao_comando = comando.replace('execute o comando', '')
        comando = gerar_comandoShell(descricao_comando)
        execute_powershell_command(comando)
        maquina.say('executando o comnando desejado')
        maquina.runAndWait()

    else:
        maquina.say('Não entendi!')
        maquina.runAndWait()
