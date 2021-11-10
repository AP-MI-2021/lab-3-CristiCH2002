def afisare_menu():
    print("1.Citire date")
    print("2.Determinare cea mai lungă subsecvență cu proprietatea:Toate numerele sunt pătrate perfecte.")
    print("3.Determinare cea mai lungă subsecvență cu proprietatea:Toate numerele au același număr de divizori.")
    print("4.Determinare cea mai lungă subsecvență cu proprietatea:Toate numerele sunt neprime.")
    print("5.Ieșire.")
def citire_date():
    lst = input("lista de nr este(cu virgula intre elemente): ")
    lst = lst.split(",")
    lst = [int(el) for el in lst]
    return lst
def patrat_perfect(n):
    '''
    Calculeaza daca n este patrat perfect
    :param n: int,nr ul dat
    :return: True/False
    '''
    for i in range(1,n+1):
        if i*i==n:
            return True
    return False
def test_patrat_perfect():
    assert(patrat_perfect(25)==True)
    assert (patrat_perfect(16) == True)
    assert (patrat_perfect(2) == False)
    assert (patrat_perfect(31) == False)

def get_longest_all_perfect_squares(lst):
    '''
    Determina cea mai lunga subsecventa de patrate perfecte
    :param lst: list,lista data
    :return: list,subsecventa ceruta
    '''
    lmax=0
    l=0
    j=-1
    for i,el in enumerate(lst):
        if patrat_perfect(el)== True:
            l=l+1
        else :
            l=0
        if lmax<l:
            lmax=l
            j=i
    rez=[]
    for i in range(j-lmax+1,j+1):
        rez.append(lst[i])
    return rez

def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([1,2,3,4,5,16,36,64,121,5]) == [16,36,64,121]
    assert get_longest_all_perfect_squares([7,11,19,-3,0]) == []
    assert get_longest_all_perfect_squares([4,9,16,25,17,1,4,4,9,36,400]) == [1,4,4,9,36,400]


def divizori(n):
    '''
    Calculeaza nr ul de divizori ai lui n
    :param n: int,nr ul dat
    :return: int,nr de divizori
    '''
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt=cnt+1
    return cnt
def test_divizori():
    assert(divizori(6)==4)
    assert (divizori(4) == 3)
    assert (divizori(11) == 2)
    assert (divizori(41) == 2)

def get_longest_same_div_count(lst):
    '''
    Determina cea mai lunga subsecventa cu nr cu acelasi nr de divizori
    :param lst: list,lista data
    :return: list,subsecventa ceruta
    '''
    lmax=0
    l=0
    j=-1
    nrdiv=-1
    for i,el in enumerate(lst):
        if divizori(el)==nrdiv:
            l=l+1
        else:
            l=1
            nrdiv=divizori(el)
        if lmax<l :
            lmax=l
            j=i
    rez = []
    for i in range(j - lmax + 1, j + 1):
        rez.append(lst[i])
    return rez
def test_get_longest_same_div_count() :
    assert get_longest_same_div_count([4,7,11,17,19,22,32]) == [7,11,17,19]
    assert get_longest_same_div_count([5,4,9,25,121,169,74,0]) ==[4,9,25,121,169]
    assert get_longest_same_div_count([6,77,39,35]) == [6,77,39,35]
def prim(n):
    '''
    Determina daca n este nr prim
    :param n:int,nr pe care vrem sa il verificam
    :return:True/False
    '''
    if n<2:
        return False
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
def get_longest_all_not_prime(lst):
    '''
    Determina cea mai lunga subsecventa de nr neprime
    :param lst:list,lista de nr
    :return:list,subsecventa data
    '''
    j=-1
    lmax=0
    l=0
    for i,el in enumerate(lst):
        if not prim(el):
            l=l+1
        else:
            l=0
        if l>lmax:
            lmax=l
            j=i
    rez=[]
    for i in range(j-lmax+1,j+1):
        rez.append(lst[i])
    return rez
def test_get_longest_all_not_prime():
    assert( get_longest_all_not_prime([1,2,3,4,6,8])==[4,6,8])
    assert( get_longest_all_not_prime([12,14,18,1,0])==[12,14,18,1,0])
    assert( get_longest_all_not_prime([3,5,7,11])==[])
    assert( get_longest_all_not_prime([81,17,19,57])==[81])
def test_prim():
    assert(prim(7)==True)
    assert (prim(5) == True)
    assert (prim(6) == False)
    assert (prim(4) == False)

def start():
    lst=[]
    while True:
        afisare_menu()
        optiune=int(input("Selectati optiunea: "))

        if optiune==1:
            lst=citire_date()
        elif optiune==2:
            rez=get_longest_all_perfect_squares(lst)
            print("Subsecventa este: ",rez)
        elif optiune==3:
            rez=get_longest_same_div_count(lst)
            print("Subsecventa este: ",rez)
        elif optiune==4:
            rez=get_longest_all_not_prime(lst)
            print("subsecventa este: ",rez)
        else:
            break
test_get_longest_all_not_prime()
test_prim()
test_get_longest_same_div_count()
test_divizori()
test_get_longest_all_perfect_squares()
test_patrat_perfect()
start()

