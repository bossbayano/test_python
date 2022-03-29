# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

class Tondeuse:

    def __init__(self, position_initiale,  instruction):
        self.position_initiale = position_initiale
        self.X = int(self.position_initiale[0])
        self.Y = int(self.position_initiale[1])
        self.O = self.position_initiale[2].lower()
        self.instruction = instruction.lower()
        self.deja_deplace = False

    def directionX(self):
        if self.O == "e":
            self.X += 1
        if self.O == "w":
            self.X -= 1

    def directionY(self):
        if self.O == "n":
            self.Y += 1
        if self.O == "s":
            self.Y -= 1

    def orientation(self, direction):
        if direction == "g":
            if self.O == "n":
                self.O = "w"
            elif self.O == "s":
                self.O = "e"
            elif self.O == "e":
                self.O = "n"
            elif self.O == "w":
                self.O = "s"
        elif direction == "d":
            if self.O == "n":
                self.O = "e"
            elif self.O == "e":
                self.O = "s"
            elif self.O == "s":
                self.O = "w"
            elif self.O == "w":
                self.O = "n"

    def deplacement(self):
        if self.deja_deplace:
            pass
        else:
            for instruction in self.instruction:
                if instruction in ['g', 'd']:
                    self.orientation(instruction)
                elif instruction == 'a':
                    self.directionX()
                    self.directionY()

            self.deja_deplace = True

    def position_finale(self):
        return f"{self.X}{self.Y}{self.O}"


class Fichiers:
    def __init__(self, fichier):
        self.fichier = open(fichier,"r")
        self.position_finales = []
        self.position_depart =  []
        self.Position_principale = ""
        self.deja_deplace = False

    def Collecte(self):
        ligne1 = True
        i = 0
        for line in self.fichier:
            if ligne1:
                self.Position_principale = line
                ligne1 = False
            else:
                self.position_depart[0] = line
                i+=1

    def deplacements(self):
        finale = 0
        for i in range(len(self.position_depart)):
            if i%2 == 0:
                tondeuse = Tondeuse(self.position_depart[i], self.position_depart[i+1])
                tondeuse.deplacement()
                self.position_finales[finale] = tondeuse.position_finale()
            else:
                pass

    def position_finale(self):
        return str(self.position_finale())




if __name__ == '__main__':
    erreur = True
    choix = 0
    while(erreur):
        print("1 pour fichier, 2 pour test d'instruction")
        choix = input()
        try:
            choix = int(choix)
            print(f"choix: {choix}")
            if choix in [1,2]:
                erreur = False
            else:
                erreur = True
        except:
            erreur = True

    if choix == 2:
        encore = 1
        while encore == 1:
            Position_principale = input("position principlae")
            position_initiale = input("position initiale")
            instruction = input("intstruction")

            tondeuse = Tondeuse(position_initiale, instruction)
            tondeuse.deplacement()
            print(f"position finale: {tondeuse.position_finale()}")

            erreur = True
            while (erreur):
                print("\n1 pour nouveau test 0 pour sortir")
                encore = input()
                try:
                    encore = int(encore)
                    if encore in [1,2]:
                        erreur = False
                    else:
                        erreur = True
                except:
                    erreur = True
    else:
        encore = 1
        while encore == 1:
            fichier = input("chemin du fichier")
            try:
                Fichier = Fichiers(fichier)
                Fichier.deplacements()
                print(f"position finale: {Fichier.position_finale()}")
            except :
                print("erreur chemin du fichier")

            erreur = True
            while (erreur):
                print("\n1 pour nouveau test 0 pour sortir")
                encore = input()
                try:
                    encore = int(encore)
                    if encore in [1, 2]:
                        erreur = False
                    else:
                        erreur = True
                except:
                    erreur = True



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
