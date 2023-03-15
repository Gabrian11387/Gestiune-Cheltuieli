from domain.cheltuiala import creeaza_cheltuiala, get_ziua_cheltuiala, get_suma_cheltuiala, get_tipul_cheltuiala, \
    valideaza_cheltuiala, actualizeaza_cheltuiala, egal_cheltuieli
from infrastructura.repository_cheltuieli import numar_cheltuieli_lista, adauga_cheltuiala_la_lista, get_all_cheltuieli, \
    sterge_cheltuiala, elimina_cheltuiala
from service.service_cheltuieli import sterge_cheltuieli_ziua, sterge_cheltuieli_tipul, sterge_cheltuieli_interval_zile, \
    elimina_cheltuieli_tipul, elimina_cheltuieli_sub_suma, obtine_cheltuieli_inainte_de_ziua_sub_suma, \
    obtine_cheltuieli_de_tipul, obtine_cheltuieli_peste_suma, adauga_cheltuiala_service, \
    suma_totala_cheltuieli_de_tipul, ziua_suma_maxima, cheltuieli_cu_suma, sorteaza_cheltuieli_dupa_tip, \
    adauga_operatie_stiva, refacere_lista


def ruleaza_teste_creare_cheltuiala():
    ziua = 17
    suma = 45.07
    tipul = "mancare"
    cheltuiala = creeaza_cheltuiala(ziua, suma, tipul)
    assert (ziua == get_ziua_cheltuiala(cheltuiala))
    assert (suma == get_suma_cheltuiala(cheltuiala))
    assert (tipul == get_tipul_cheltuiala(cheltuiala))


def ruleaza_teste_actualizare_cheltuiala():
    ziua = 10
    suma = 90.80
    tipul = "altele"
    cheltuiala = creeaza_cheltuiala(ziua, suma, tipul)
    ziua_noua = 17
    suma_noua = 70.67
    tipul_nou = "telefon"
    actualizeaza_cheltuiala(cheltuiala, ziua_noua, suma_noua, tipul_nou)
    assert (ziua_noua == get_ziua_cheltuiala(cheltuiala))
    assert (suma_noua == get_suma_cheltuiala(cheltuiala))
    assert (tipul_nou == get_tipul_cheltuiala(cheltuiala))


def ruleaza_teste_validare_cheltuiala():
    ziua = 5
    suma = 65.07
    tip = "altele"
    cheltuiala = creeaza_cheltuiala(ziua, suma, tip)
    valideaza_cheltuiala(cheltuiala)

    ziua_gresita = 40
    suma_gresita = -342.90
    tip_gresit = "electrocasnice"
    cheltuiala_gresita = creeaza_cheltuiala(ziua_gresita, suma_gresita, tip_gresit)
    try:
        valideaza_cheltuiala(cheltuiala_gresita)
        assert False
    except ValueError as ve:
        assert(str(ve) == "zi invalida!\nsuma invalida!\ntip invalid!\n")


def ruleaza_teste_egal_cheltuieli():
    ziua1 = 10
    suma1 = 50.50
    tipul1 = "telefon"
    cheltuiala1 = creeaza_cheltuiala(ziua1, suma1, tipul1)
    cheltuiala2 = creeaza_cheltuiala(ziua1, suma1, tipul1)
    assert (egal_cheltuieli(cheltuiala1, cheltuiala2) == True)
    ziua_alta = 15
    suma_alta = 50.30
    tipul_altul = "mancare"
    cheltuiala_alta = creeaza_cheltuiala(ziua_alta, suma_alta, tipul_altul)
    assert (egal_cheltuieli(cheltuiala1, cheltuiala_alta) == False)


