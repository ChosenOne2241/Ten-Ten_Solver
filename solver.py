#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description: it contains a solver using the risk function.
# Author: Yongzhen Ren

from utilities import *
import copy

def calculate_risk(playfield):
	risk_list = []

	# Rows.
	for row in range(playfield.size):
		flag = playfield.layout[row][0]
		num = 1
		for column in range(1, playfield.size):
			if playfield.layout[row][column] == flag:
				num += 1
			else:
				flag = playfield.layout[row][column]
				risk_list.append(num)
				num = 1
		risk_list.append(num)

	# Columns.
	for column in range(playfield.size):
		flag = playfield.layout[0][column]
		num = 1
		for row in range(1, playfield.size):
			if playfield.layout[row][column] == flag:
				num += 1
			else:
				flag = playfield.layout[row][column]
				risk_list.append(num)
				num = 1
		risk_list.append(num)

	risk = len(risk_list)
	return risk

def greedy_place(next_queue, playfield):
	risk_dict_all_orders = dict() # 3!
	for order in next_queue.generate_all_place_orders():
		new_playfield = finish_one_order(order, playfield)
		if new_playfield is not None:
			risk_dict_all_orders[calculate_risk(new_playfield)] = new_playfield

	k = min(risk_dict_all_orders, key = int)
	return risk_dict_all_orders[k]

def finish_one_order(order, playfield):
	new_playfield = copy.deepcopy(playfield)
	for piece in order:
		risk_dict_one_piece = dict()
		for row in range(playfield.size):
			for column in range(playfield.size):
				if new_playfield.if_placeable(row, column, piece):
				# At least one position is placeable for the current piece.
					dummy_playfield = copy.deepcopy(new_playfield) # Deep copy.
					dummy_playfield.place_one_piece(row, column, piece)
					risk_dict_one_piece[calculate_risk(dummy_playfield)] = (row, column)
		if bool(risk_dict_one_piece) == False: # No item is in the dictionary.
			return # Go to the next order.
		else:
			k = min(risk_dict_one_piece, key = int)
			row, column = risk_dict_one_piece[k]
			new_playfield.place_one_piece(row, column, piece)

	return new_playfield

if __name__ == "__main__":
	next_queue = NextQueue()
	next_queue.print()

	playfield = Playfield()
	risk = calculate_risk(playfield)
	print(risk)
	playfield = greedy_place(next_queue, playfield)
	risk = calculate_risk(playfield)
	playfield.print()
	print("The risk of the current playfield is {0}".format(risk))
