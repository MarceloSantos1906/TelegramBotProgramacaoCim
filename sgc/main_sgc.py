import subprocess
import pyautogui
import keyboard
import pyperclip
import time
from sgc import (
    verificarTela,
    reconectar,
    utils_sgc,
    ativar_janela,
    verificar_janela_existe,
    tela21,
    estado_tecla,
)


def verificar_tela_21_emergencial():
    janela = "extra"
    loop = 0
    dados = []
    index = []
    ativar_janela.ativarJanela(titulo=janela)
    time.sleep(0.5)
    verificarTela.verificar_pos_invalida()
    verificarTela.verificar_Carregando()

    pyautogui.press("f3")
    while True:
        tela, clipboard = verificarTela.verificar_telas()
        if tela == "opcao":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            pyautogui.press("f3")
            utils_sgc.tela_opcao(opcao="21")
        elif tela == "data_programacao":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            utils_sgc.definir_data_tela_21(data="11112222", emergencial=True)
        elif tela == "tela_21":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            loop = 0
            while True:
                clipboard = verificarTela.copy_screen()
                dado, indexes = tela21.separar_dados_emergencial(clipboard)
                pyautogui.press("enter")
                verificarTela.verificar_pos_invalida()
                verificarTela.verificar_Carregando()
                for i in range(len(dado)):
                    dados.append(dado[i])
                for i in range(len(indexes)):
                    index.append(indexes[i])
                clipboard_anterior = clipboard
                tela, clipboard = verificarTela.verificar_telas()
                verificarTela.verificar_pos_invalida()
                verificarTela.verificar_Carregando()

                if tela == "data_programacao":
                    pyautogui.press("f3")
                    break
                elif clipboard_anterior == clipboard:
                    loop += 1
                elif loop == 4:
                    pyautogui.press("f3")
                    break
            return dados, index
        clipboard_anterior = clipboard


def verificar_tela_21_programado():
    janela = "extra"
    loop = 0
    dados = []
    index = []
    ativar_janela.ativarJanela(titulo=janela)
    time.sleep(0.5)
    verificarTela.verificar_pos_invalida()
    verificarTela.verificar_Carregando()

    pyautogui.press("f3")
    while True:
        tela, clipboard = verificarTela.verificar_telas()
        if tela == "opcao":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            pyautogui.press("f3")
            utils_sgc.tela_opcao(opcao="21")
        elif tela == "data_programacao":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            utils_sgc.definir_data_tela_21(data="11112222", emergencial=False)
        elif tela == "tela_21":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            loop = 0
            while True:
                clipboard = verificarTela.copy_screen()
                dado, indexes = tela21.separar_dados(clipboard)
                
                pyautogui.press("enter")
                verificarTela.verificar_pos_invalida()
                verificarTela.verificar_Carregando()
                for i in range(len(dado)):
                    dados.append(dado[i])
                for i in range(len(indexes)):
                    index.append(indexes[i])
                clipboard_anterior = clipboard
                tela, clipboard = verificarTela.verificar_telas()
                verificarTela.verificar_pos_invalida()
                verificarTela.verificar_Carregando()

                if tela == "data_programacao":
                    pyautogui.press("f3")
                    break
                elif clipboard_anterior == clipboard:
                    loop += 1
                elif loop == 4:
                    pyautogui.press("f3")
                    break
            return
        clipboard_anterior = clipboard


