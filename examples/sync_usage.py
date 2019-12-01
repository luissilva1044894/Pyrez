
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

import pyrez

fake_dev_id=1004
fake_auth_key='23DF3C7E9BD14D84BF892AD206B6755C'

def standard():
	paladins = pyrez.api.Paladins(fake_dev_id, fake_auth_key)
	print(paladins.data_used())
	paladins.close()

def context_manager():
	"""Context manager"""
	with pyrez.api.Smite(fake_dev_id, fake_auth_key) as smite:
		print(smite.data_used())

def main():
	standard()
	context_manager()

if __name__ == '__main__':
	main()
