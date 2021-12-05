import time

espace =[]
espace_dispo =0
espace_total =0
compteurs_espace =0
lignes=0
frontiere=""

#classe pour declarer vehicule
class vehicule:
    def __init__(self ,v_type ,temps_entree):
        self.type =v_type
        self.temps_entree =time.time()

    def saisie_type(self):
        if self.type==1:
            return "voiture"
        if self.type==2:
            return "trax"
        if self.type==3:
            return "moto"

    def temps_entre(self):
            return self.temps_entree

    def vehicule_information(self):
        print ( self.type ,self.temps_entree)

    def type_vehicule(self):
        return self.type

    def temps_entree_vehicule(self):
        return self.temps_entree


#classe pour declarer espace pour parker
    class espace:

        def __init__(self):
            self.occupee =False
            self.vehicule =None

        def ajout_vehicule(self):
            self.occupee =True
            self.vehicule =vehicule

        def efface_vehicule(self):
            v_exit = self.vehicule
            self.vehicule = None
            self.occupee= False
            return v_exit

        def est_disponible(self):
            return self.occupee

        def vehicule_info(self):
            return self.vehicule

#tracage du parking
def tracage_lignes(lignes):
    l=""
    l+="|"
    start=compteurs_espace*lignes
    end=compteurs_espace*(lignes+1)
    for i in range (start,end):
        espace_dispo=espace[i].est_disponible()
        if espace_dispo==True :
            l+="[]"
        else:
           l+="["
           type_vehicule=espace[l].vehicule_information().type_vehicule()
           if type_vehicule == 1:
               l+="v"
           if type_vehicule == 2:
               l+="t"
           else:
               l+="m"
               l+="]"
               final_element=compteurs_espace*(lignes+1)-1
           if i<final_element:
            l+=""
            l+="|"
            return l



  #affichage d'une place
def affiche_lot():
    global espaces, espace_dispo, espace_total, lignes

    output = "place disponible: " + str(espace_dispo) + "\n"

    output += frontiere

    for lignes in range(lignes):
        output += tracage_lignes(lignes) + "\n"

    output += frontiere
    return output


 #affichage d'espace 
def affiche_espace_selectionne():
    global espaces, espace_dispo, espace_total, lignes

    output = "espaces: " + int(lignes) + "\n"
    output += frontiere
    output += tracage_lignes(int(lignes)) + "\n"

    output += " "
    for i in range(compteurs_espace):
        if i < 10:
            output += "<" + str(i) + "> "
        else:
            output += "<" + str(i) + ">"

    output += "\n"
    output += frontiere
    return compteurs_espace

#entrer une vehicule au parking
def entree_vehicule():
    global espace, espace_dispo, espace_total, lignes
    if espace_dispo == 0:
        affiche_lot()
        print("Erreur: pas espaces!")

    else:
        affiche_espace_selectionne()
        print("vehicule en place")

    new_vehicule = Vehicule(v_type)
    espace.ajout_vehicule(new_vehicule)
    espace_dispo-= 1
    affiche_lot()
    print("Vehicule est ajoute au place \n")
    return new_vehicule


#sortir d'une vehicule du parking
def sortie_vehicule():
    global espace_dispo
    i=(int(lignes) * compteurs_espace() + int(espace))
    if espace[i].est_disponible()==False:
        affiche_espace_selectionne(lignes)
        print ("erreur:pas de vehicule")
    removed = espaces[i].efface_vehicule()
    espace_dispo += 1
    affiche_lot()

#programme principale

espace=5
espace_dispo=0
lignes=4
time_to_exit=False
v1=vehicule(1,9)
tracage_lignes(lignes)
print("v1:",v1.saisie_type())
print("temps entree:",v1.temps_entre())
print("veuillez choisir parmi ces options:")
p=print("P=park vehicule")
q=print("Q=quitter le parking")
v=print("V=voir une vehicule au parking")
choix=input("choix:")

if choix=="p":
 if espace_dispo==0:
  print("pas espace !")
  
if espace_dispo>0:
 v1=entree_vehicule()
 affiche_lot()
 affiche_espace_selectionne()
 espace_dispo=espace_dispo-1


if choix=="q":
 time_to_exit=True
 sortie_vehicule()
 espace.efface_vehicule(v1)
 
if choix=="v":
 affiche_lot()
 print("votre vehicule est place dans la ligne",affiche_du_ligne_selectionne())
 

 

 
