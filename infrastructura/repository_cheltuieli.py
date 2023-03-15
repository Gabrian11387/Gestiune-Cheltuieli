from domain.cheltuiala import egal_cheltuieli, valideaza_cheltuiala


def adauga_cheltuiala_la_lista(cheltuieli, cheltuiala):
    """
    functia adauga la lista cheltuieli, cheltuiala de tip dictionar
    daca in lista nu mai exista o alta cheltuiala cu aceleasi date
    :param cheltuieli: lista de cheltuieli
    :param cheltuiala: dictionar
    :return: - (cheltuieli' = cheltuieli U {cheltuiala}, daca informatiile cheltuielii
                pe care dorim sa o adaugam nu se mai afla si in alta cheltuiala deja adaugata
    raises: ValueError cu mesajul string "cheltuiala deja existenta!\n" daca informatiile din cheltuiala
            se regasesc in alta cheltuiala deja existenta
    """
    for _cheltuiala in cheltuieli:
        if egal_cheltuieli(_cheltuiala, cheltuiala):
            raise ValueError("cheltuiala deja existenta!\n")
    valideaza_cheltuiala(cheltuiala)
    cheltuieli.append(cheltuiala)


def numar_cheltuieli_lista(cheltuieli):
    """
    functia returneaza numar de cheltuieli din lista cheltuieli care difera intre ele
    prin cel putin o informatie dintre: ziua, suma si tip
    :param cheltuieli: lista de cheltuieli
    :return: integer - numarul de cheltuieli din lista de cheltuieli
    """
    return len(cheltuieli)


def get_all_cheltuieli(cheltuieli):
    """
    functia returneaza toate cheltuielile salvate in lista cheltuieli
    :param cheltuieli: lista de dictionare unic identificabile prin combinatia de informatii pe care o retin
    :return: cheltuieli' = cheltuieli[:] (tip lista)
    """
    return cheltuieli[:]


def sterge_cheltuiala(cheltuieli, cheltuiala):
    """
    functia sterge cheltuiala chelatuiala din lista de cheltuieli
    :param cheltuieli: lista de dictionare/cheltuieli
    :param cheltuiala: dictionar
    :return: -
    """
    cheltuieli.remove(cheltuiala)


def elimina_cheltuiala(cheltuieli, cheltuiala):
    """
    functia elimina cheltuiala cheltuiala din lista de cheltuieli
    :param cheltuieli: lista de dictionare
    :param cheltuiala: dictionar
    :return: -
    """
    cheltuieli_ramase = []
    for el in cheltuieli:
        if not egal_cheltuieli(el, cheltuiala):
            cheltuieli_ramase.append(el)
    cheltuieli[:] = cheltuieli_ramase
