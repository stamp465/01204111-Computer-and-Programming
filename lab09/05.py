import numpy as np
class Knight:
	def __init__(self,hp):
		self.maxhp = hp
		self.hp = int(hp)
		self.attack = 10
	def heal(self) :
		self.hp += 20
		if self.hp > self.maxhp : self.hp = self.maxhp
		self.attack = 10
	def attack_mon(self):
		self.attack += 2
		return self.attack-2
	def got_attack(self,dmg):
		self.hp -= dmg

class Monster:
	def __init__(self,hp):
		self.hp = int(hp)
	def mon_attack(self,X):
		dmg = X.randint(1, 40)
		#print(dmg)
		return dmg
	def got_attack(self,dmg):
		self.hp -= dmg

def Fight(mon,kni,X) :
	while True :
		at = input('Attack(a) or Heal(h): ')
		if at == 'a' :
			mon.got_attack(kni.attack_mon())
			checkmon = max(0,mon.hp)
			print("Monster's HP left",checkmon)
			if checkmon==0 : return True
		else :
			kni.heal()
			print("Your HP left",kni.hp)


		kni.got_attack(mon.mon_attack(X))
		checkmon = max(0,kni.hp)
		print("Monster's turn : Your HP left",checkmon)
		if checkmon==0 : return False

Blood = int(input("Blood Start: "))  
mon = Monster(Blood)
kni = Knight(Blood)
X = np.random.RandomState(1)
if Fight(mon,kni,X) :
	print('You win.(^_^)')
else : print('You lose and die.(T_T)')