def programar_servico_emergencial(
    protocolo: str,
    equipe: str,
):
    ordem = 0
    janela = "extra"
    loop = 0
    protocolo = protocolo.strip()
    ativar_janela.ativarJanela(titulo=janela)
    pyautogui.press("f3")
    while True:
        verificarTela.verificar_pos_invalida()
        verificarTela.verificar_Carregando()

        tela, clipboard = verificarTela.verificar_telas()
        if tela == "opcao":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            utils_sgc.tela_opcao(opcao="21")
            loop = 0
        elif tela == "data_programacao":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            utils_sgc.definir_data_tela_21(data="11112222", emergencial=True)
            loop = 0
        elif tela == "tela_21":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            while True:
                for index in range(14):
                    for i in range(18):
                        keyboard.press("left")
                        time.sleep(0.00001)
                    pyperclip.copy("")
                    if estado_tecla.is_num_lock() == 1:
                        pyautogui.press("numlock")
                    keyboard.press("shift")
                    for i in range(16):
                        keyboard.press("right")
                        time.sleep(0.00001)
                    keyboard.release("shift")
                    keyboard.press("ctrl")
                    keyboard.press("c")
                    time.sleep(0.00001)
                    keyboard.release("ctrl")
                    keyboard.release("c")
                    pyautogui.press("tab")
                    if protocolo in pyperclip.paste().strip():
                        pyautogui.press("tab")
                        pyautogui.write(equipe)
                        pyautogui.press("enter")
                        pyautogui.press("f3")
                        while True:
                            verificarTela.verificar_pos_invalida()
                            verificarTela.verificar_Carregando()
                            tela, clipboard = verificarTela.verificar_telas()
                            if tela == "opcao":
                                utils_sgc.tela_opcao(opcao="32")
                                loop = 0
                            elif tela == "tela_32":
                                pyautogui.press("x")
                                pyautogui.press("enter")
                            elif tela == "tela_32_sel_eq":
                                pyautogui.write(equipe)
                                pyautogui.press("enter")
                            elif tela == "tela_32_lista":
                                for i in range(14):
                                    for i in range(8):
                                        keyboard.press_and_release("right")
                                        time.sleep(0.00001)
                                    keyboard.press("shift")
                                    for i in range(16):
                                        keyboard.press_and_release("right")
                                        time.sleep(0.00001)
                                    keyboard.release("shift")
                                    keyboard.press("ctrl")
                                    keyboard.press("c")
                                    time.sleep(0.00001)
                                    keyboard.release("ctrl")
                                    keyboard.release("c")
                                    pyautogui.press("tab")
                                    time.sleep(0.00001)
                                    if (
                                        protocolo in pyperclip.paste().strip()
                                        and i == 14
                                    ):
                                        ordem += 1
                                        pyautogui.press("down", presses=13)
                                        numero = str(ordem).zfill(2)
                                        pyautogui.write(numero)
                                        pyautogui.press("f7")
                                        if estado_tecla.is_num_lock() == 0:
                                            pyautogui.press("numlock")
                                        return
                                    elif protocolo in pyperclip.paste().strip():
                                        ordem += 1
                                        pyautogui.press("up")
                                        numero = str(ordem).zfill(2)
                                        pyautogui.write(numero)
                                        pyautogui.press("f7")
                                        pyautogui.press('s')
                                        pyautogui.press('enter')
                                        pyautogui.press('f3')
                                        pyautogui.press('f1')
                                        if estado_tecla.is_num_lock() == 0:
                                            pyautogui.press("numlock")
                                        return
                                pyautogui.press("enter")
                    elif pyperclip.paste().strip() == "":
                        pyautogui.press("f3")
                        if estado_tecla.is_num_lock() == 0:
                            pyautogui.press("numlock")
                        return
                    pyautogui.press("down")
                pyautogui.press("enter")
                verificarTela.verificar_pos_invalida()
                verificarTela.verificar_Carregando()
                tela, clipboard = verificarTela.verificar_telas()
                if tela == "data_programacao":
                    pyautogui.press("f3")
                    if estado_tecla.is_num_lock() == 0:
                        pyautogui.press("numlock")
                    return
        elif clipboard_anterior == clipboard:
            loop += 1
        elif loop == 3:
            pyautogui.press("f3")
        clipboard_anterior = clipboard


def programar_servicos(
    dados,
    index,
    equipes,
):
    base_uniao = ["104", "196", "211", "283", "400", "645", "668", "674", "682"]
    nao_precisa_autorizar_ligacao = ["104", "674"]
    base_bituruna = ["055", "413"]
    base_cruz_machado = ["088", "644"]

    for i in range(0, len(dados), 4):
        if dados[i + 3] in base_uniao:
            codigo_servico = dados[i]
            protocolo = dados[i + 1][:12]
            equipe = dados[i + 2]
            local = dados[i + 3]


def imprimir_servico(protocolo: str):
    ordem = 0
    janela = "extra"
    loop = 0
    protocolo = protocolo.strip()
    ativar_janela.ativarJanela(titulo=janela)
    pyautogui.press("f3")
    while True:
        verificarTela.verificar_pos_invalida()
        verificarTela.verificar_Carregando()

        tela, clipboard = verificarTela.verificar_telas()
        if tela == "opcao":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            utils_sgc.tela_opcao(opcao="58")
            loop = 0
        elif tela == "tela_58":
            pyautogui.press("down")
            pyautogui.write(protocolo)
            pyautogui.press("enter")
            pyautogui.press("f3")
            return
        else:
            pyautogui.press("f3")


def sgc(chave: str, senha: str, impressora: str):
    janela = "extra"
    caminho = "extra.edp"
    if not (verificar_janela_existe.main(classname="SDIMainFrame")):
        subprocess.Popen(
            caminho,
            shell=True,
        )
        while True:
            if not (verificar_janela_existe.main(classname="SDIMainFrame")):
                time.sleep(1)
            else:
                break
    ativar_janela.ativarJanela(titulo=janela)
    while True:
        verificarTela.verificar_pos_invalida()
        verificarTela.verificar_Carregando()

        tela, clipboard = verificarTela.verificar_telas()
        if tela == "disconected":
            reconectar.reconectar()
            loop = 0
        elif tela == "aplicacao":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            utils_sgc.definir_aplicacao(aplicacao="sgc")
            loop = 0
        elif tela == "login":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            utils_sgc.logar(chave=chave, senha=senha)
            loop = 0
        elif tela == "impressora":
            verificarTela.verificar_pos_invalida()
            verificarTela.verificar_Carregando()
            utils_sgc.definir_impressora(impressora=impressora)
            loop = 0
        elif tela == "opcao":
            return
        elif tela == "data_programacao":
            return
        elif tela == "tela_21":
            return


if __name__ == "__main__":
    sgc()