def ruleaza_teste_repository_cheltuieli():
    # assert-uri care verifica daca adaugarea unei cheltuieli
    # la lista de cheltuieli se face corespunzator
    cheltuieli = []
    ziua = 10
    suma = 140.17
    tipul = "telefon"
    cheltuiala = creeaza_cheltuiala(ziua, suma, tipul)
    assert(numar_cheltuieli_lista(cheltuieli) == 0)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)
    assert(numar_cheltuieli_lista(cheltuieli) == 1)

    # assert-uri care verifica daca functia de adaugare cheltuiala la lista
    # verifica corect ca cheltuiala adaugata sa nu mai existe deja in lista
    ziua_aceeasi = 10
    suma_aceeasi = 140.17
    tipul_acelasi = "telefon"
    aceeasi_cheltuiala = creeaza_cheltuiala(ziua_aceeasi, suma_aceeasi, tipul_acelasi)
    try:
        adauga_cheltuiala_la_lista(cheltuieli, aceeasi_cheltuiala)
        assert False
    except ValueError as ve:
        assert (str(ve) == "cheltuiala deja existenta!\n")
    assert (numar_cheltuieli_lista(cheltuieli) == 1)

    # verificarea corectitudinii functiilor:
    # - de obtinere a tuturor cheltuielilor
    # - de obtinere a informatiilor despre o anumita cheltuiala
    lista_cheltuieli = get_all_cheltuieli(cheltuieli)
    assert (len(lista_cheltuieli) == 1)
    assert (get_ziua_cheltuiala(lista_cheltuieli[0]) == get_ziua_cheltuiala(cheltuiala))
    assert (abs(get_suma_cheltuiala(lista_cheltuieli[0]) - get_suma_cheltuiala(cheltuiala)) < 0.01)
    assert (get_tipul_cheltuiala(lista_cheltuieli[0]) == get_tipul_cheltuiala(cheltuiala))

    sterge_cheltuiala(cheltuieli, cheltuiala)
    assert (numar_cheltuieli_lista(cheltuieli) == 0)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala)
    assert (numar_cheltuieli_lista(cheltuieli) == 1)
    elimina_cheltuiala(cheltuieli, cheltuiala)
    assert (numar_cheltuieli_lista(cheltuieli) == 0)


def ruleaza_teste_adauga_cheltuiala_service():
    cheltuieli = []
    stack = []
    ziua = 1
    suma = 20.50
    tipul = "mancare"
    cheltuiala = creeaza_cheltuiala(ziua, suma, tipul)
    assert (numar_cheltuieli_lista(cheltuieli) == 0)
    adauga_cheltuiala_service(cheltuieli, stack, ziua, suma, tipul)
    assert (numar_cheltuieli_lista(cheltuieli) == 1)
    assert (stack[0]["nume_operatie"] == "adaugare")
    assert (stack[0]["element"] == cheltuiala)
    assert (stack[0]["nr_modif"] == 1)


def ruleaza_teste_sterge_cheltuieli_ziua():
    cheltuieli = []
    stack = []
    ziua = 3
    cheltuiala1 = creeaza_cheltuiala(3, 50.20, "telefon")
    cheltuiala2 = creeaza_cheltuiala(5, 60.30, "mancare")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    sterge_cheltuieli_ziua(cheltuieli, stack, ziua)
    assert (cheltuieli == [{"ziua": 5,
                            "suma": 60.30,
                            "tipul": "mancare"}])
    assert (stack[0]["nume_operatie"] == "stergere")
    assert (stack[0]["element"] == cheltuiala1)
    assert (stack[0]["nr_modif"] == 1)


def ruleaza_teste_sterge_cheltuieli_tipul():
    stack = []
    cheltuieli = []
    cheltuiala1 = creeaza_cheltuiala(5, 60.90, "telefon")
    cheltuiala2 = creeaza_cheltuiala(10, 80.65, "mancare")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    tipul = "telefon"
    sterge_cheltuieli_tipul(cheltuieli, stack, tipul)
    assert (cheltuieli == [{
            "ziua": 10,
            "suma": 80.65,
            "tipul": "mancare"
        }])
    assert (stack[0]["nume_operatie"] == "stergere")
    assert (stack[0]["element"] == cheltuiala1)
    assert (stack[0]["nr_modif"] == 1)


