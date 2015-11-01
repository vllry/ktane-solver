#!/usr/bin/python3

import lib



def tap():
	print("TAP AND IMMEDIATELY RELEASE THE BUTTON")

def hold():
	print("HOLD THE BUTTON DOWN")
	print("""[b]lue
[w]hite
[y]ellow
[o]ther""")
	lit_colour = input("Color: ").lower()
	if lit_colour == "b":
		print("RELEASE WHEN THE TIMER CONTAINS A 4")
	elif lit_colour == "w" or lit_colour == "o":
		print("RELEASE WHEN THE TIMER CONTAINS A 1")
	elif lit_colour == "y":
		print("RELEASE WHEN THE TIMER CONTAINS A 5")



def main(dic):
	print("=== THE BUTTON ===")

	print("""[b]lue
	[r]ed
	[w]hite
	[y]ellow""")
	colour = input("Color: ").lower()

	label = input("Label: ").lower()

	#Case 1
	if colour == "b" and label == "abort":
		hold()
		return

	lib.batteries(dic)
	#Case 2
	if dic['batteries'] > 1 and label == "detonate":
		tap()
		return

	#Case 3
	if colour == "w":
		lib.indicators(dic)
		if "car" in dic['indicators']:
			hold()
			return

	lib.batteries(dic)
	#Case 4
	lib.indicators(dic)
	if dic['batteries'] > 2 and "frk" in dic['indicators']:
		tap()
		return

	#Case 5
	if colour == "y":
		hold()
		return

	#Case 6
	if colour == "r" and label == "hold":
		tap()
		return

	#Case 7
	hold()
	return
