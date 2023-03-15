from domain.cheltuiala import actualizeaza_cheltuiala
from infrastructura.repository_cheltuieli import numar_cheltuieli_lista
from service.service_cheltuieli import adauga_cheltuiala_service, sterge_cheltuieli_interval_zile, \
    sterge_cheltuieli_ziua, sterge_cheltuieli_tipul, elimina_cheltuieli_tipul, elimina_cheltuieli_sub_suma, \
    sorteaza_cheltuieli_dupa_tip, refacere_lista, obtine_cheltuieli_inainte_de_ziua_sub_suma, \
    obtine_cheltuieli_de_tipul, obtine_cheltuieli_peste_suma, suma_totala_cheltuieli_de_tipul, ziua_suma_maxima, \
    cheltuieli_cu_suma


def afisare_cheltuieli(cheltuieli):
    i = 0
    for cheluiala in cheltuieli:
        i += 1
        print("Cheltuiala", i)
        for key, val in cheluiala.items():
            print("{}: {}".format(key, val))
        print()


def ui_adauga_cheltuiala(cheltuieli, stack, parametri):
    if len(parametri) != 3:
        raise ValueError("numar parametri invalid!\n")
    ziua = int(parametri[0])
    suma = float(parametri[1])
    tipul = str(parametri[2])
    adauga_cheltuiala_service(cheltuieli, stack, ziua, suma, tipul)


def ui_afiseaza_cheltuieli(cheltuieli, stack, parametri):
    if len(parametri) != 0:
        raise ValueError("numar parametri invalid!\n")
    i = 0
    afisare_cheltuieli(cheltuieli)
    if numar_cheltuieli_lista(cheltuieli) == 0:
        print("Lista de cheltuieli este vidă!")


def ui_actualizeaza_cheltuiala(cheltuieli, stack, parametri):
    if len(parametri) != 4:
        raise ValueError("numar parametri invalid!\n")
    numar_cheltuiala = int(parametri[0]) - 1
    if numar_cheltuiala < 0 or numar_cheltuiala > numar_cheltuieli_lista(cheltuieli) - 2:
        raise ValueError("numar cheltuiala invalid!")
    ziua = int(parametri[1])
    suma = float(parametri[2])
    tipul = parametri[3]
    actualizeaza_cheltuiala(cheltuieli[numar_cheltuiala], ziua, suma, tipul)


def ui_tipareste_cheltuieli_peste_suma(cheltuieli, stack, parametri):
    if len(parametri) != 1:
        raise ValueError("numar parametri invalid!\n")
    suma = float(parametri[0])
    cheltuieli_bune = obtine_cheltuieli_peste_suma(cheltuieli, suma)
    afisare_cheltuieli(cheltuieli_bune)


def ui_tipareste_cheltuieli_de_tipul(cheltuieli, stack, parametri):
    if len(parametri) != 1:
        raise ValueError("numar de parametri invalid!\n")
    tip = parametri[0]
    cheltuieli_bune = obtine_cheltuieli_de_tipul(cheltuieli, tip)
    afisare_cheltuieli(cheltuieli_bune)


def ui_tipareste_cheltuieli_inainte_de_ziua_sub_suma(cheltuieli, stack, parametri):
    if len(parametri) != 2:
        raise ValueError("numar parametri invalid!\n")
    ziua = parametri[0]
    suma = parametri[1]
    cheltuieli_bune = obtine_cheltuieli_inainte_de_ziua_sub_suma(cheltuieli, ziua, suma)
    afisare_cheltuieli(cheltuieli_bune)


def tipareste_suma_totala_cheltuieli_de_tipul(cheltuieli, stack, parametri):
    if len(parametri) != 1:
        raise ValueError("numar parametri invalid!")
    tipul = parametri[0]
    suma_totala = suma_totala_cheltuieli_de_tipul(cheltuieli, tipul)
    print("Suma totala pentru cheltuielile de tipul", tipul, "este", suma_totala)


def cauta_ziua_suma_maxima(cheltuieli, stack, parametri):
    if len(parametri) != 0:
        raise ValueError("numar parametri invalid!")
    ziua = ziua_suma_maxima(cheltuieli)
    print("Ziua in care a fost cheltuita suma maxima este", ziua)


