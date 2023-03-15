from domain.cheltuiala import creeaza_cheltuiala
from infrastructura.repository_cheltuieli import adauga_cheltuiala_la_lista, sterge_cheltuiala, elimina_cheltuiala, \
    numar_cheltuieli_lista


def adauga_cheltuiala_service(cheltuieli, stack, ziua, suma, tipul):
    """
    adauga cheltuiala data de ziua, suma si tipul in lista de cheltuieli
    :param cheltuieli: lista de dicitonare
    :param stack: lista de dicitonare
    :param ziua: integer
    :param suma: float
    :param tipul: string
    :return:
    """
    cheltuiala = creeaza_cheltuiala(ziua, suma, tipul)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)
    operatie = "adaugare"
    adauga_operatie_stiva(stack, operatie, cheltuiala, 1)


def sterge_cheltuieli_ziua(cheltuieli, stack, ziua):
    """
    functia sterge cheltuiala cu ziua specificata din lista de cheltuieli
    :param cheltuieli: lista de dictionare
    :param stack: lista de dictionare
    :param ziua: interger
    :return: -
    """
    nr_modif = 0
    for i in range(0, 2):
        for cheltuiala in cheltuieli:
            if cheltuiala["ziua"] == ziua:
                nr_modif += 1
                adauga_operatie_stiva(stack, "stergere", cheltuiala, nr_modif)
                sterge_cheltuiala(cheltuieli, cheltuiala)


def sterge_cheltuieli_tipul(cheltuieli, stack, tipul):
    """
    functia sterge cheltuielile de tipul tipul din lista de cheltuieli
    :param cheltuieli: lista de dictionare
    :param stack: lista de dictionare
    :param tipul: string
    :return: -
    """
    nr_modif = 0
    for i in range(0, 2):
        for cheltuiala in cheltuieli:
            if cheltuiala["tipul"] == tipul:
                nr_modif += 1
                adauga_operatie_stiva(stack, "stergere", cheltuiala, nr_modif)
                sterge_cheltuiala(cheltuieli, cheltuiala)


def sterge_cheltuieli_interval_zile(cheltuieli, stack, zi_inceput, zi_sfarsit):
    """
    functia sterge din lista de cheltuilei cheltuielile a caror zi se afla intre zi inceput si zi sfarsit
    :param cheltuieli: lista de dictionare
    :param stack: lista de dictionare
    :param zi_inceput: integer
    :param zi_sfarsit: interger
    :return:
    """
    nr_modif = 0
    for i in range(0, 2):
        for cheltuiala in cheltuieli:
            if zi_inceput <= cheltuiala["ziua"] <= zi_sfarsit:
                nr_modif += 1
                adauga_operatie_stiva(stack, "stergere", cheltuiala, nr_modif)
                sterge_cheltuiala(cheltuieli, cheltuiala)


def elimina_cheltuieli_tipul(cheltuieli, stack, tipul):
    """
    fucntia elimina din lista de cheltuilei, cheltuielile de tipul tipul
    :param cheltuieli: lista de dictionare
    :param stack: lista de dictionare
    :param tipul: string
    :return: -
    """
    nr_modif = 0
    for i in range(0, 2):
        for cheltuiala in cheltuieli:
            if cheltuiala["tipul"] == tipul:
                nr_modif += 1
                adauga_operatie_stiva(stack, "eliminare", cheltuiala, nr_modif)
                elimina_cheltuiala(cheltuieli, cheltuiala)


def elimina_cheltuieli_sub_suma(cheltuieli, stack, suma):
    """
    functia elimina din lista de cheltuieli, cheltuielile a caror suma este mai mica(aproximativ) decat suma
    :param cheltuieli: lista de dictionare
    :param stack: lista de dictionare
    :param suma: float
    :return: -
    """
    nr_modif = 0
    for i in range(0, 2):
        for cheltuiala in cheltuieli:
            if cheltuiala["suma"] < suma:
                nr_modif += 1
                adauga_operatie_stiva(stack, "eliminare", cheltuiala, nr_modif)
                elimina_cheltuiala(cheltuieli, cheltuiala)


def suma_totala_cheltuieli_de_tipul(cheltuieli, tipul):
    """
    functia calculeaza suma tuturor cheltuielilor de tipul tipul, pe care o returneaza
    :param cheltuieli: lista de dictionare
    :param tipul: lista de dictionare
    :return: suma tuturor cheltuielilor de tipul tipul
    """
    s = 0
    for cheltuiala in cheltuieli:
        if cheltuiala["tipul"] == tipul:
            s += cheltuiala["suma"]
    return s


