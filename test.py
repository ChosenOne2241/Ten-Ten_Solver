#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
	s = set()
	for i in [1, 2, 3, 4, 5, 9]:
		for j in [1, 2, 3, 4, 5, 9]:
			for k in [1, 2, 3, 4, 5, 9]:
				s.add(i + j + k)
	print(s)
	# {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 27}
# In total 22 different sums.
	for l in range(1, 7):
		print(10 * l * (0.5 * l + 0.5))