def ruleaza_teste_sterge_cheltuieli_interval_zile():
    cheltuieli = []
    stack = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.90, "telefon")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "altele")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    zi_inceput = 1
    zi_sfarsit = 8
    sterge_cheltuieli_interval_zile(cheltuieli, stack, zi_inceput, zi_sfarsit)
    assert (cheltuieli == [{
            "ziua": 10,
            "suma": 70.65,
            "tipul": "altele"
        }])
    assert (stack[0]["nume_operatie"] == "stergere")
    assert (stack[0]["element"] == cheltuiala1)
    assert (stack[0]["nr_modif"] == 1)


def ruleaza_teste_elimina_cheltuieli_tipul():
    cheltuieli = []
    stack = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.90, "telefon")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "altele")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    tipul = "altele"
    elimina_cheltuieli_tipul(cheltuieli, stack, tipul)
    assert (cheltuieli == [
        {"ziua": 7,
         "suma": 20.90,
         "tipul": "telefon"}])
    assert (stack[0]["nume_operatie"] == "eliminare")
    assert (stack[0]["element"] == cheltuiala2)
    assert (stack[0]["nr_modif"] == 1)


def ruleaza_teste_elimina_cheltuieli_sub_suma():
    cheltuieli = []
    stack = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.90, "telefon")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "altele")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    suma = 50
    elimina_cheltuieli_sub_suma(cheltuieli, stack, suma)
    assert (cheltuieli == [{
        "ziua": 10,
        "suma": 70.65,
        "tipul": "altele"
    }])
    assert (stack[0]["nume_operatie"] == "eliminare")
    assert (stack[0]["element"] == cheltuiala1)
    assert (stack[0]["nr_modif"] == 1)


def ruleaza_teste_suma_totala_cheltuieli_de_tipul():
    cheltuieli = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.30, "altele")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "altele")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    tipul = "altele"
    s = suma_totala_cheltuieli_de_tipul(cheltuieli, tipul)
    assert (abs(s - 90.95) < 0.01)


def ruleaza_teste_ziua_suma_maxima():
    cheltuieli = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.30, "altele")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "altele")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    ziua = ziua_suma_maxima(cheltuieli)
    assert (ziua == 10)


def ruleaza_teste_cheltuieli_cu_suma():
    cheltuieli = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.30, "altele")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "altele")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    suma = 70.65
    cheltuieli_bune = cheltuieli_cu_suma(cheltuieli, suma)
    assert (cheltuieli_bune == [{
        "ziua": 10,
        "suma": 70.65,
        "tipul": "altele"
    }])


def ruleaza_teste_sorteaza_cheltuieli_dupa_tip():
    cheltuieli = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.30, "altele")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "telefon")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    sorteaza_cheltuieli_dupa_tip(cheltuieli)
    assert (cheltuieli == [
        {"ziua": 7,
        "suma": 20.30,
        "tipul": "altele"},

        {"ziua": 10,
        "suma": 70.65,
        "tipul": "telefon"}
    ])


def ruleaza_teste_tiparire_peste_suma():
    cheltuieli = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.30, "altele")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "telefon")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    suma = 70.0
    cheltuieli_peste_suma = obtine_cheltuieli_peste_suma(cheltuieli, suma)
    assert (cheltuieli_peste_suma == [
            {"ziua": 10,
            "suma": 70.65,
            "tipul": "telefon"}
    ])


def ruleaza_teste_tiparire_de_tipul():
    cheltuieli = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.30, "altele")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "telefon")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    tip = "telefon"
    cheltuieli_de_tipul = obtine_cheltuieli_de_tipul(cheltuieli, tip)
    assert (cheltuieli_de_tipul == [
       {"ziua": 10,
        "suma": 70.65,
        "tipul": "telefon"}
    ])


def ruleaza_teste_tiparire_cheltuieli_inainte_de_ziua_sub_suma():
    cheltuieli = []
    cheltuiala1 = creeaza_cheltuiala(7, 20.30, "altele")
    cheltuiala2 = creeaza_cheltuiala(10, 70.65, "telefon")
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala1)
    adauga_cheltuiala_la_lista(cheltuieli, cheltuiala2)
    ziua = 8
    suma = 70.0
    cheltuieli_inainte_de_ziua_sub_suma = obtine_cheltuieli_inainte_de_ziua_sub_suma(cheltuieli, ziua, suma)
    assert (cheltuieli_inainte_de_ziua_sub_suma == [
        {"ziua": 7,
        "suma": 20.30,
        "tipul": "altele"}
    ])


