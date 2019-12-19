#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description: it includes the basic components used in 1010! game.
# Author: Yongzhen Ren

import random
import itertools

PLAYFIELD_SIZE = 10
EMPTY = '.'
OCCUPIED = 'x'
DELIMITER = ' '
BORDER = '-'
NEXT_QUEUE_SIZE = 3

p_d = [[OCCUPIED]] # The dot piece.
# Four kinds of horizontal pieces.
p_h1 = [[OCCUPIED, OCCUPIED]]
p_h2 = [[OCCUPIED, OCCUPIED, OCCUPIED]]
p_h3 = [[OCCUPIED, OCCUPIED, OCCUPIED, OCCUPIED]]
p_h4 = [[OCCUPIED, OCCUPIED, OCCUPIED, OCCUPIED, OCCUPIED]]
# Four kinds of vertical pieces.
p_v1 = [[OCCUPIED], [OCCUPIED]]
p_v2 = [[OCCUPIED], [OCCUPIED], [OCCUPIED]]
p_v3 = [[OCCUPIED], [OCCUPIED], [OCCUPIED], [OCCUPIED]]
p_v4 = [[OCCUPIED], [OCCUPIED], [OCCUPIED], [OCCUPIED], [OCCUPIED]]
p_r = [[OCCUPIED, OCCUPIED], [OCCUPIED]]
p_R = [[OCCUPIED, OCCUPIED, OCCUPIED], [OCCUPIED], [OCCUPIED]]
p_l = [[OCCUPIED], [OCCUPIED, OCCUPIED]]
p_L = [[OCCUPIED], [OCCUPIED], [OCCUPIED, OCCUPIED, OCCUPIED]]
p_j = [[EMPTY, OCCUPIED], [OCCUPIED, OCCUPIED]]
p_J = [[EMPTY, EMPTY, OCCUPIED], [EMPTY, EMPTY, OCCUPIED], [OCCUPIED, OCCUPIED, OCCUPIED]]
p_t = [[OCCUPIED, OCCUPIED], [EMPTY, OCCUPIED]]
p_T = [[OCCUPIED, OCCUPIED, OCCUPIED], [EMPTY, EMPTY, OCCUPIED], [EMPTY, EMPTY, OCCUPIED]]
p_o = [[OCCUPIED, OCCUPIED], [OCCUPIED, OCCUPIED]]
p_O = [[OCCUPIED, OCCUPIED, OCCUPIED], [OCCUPIED, OCCUPIED, OCCUPIED], [OCCUPIED, OCCUPIED, OCCUPIED]]

all_pieces = [p_d, p_h1, p_h2, p_h3, p_h4, p_v1, p_v2, p_v3, p_v4, p_r, p_R, p_l, p_L, p_j, p_J, p_t, p_T, p_o, p_O]

class NextQueue:
	def __init__(self, next_queue_size = NEXT_QUEUE_SIZE):
		self.generate_new_pieces(next_queue_size)

	def generate_new_pieces(self, next_queue_size = NEXT_QUEUE_SIZE):
		self.contents = []
		for i in range(next_queue_size):
			self.contents.append(random.choice(all_pieces)) # Independently random.

	def generate_all_place_orders(self):
		orders = []
		for order in [list(item) for item in itertools.permutations(self.contents)]:
			if order not in orders: # Remove possible repetitions.
				orders.append(order)
		return orders

	def print(self):
		for i, pieces in enumerate(self.contents):
			print("Piece #{0}".format(i + 1))
			for blocks in pieces:
				for block in blocks:
					if block == OCCUPIED:
						print(OCCUPIED, end = DELIMITER)
				print()

class Playfield:
	def __init__(self, size = PLAYFIELD_SIZE):
		self.score = 0
		self.rounds = 1
		self.size = size
		self.layout = [[EMPTY] * self.size for i in range(self.size)]

	def if_placeable(self, pos_x, pos_y, piece):
		for i, blocks in enumerate(piece):
			for j, block in enumerate(blocks):
				x = pos_x + i
				y = pos_y + j
				if x >= self.size or y >= self.size or (block == OCCUPIED and self.layout[x][y] == OCCUPIED):
					return False
		return True

	# Use the method ONLY after `if_placeable()` return True.
	def place_one_piece(self, pos_x, pos_y, piece):
		for i, blocks in enumerate(piece):
			for j, block in enumerate(blocks):
				if block == OCCUPIED:
					self.layout[pos_x + i][pos_y + j] = OCCUPIED
		self.clear_lines()

	def clear_lines(self):
		# Vertically.
		clear_rows = []
		for row in range(self.size):
			flag = True
			for column in range(self.size):
				if self.layout[row][column] == EMPTY:
					flag = False
					break
			if flag == True:
				clear_rows.append(row)
		# Horizontally.
		clear_columns = []
		for column in range(self.size):
			flag = True
			for row in range(self.size):
				if self.layout[row][column] == EMPTY:
					flag = False
					break
			if flag == True:
				clear_columns.append(column)

		for row in clear_rows:
			for column in range(self.size):
				self.layout[row][column] = EMPTY

		for row in range(self.size):
			for column in clear_columns:
				self.layout[row][column] = EMPTY

		total_clear_num = len(clear_rows) + len(clear_columns)
		self.score += 5 * total_clear_num * (total_clear_num  + 1)

	def print(self):
		print(BORDER * (2 * self.size + 1))
		print("Round: {0}".format(self.rounds))
		print("Score: {0}".format(self.score))
		print(BORDER * (2 * self.size + 1))
		print(DELIMITER, end = DELIMITER)
		for i in range(self.size):
			print(i, end = DELIMITER)
		print()
		for row in range(self.size):
			print(row, end = DELIMITER)
			for column in range(self.size):
				print(self.layout[row][column], end = DELIMITER)
			print()
		print(BORDER * (2 * self.size + 1))
