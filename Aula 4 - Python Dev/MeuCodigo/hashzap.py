# Sites / Sistemas / Aplicativos
# Flask
# Django
# FastAPI
# Flet -> Python -> visual (frontend) / logica (backend)
# Kivy

# Framework -> biblioteca com regras específicas

# criar o hashzap

# Titulo: Bem vindo ao HashZApp
# Botao: Iniciar chat
    # quando eu clicar no botao:
    # Janela / Dialog / Model / Popup
        # Titulo: Bem vindo ao HashZApp
        # Campo de texto: Escreve seu nome
        # Botao: Entrar no chat
            # clicou no botao:
            # Fechar o Dialog
                # criar o chat
                # criar o campo de mensagem: >>> Digite sua mensagem
                # botao: enviar
                    # quando clicar no botao:
                    # envie a mensagem para o chat 

#Importar o flet
import flet as ft

#Criar a funcao principal (main) do aplicativo
def main(pagina):
    # criar os elementos
    titulo = ft.Text('HashZApp')
    
    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    # WebSocket -> Tunel de comunicacao
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        mensagem = f'{campo_nome.value}: {campo_mensagem.value}'
        #enviar a mensagem no tunel
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()
    
    campo_mensagem = ft.TextField(label='Escreva sua mensagem', on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    chat = ft.Column()
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        pagina.pubsub.send_all(f'{campo_nome.value} entrou no chat')
        #Fechar o dialog
        janela.open = False
        # tirar o titulo
        pagina.remove(titulo)
        # tirar o botao iniciar
        pagina.remove(botao_iniciar)

        # criar o chat
        pagina.add(chat)
        # criar o campo digite sua mensagem
        # criar o botao enviar
        pagina.add(linha_mensagem)

        pagina.update()

    campo_nome = ft.TextField(label='Digite seu nome', on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    
    titulo_janela = ft.Text('Bem vindo ao HashZApp')
    janela = ft.AlertDialog(
        title = titulo_janela,
        content = campo_nome,
        actions = [botao_entrar]
    )


    def abrir_dialog(evento):
        print('clicou no botao')
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=abrir_dialog)

    # adicionar o dialog no overlay da página
    pagina.overlay.append(janela)

    #colocar os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
    
#Rodar o app
ft.app(main, view=ft.WEB_BROWSER)

#Ctrl + C no terminal para reabrir o site
