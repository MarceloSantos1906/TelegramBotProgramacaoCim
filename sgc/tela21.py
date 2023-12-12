import pyautogui
from sgc import verificarTela


def separar_dados_emergencial(clipboard):
    linhas = clipboard.splitlines()
    for linha in range(len(linhas)):
        while True:
            if len(linhas[linha]) < 80:
                linhas[linha] += " "
            else:
                break
    informacoes = []
    indexes = []
    for linha in range(8, 22):
        if linhas[linha][2:6] != "    " and linhas[linha][2:6] not in codigos_sanepar:
            verificarTela.verificar_Carregando()
            indexes.append(linha - 8)
            codigo_servico = linhas[linha][2:6]
            protocolo = linhas[linha][12:29]
            equipe = linhas[linha][39:43]
            local = linhas[linha][49:52]
            informacoes.append(codigo_servico)
            informacoes.append(protocolo)
            informacoes.append(equipe)
            informacoes.append(local)
            pyautogui.press("left", presses=2)
            pyautogui.press("down", presses=linha - 8)
            pyautogui.press("f5")
            clipboard = verificarTela.copy_screen()
            pyautogui.press("enter")
            linhas_inf = clipboard.splitlines()
            endereco = linhas_inf[11][17:53]
            motivo = linhas_inf[18][17:53]
            informacoes.append(endereco)
            informacoes.append(motivo)
    return informacoes, indexes


def separar_dados(clipboard):
    linhas = clipboard.splitlines()
    for linha in range(len(linhas)):
        while True:
            if len(linhas[linha]) < 80:
                linhas[linha] += " "
            else:
                break
    informacoes = []
    indexes = []
    for linha in range(8, 22):
        if (
            linhas[linha][2:6] != "    "
            and linhas[linha][2:6] in codigos_para_programar
        ):
            indexes.append(linha - 8)
            codigo_servico = linhas[linha][2:6]
            protocolo = linhas[linha][12:29]
            equipe = linhas[linha][39:43]
            local = linhas[linha][49:52]
            informacoes.append(codigo_servico)
            informacoes.append(protocolo)
            informacoes.append(equipe)
            informacoes.append(local)
    return informacoes, indexes


codigos_emergenciais = [
    "2050",
    "2350",
    "3690",
    "3695",
    "0010",
    "0050",
    "0090",
    "0110",
    "0151",
    "0245",
    "0365",
    "0370",
    "1271",
    "1330",
    "1350",
    "1360",
    "1380",
    "1430",
    "1500",
    "1740",
    "1750",
    "1760",
    "1770",
    "1771",
    "1780",
    "1800",
    "1830",
    "1840",
    "1850",
    "1870",
    "1970",
    "2455",
    "2465",
    "3410",
    "3455",
    "3465",
    "3470",
    "3600",
    "3601",
]
codigos_para_programar = [
    "0040",
    "0042",
    "0047",
    "0115",
    "0130",
    "0131",
    "0132",
    "0350",
    "0541",
    "0551",
    "0552",
    "0705",
    "0710",
    "0715",
    "0720",
    "0730",
    "0745",
    "0750",
    "0751",
    "0930",
    "1050",
    "1060",
    "1065",
    "1100",
    "1110",
    "1390",
    "1400",
    "1410",
    "1480",
    "1490",
    "1510",
    "1520",
    "1540",
    "2000",
    "2010",
    "2051",
    "2060",
    "2090",
    "2160",
    "2170",
    "2180",
    "2445",
    "1555",
    "1556",
    "1557",
    "1560",
    "3020",
    "3080",
    "3090",
    "3245",
    "3280",
    "3290",
    "3310",
    "3390",
    "3400",
    "3415",
    "3420",
    "3440",
    "3450",
    "3460",
    "3560",
    "3585",
    "3830",
]



codigos_para_nao_programar = [
    '0746',
    '0755',
    '1670',
    '1920',
    '3500',
    '3520',
]

codigos_sanepar = [
    "0020",
    "0240",
    "0250",
    "1280",
    "1346",
    "1660",
    "2105",
    "2130",
    "2450",
    "2460",
    "2461",
    "2630",
    "3246",
    "3330",
    "3466",
    "3545",
    "3630",
    "3680",
    "3701",
]
