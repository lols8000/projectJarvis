from voiceCapture import *
from CommandsList.execute_o_comando import *
from CommandsList.me_diga_sobre import *
from CommandsList.horas import *
from CommandsList.procure_por import *
from CommandsList.toque import *


def executa_comando(comando):
    if 'horas' in comando:
        maquina.say('Agora são' + horas())
        maquina.runAndWait()

    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        maquina.say(procurar_wikipedia(procurar))
        maquina.runAndWait()

    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        procurar_musica(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()

    elif 'execute o comando' in comando:
        descricao_comando = comando.replace('execute o comando', '')
        comando = gerar_comandoShell(descricao_comando)
        execute_powershell_command(comando)
        maquina.say('executando o comnando desejado')
        maquina.runAndWait()

    elif 'me diga sobre' in comando:
        descricao_comando = comando.replace('me diga sobre', '')
        comando = informacao(descricao_comando)
        maquina.say(comando)
        maquina.runAndWait()

    else:
        maquina.say('Não entendi!')
        maquina.runAndWait()


executa_comando('que horas são')