def ruleaza_teste_adauga_operatie_stiva():
    stack = []
    operatie = "adaugare"
    cheltuiala = creeaza_cheltuiala(7, 60.30, "telefon")
    nr_modif = 1
    adauga_operatie_stiva(stack, operatie, cheltuiala, nr_modif)
    assert (stack == [{
        "nume_operatie": operatie,
        "element": cheltuiala,
        "nr_modif": nr_modif
    }])


def ruleaza_teste_refacere_lista():
    cheltuieli = []
    stack = []
    adauga_cheltuiala_service(cheltuieli, stack, 5, 60.50, "mancare")
    adauga_cheltuiala_service(cheltuieli, stack, 8, 20.40, "telefon")
    refacere_lista(cheltuieli, stack)
    assert (cheltuieli == [{
        "ziua": 5,
        "suma": 60.50,
        "tipul": "mancare"
    }])
    adauga_cheltuiala_service(cheltuieli, stack, 8, 20.40, "telefon")
    sterge_cheltuieli_tipul(cheltuieli, stack, "telefon")
    refacere_lista(cheltuieli, stack)
    assert (cheltuieli == [
        {"ziua": 5,
        "suma": 60.50,
        "tipul": "mancare"},

        {"ziua": 8,
        "suma": 20.40,
        "tipul": "telefon"}
    ])


def ruleaza_toate_testele():
    ruleaza_teste_creare_cheltuiala()
    print("testele creare cheltuiala rulate cu succes!")
    ruleaza_teste_actualizare_cheltuiala()
    print("testele actualizare cheltuiala rulate cu succes!")
    ruleaza_teste_validare_cheltuiala()
    print("testele validare cheltuiala rulate cu succes!")
    ruleaza_teste_egal_cheltuieli()
    print("testele egal cheltuieli rulate cu succes!")
    ruleaza_teste_repository_cheltuieli()
    print("testele repository cheltuieli rulate cu succes!")
    ruleaza_teste_adauga_cheltuiala_service()
    print("testele adauga cheltuiala service rulate cu succes!")
    ruleaza_teste_sterge_cheltuieli_ziua()
    print("testele sterge cheltuieli ziua rulate cu succes!")
    ruleaza_teste_sterge_cheltuieli_tipul()
    print("testele sterge cheltuieli tipul rulate cu succes!")
    ruleaza_teste_sterge_cheltuieli_interval_zile()
    print("testele sterge cheltuieli interval zile rulate cu succes!")
    ruleaza_teste_elimina_cheltuieli_tipul()
    print("testele elimina cheltuieli tipul rulate cu succes!")
    ruleaza_teste_elimina_cheltuieli_sub_suma()
    print("testele elimina cheltuieli sub suma rulate cu succes!")
    ruleaza_teste_suma_totala_cheltuieli_de_tipul()
    print("testele suma totala cheltuieli de tipul rulate cu succes!")
    ruleaza_teste_ziua_suma_maxima()
    print("testele ziua cu suma maxima rulate cu succes!")
    ruleaza_teste_cheltuieli_cu_suma()
    print("testele cheltuieli cu suma rulate cu succes!")
    ruleaza_teste_sorteaza_cheltuieli_dupa_tip()
    print("testele sorteaza cheltuieli dupa tip rulate cu succes!")
    ruleaza_teste_tiparire_peste_suma()
    print("testele tiparire cheltuiala peste suma rulate cu succes!")
    ruleaza_teste_tiparire_de_tipul()
    print("testele tiparire cheltuiala de tipul rulate cu succes!")
    ruleaza_teste_tiparire_cheltuieli_inainte_de_ziua_sub_suma()
    print("testele tiparire cheltuiala inainte de ziua sub suma rulate cu succes!")
    ruleaza_teste_adauga_operatie_stiva()
    print("testele adauga operatie stiva rulate cu succes!")
    ruleaza_teste_refacere_lista()
    print("testele refacere lista rulate cu succes!")

