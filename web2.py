#!/usr/bin/python
import urllib

objeto = raw_input("Digite o site: ")
site = urllib.urlopen(objeto)
server = site.info()

print "O servidor web esta rodando:"
print server
