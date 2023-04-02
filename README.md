# Gestiune-Cheltuieli

Aplicația gestionează cheltuielile de familie efectuate într-o lună. Ca și entitate principală avem o cheltuială, care are următoarele atribute

    Cheltuiala (ziua, suma, tipul)

## Funcționalități
- Adaugă o nouă cheltuială
- Actualizează cheltuială
- Sterge toate cheltuielile pentru o zi dată 
- Șterge cheltuielile dintr-un interval de timp
- Șterge cheltuielile de un anumit tip
- Tipărește cheltuielile care au suma mai mare decât o sumă dată
- Tipărește cheltuielile efectuate înainte de o anumită zi și care au suma mai mică decât o sumă dată
- Șterge cheltuielile de un anumit tip 
- Tipărește suma totală pentru un anumit tip de cheltuială
- Găsește ziua în care suma cheltuită e maximă
- Tipărește toate cheltuielile ce au o anumită sumă
- Tipărește cheltuielile sortate după tip
- Reface ultima operație efectuată asupra listei de cheltuieli


## Informații generale

Ca și paradigmă de programare este folosită programarea procedurală. Aplicația este împărțită în 3 nivele/straturi: ui(console) -> service(business) -> repo(storage). Aplicația lucrează cu date primite de la utilizator și afișează rezultatele operațiilor efectuate în consolă. 
