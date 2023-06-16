import wikipedia

def procurar_wikipedia(procurar):
    wikipedia.set_lang('pt')
    resultado = wikipedia.summary(procurar, 2)
    return resultado