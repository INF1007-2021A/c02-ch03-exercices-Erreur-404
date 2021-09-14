#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2 / resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y

	dot_product = v1[0] * v2[0] + v1[1] * v2[1]
	return dot_product == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	sum = 0
	num_values = 0
	for v in values:
		if v >= 0:
			sum += v
			num_values += 1
		pass # La variable v contient une valeur de la liste.
	return sum / num_values

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = tens = fives = ones = 0
	while value != 0:
		if value >= 20:
			twenties += value // 20
			value %= 20
		elif value >= 10:
			tens += value // 10
			value %= 10
		elif value >= 5:
			fives += value // 5
			value %= 5
		elif value >= 1:
			ones += value // 1
			value %= 1

	return (twenties, tens, fives, ones)

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(146))
