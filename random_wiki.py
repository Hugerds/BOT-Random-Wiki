import wikipedia
import tweepy
from time import sleep

chave_consumidor = ""
segredo_consumidor = ""
token_acesso = ""
token_acesso_secreto = ""

autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_secreto)

twitter = tweepy.API(autenticacao)

wikipedia.set_lang('pt')

def rodar():
    temPonto = 0
    paginaRandom = wikipedia.random(pages=1)
    texto = wikipedia.summary(title=paginaRandom)
    texto = [281]
    while(1):
        try:
            paginaRandom = wikipedia.random(pages=1)
            texto = wikipedia.summary(title=paginaRandom)
            tamTexto = len(texto)
            if tamTexto<=0:
                rodar()
            if (len(texto)<280):
                print("ESSE NÃO TEM MAIS DE 280 CARACTERES")
                if "== Referências ==" in texto:
                    for c in range(0,tamTexto-17):
                        try:
                            texto[c] = texto
                        except TypeError:
                            rodar()
                    print(texto)
                    publicaTuite(texto)
                else:
                    print(texto)
                    publicaTuite(texto)
            else:
                try:
                    for c in range(0, 280):
                        texto = texto[0:280]
                        if c > 200:
                            if "." in texto[c]:
                                temPonto = 1
                                posPonto = c
                                if temPonto == 0:
                                    for b in range(0,280):
                                        if b>100:
                                            if "." in texto[b]:
                                                posPonto = b
                                                temPonto = 1
                                                if temPonto == 0:
                                                    for d in range(0,280):
                                                        if d>50:
                                                            if "." in texto[d]:
                                                                posPonto=d
                                                                temPonto=1
                    for a in range(0, posPonto):
                        texto = texto[0:posPonto+1]
                    if "." not in texto[posPonto]:
                        rodar()
                    else:
                        print("ESSE TEM MAIS DE 280 CARACTERES")
                        print(texto)
                        publicaTuite(texto)
                except UnboundLocalError as error:
                    rodar()
        except wikipedia.exceptions.DisambiguationError:
            rodar()
        print(len(texto))

def publicaTuite(postTuite):
    try:
        twitter.update_status(postTuite)
        sleep(5)
        rodar()
    except:
        rodar()

rodar()