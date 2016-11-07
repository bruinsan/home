# coding: utf8

class Hand:
    def __init__(self):
        """ list of fingers used in the Hand class
	    and hand name
	"""
        self.fingers = []
	    self.ID = ""

    def setHandName(self, hand_name):
        self.ID = hand_name

    def createFingers(self, list_names):
	""" create the list with the name of each
	    object finger
	"""
        for x in list_names:
	    aux = Finger()
	    aux.setFingerName(x, self.ID)
        self.fingers.append(aux)


class Finger:
    def __init__(self):
        self.name = ""
        self.hand = ""		# IMPORTANT: used to save the hand associated to the finger

    def setFingerName(self, finger_name, hand_name):
	    self.name = finger_name
	    self.hand = hand_name

    def tirarCacaDoNariz(self):
        return "Très bien, on fait quoi maintenant ? On a utilisé {} de la main {}".format(self.name, self.hand)

# ------------------ MAIN PROGRAM ----------------------- #

if __name__ == '__main__':

    list_name = ["le pouce","l'index","le majeur","l'annulaire","l'auriculaire"]	# list of names for fingers

    hand_droite = Hand()
    hand_gauche = Hand()

    hand_droite.setHandName("Right")
    hand_droite.createFingers(list_name)	# create objects fingers inside the class Hand

    hand_gauche.setHandName("Left")
    hand_gauche.createFingers(list_name)	# create objects fingers inside the class Hand

    for _ in hand_droite.fingers:
        print _.tirarCacaDoNariz()	# each finger knows the ID of its hand

    print ""

    for _ in hand_gauche.fingers:
        print _.tirarCacaDoNariz()	# each finger knows the ID of its hand