def ziua_suma_maxima(cheltuieli):
    """
    functia cauta cheltuiala cu suma maxima si returneaza ziua acesteia
    :param cheltuieli: lista de dictionare
    :return: ziua cheltuielii cu suma maxima
    """
    smax, ziua = 0, 0
    for cheltuiala in cheltuieli:
        if cheltuiala["suma"] > smax:
            smax = cheltuiala["suma"]
            ziua = cheltuiala["ziua"]
    return ziua


def cheltuieli_cu_suma(cheltuieli, suma):
    """
    fucntia returneaza o lista de cheltuieli care au suma aproximativ egala cu suma transmisa ca parametru
    :param cheltuieli: lista de dictionare
    :param suma: float
    :return: lista de cheltuieli care are suma apropiata de suma
    """
    cheltuieli_bune = []
    for cheltuiala in cheltuieli:
        if abs(cheltuiala["suma"] - suma) < 0.01:
            cheltuieli_bune.append(cheltuiala)
    return cheltuieli_bune


def sorteaza_cheltuieli_dupa_tip(cheltuieli):
    """
    functia sorteaza lista de cheltuieli dupa tipul acestora
    :param cheltuieli: lista de dictionare
    :return: -
    """
    n = numar_cheltuieli_lista(cheltuieli)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if cheltuieli[i]["tipul"] > cheltuieli[j]["tipul"]:
                cheltuieli[i], cheltuieli[j] = cheltuieli[j], cheltuieli[i]


def obtine_cheltuieli_inainte_de_ziua_sub_suma(cheltuieli, ziua, suma):
    """
    functia returneaza o lista de cheltuieli care au fost efectuazate inainte de ziua transmisa ca parametru,
    si au o suma mai mica decat suma transmisa ca parametru
    :param cheltuieli: lista de dictionare
    :param ziua: integer
    :param suma: float
    :return: lista de cheltuieli care respecta conditia
    """
    cheltuieli_bune = []
    for cheltuiala in cheltuieli:
        if cheltuiala["ziua"] < ziua and cheltuiala["suma"] < suma:
            cheltuieli_bune.append(cheltuiala)
    return cheltuieli_bune


def obtine_cheltuieli_de_tipul(cheltuieli, tip):
    """
    functia returneaza toate cheltuielile de tipul tip
    :param cheltuieli: lista de dictionare
    :param tipul: string
    :return: lista de cheltuieli care respecta conditia
    """
    cheltuieli_bune = []
    for cheltuiala in cheltuieli:
        if cheltuiala["tipul"] == tip:
            cheltuieli_bune.append(cheltuiala)
    return cheltuieli_bune


def obtine_cheltuieli_peste_suma(cheltuieli, suma):
    """
    functia returneaza cheltuielile care au suma mai mare decat suma data ca parametru
    :param cheltuieli: lista de dictionare
    :param suma: float
    :return: lista de cheltuieli care respecta conditia
    """
    cheltuieli_bune = []
    for cheltuiala in cheltuieli:
        if cheltuiala["suma"] - suma > 0:
            cheltuieli_bune.append(cheltuiala)
    return cheltuieli_bune


def adauga_operatie_stiva(stack, operatie, cheltuiala, nr_modif):
    """
    functia adauga pe stiva un dicitonar dat de inforamtiile operatie, cheltuiala si nr_modif
    :param stack: lista de dictionare
    :param operatie: string
    :param cheltuiala: dictionar
    :param nr_modif: integer
    :return: -
    """
    ultima_operatie = {
        "nume_operatie": operatie,
        "element": cheltuiala,
        "nr_modif": nr_modif
    }
    stack.append(ultima_operatie)


def refacere_lista(cheltuieli, stack):
    """
    functia reface lista la starea ei initiala ultimei operatii care a modificat-o
    :param cheltuieli: lista de dictionare
    :param stack: lista de dictionare
    :return: -
    """
    if len(stack) == 0:
        raise ValueError("Ati ajuns la inceputul executiei aplicatiei!")
    ultima_operatie = stack.pop()
    operatie = ultima_operatie["nume_operatie"]
    element = ultima_operatie["element"]
    nr_modif = ultima_operatie["nr_modif"]
    if operatie == "adaugare":
        sterge_cheltuiala(cheltuieli, element)

    elif operatie == "stergere" or operatie == "eliminare":
        adauga_cheltuiala_la_lista(cheltuieli, element)
        while nr_modif != 1:
            ultima_operatie = stack.pop()
            operatie = ultima_operatie["nume_operatie"]
            element = ultima_operatie["element"]
            nr_modif = ultima_operatie["nr_modif"]
            adauga_cheltuiala_la_lista(cheltuieli, element)