def ui_tipareste_cheltuieli_sortate_dupa_tip(cheltuieli, stack, parametri):
    if len(parametri) != 0:
        raise ValueError("numar parametri invalid!")
    copie_cheltuieli = []
    copie_cheltuieli = cheltuieli
    sorteaza_cheltuieli_dupa_tip(copie_cheltuieli)
    afisare_cheltuieli(copie_cheltuieli)


def ui_sterge_cheltuieli_interval_zile(cheltuieli, stack, parametri):
    if len(parametri) != 2:
        raise ValueError("numar parametri invalid!")
    zi_inceput = int(parametri[0])
    zi_sfarsit = int(parametri[1])
    sterge_cheltuieli_interval_zile(cheltuieli, stack, zi_inceput, zi_sfarsit)


def ui_sterge_cheltuieli_ziua(cheltuieli, stack, parametri):
    if len(parametri) != 1:
        raise ValueError("numar parametri invalid!")
    ziua = int(parametri[0])
    sterge_cheltuieli_ziua(cheltuieli, stack, ziua)


def ui_sterge_cheltuieli_tipul(cheltuieli, stack, parametri):
    if len(parametri) != 1:
        raise ValueError("numar parametri invalid!")
    tipul = str(parametri[0])
    sterge_cheltuieli_tipul(cheltuieli, stack, tipul)

def ui_elimina_cheltuieli_tipul(cheltuieli, stack, parametri):
    if len(parametri) != 1:
        raise ValueError("numar parametri invalid!")
    tipul = str(parametri[0])
    elimina_cheltuieli_tipul(cheltuieli, stack, tipul)


def ui_elimina_cheltuieli_sub_suma(cheltuieli, stack, parametri):
    if len(parametri) != 1:
        raise ValueError("numar parametri invalid!")
    suma = int(parametri[0])
    elimina_cheltuieli_sub_suma(cheltuieli, stack, suma)


def ui_undo(cheltuieli, stack, parametri):
    if len(parametri) != 0:
        raise ValueError("numar parametri invalid!")
    refacere_lista(cheltuieli, stack)


def tipareste_cheltuieli_cu_suma(cheltuieli, stack, parametri):
    if len(parametri) != 1:
        raise ValueError("numar parametri invalid!")
    suma = parametri[0]
    cheltuieli_bune = cheltuieli_cu_suma(cheltuieli, suma)
    afisare_cheltuieli(cheltuieli_bune)

def run_ui():
    cheltuieli = []
    stack = []
    comenzi = {
        "adauga_cheltuiala": ui_adauga_cheltuiala,
        "afiseaza_cheltuieli": ui_afiseaza_cheltuieli,
        "actualizeaza_cheltuiala": ui_actualizeaza_cheltuiala,
        "tipareste_cheltuieli_peste_suma": ui_tipareste_cheltuieli_peste_suma,
        "tipareste_cheltuieli_de_tipul": ui_tipareste_cheltuieli_de_tipul,
        "tipareste_cheltuieli_inainte_de_ziua_sub_suma": ui_tipareste_cheltuieli_inainte_de_ziua_sub_suma,
        "sterge_cheltuieli_interval_zile": ui_sterge_cheltuieli_interval_zile,
        "sterge_cheltuieli_ziua": ui_sterge_cheltuieli_ziua,
        "sterge_cheltuieli_tipul": ui_sterge_cheltuieli_tipul,
        "elimina_cheltuieli_tipul": ui_elimina_cheltuieli_tipul,
        "elimina_cheltuieli_sub_suma": ui_elimina_cheltuieli_sub_suma,
        "tipareste_cheltuieli_sortate_dupa_tip": ui_tipareste_cheltuieli_sortate_dupa_tip,
        "undo": ui_undo,
        "tipareste_suma_totala_cheltuieli_de_tipul": tipareste_suma_totala_cheltuieli_de_tipul,
        "tipareste_cheltuieli_cu_suma": tipareste_cheltuieli_cu_suma,
        "cauta_ziua_suma_maxima": cauta_ziua_suma_maxima
    }
    while True:
        command = input(">>> ")
        command = command.strip()
        if command == "":
            continue
        if command == "exit":
            return
        parts = command.split()
        nume_command = parts[0]
        if nume_command in comenzi:
            try:
                comenzi[nume_command](cheltuieli, stack, parts[1:])
            except ValueError as ve:
                print(ve)
        else:
            print("comanda invalida!\n")