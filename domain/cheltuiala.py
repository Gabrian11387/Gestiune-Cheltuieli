def creeaza_cheltuiala(ziua, suma, tipul):
    """
    functia creeaza o cheltuiala pe baza informatiilor primte prin parametrii ziua, suma si tipul
    si o returneaza sub forma unui dictionar
    :param ziua: integer
    :param suma: float
    :param tipul: string
    :return: dictionar care contine informatiile unei cheltuieli
    """
    return {
        "ziua": ziua,
        "suma": suma,
        "tipul": tipul
    }


def get_ziua_cheltuiala(cheltuiala):
    """
    functia obtine ziua corespunzatoare cheltuielii transmise ca parametru
    :param cheltuiala: dictionar
    :return: ziua cheltuielii - integer
    """
    return int(cheltuiala["ziua"])


def get_suma_cheltuiala(cheltuiala):
    """
    functia obtine suma corespunzatoare cheltuielii transmise ca parametru
    :param cheltuiala: dictionar
    :return: suma cheltuielii - float
    """
    return float(cheltuiala["suma"])


def get_tipul_cheltuiala(cheltuiala):
    """
    functia obtine tipul corespunzatoare cheltuielii transmise ca parametru
    :param cheltuiala: dictionar
    :return: tipul cheltuielii - string
    """
    return str(cheltuiala["tipul"])


def actualizeaza_cheltuiala(cheltuiala, ziua, suma, tipul):
    """
    functia actualizeaza cheltuiala cu parametrii primiti,
    daca acestia pot constitui o cheltuiala valida
    :param cheltuiala: dictionar
    :param ziua: integer
    :param suma: float
    :param tipul: string
    :return: - daca actualizarea a avut loc cu succes
    """
    cheltuiala_pentru_validare = creeaza_cheltuiala(ziua, suma, tipul)
    valideaza_cheltuiala(cheltuiala_pentru_validare)
    cheltuiala["ziua"] = ziua
    cheltuiala["suma"] = suma
    cheltuiala["tipul"] = tipul

def valideaza_cheltuiala(cheltuiala):
    """
    verifica daca ziua cheltuielii este in intervalul [1,30], daca suma este pozitiva
    si daca tipul cheltuielii este dintre cele specificate: mancare, intretinere, imbracaminte, telefon, altele
    :param cheltuiala: un dictionar care contine informatiile despre cheltuiala: ziua, suma si tipul
    :return: - (daca cheltuiala resprecta toate conditiile impuse)
    raises:ValueError daca ziua nu este din intervalul [1,30] atunci concateneaza mesajul "zi invalida!\n"
                      daca suma este < 0 atunci concateneaza mesajul "suma invalida!\n"
                      daca tipul nu este dintre cele mentionate atunci concateneaza mesajul "tip invalid!\n"
    """
    tipuri_cheltuieli_valide = ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]
    erori = ""
    if get_ziua_cheltuiala(cheltuiala) < 1 or get_ziua_cheltuiala(cheltuiala) > 30:
        erori += "zi invalida!\n"
    if get_suma_cheltuiala(cheltuiala) < 0:
        erori += "suma invalida!\n"
    if get_tipul_cheltuiala(cheltuiala) not in tipuri_cheltuieli_valide:
        erori += "tip invalid!\n"
    if len(erori) > 0:
        raise ValueError(erori)


def egal_cheltuieli(cheltuiala_a, cheltuiala_b):
    """
    verifica daca cheltuiala_a contine aceleasi informatii ca si cheltuiala_b
    :param cheltuiala_a: dictionar
    :param cheltuiala_b: dictionar
    :return: True - daca cheltuielile contin exact aceleasi date
             False - daca altfel
    """
    presupunere_egalitate = True
    if cheltuiala_a["ziua"] != cheltuiala_a["ziua"]:
        presupunere_egalitate = False
    if abs(cheltuiala_a["suma"] - cheltuiala_b["suma"]) > 0.01:
        presupunere_egalitate = False
    if cheltuiala_a["tipul"] != cheltuiala_b["tipul"]:
        presupunere_egalitate = False
    return presupunere_egalitate








