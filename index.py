#!/usr/bin/python3

print("Content-Type: text/html")
print("")

template = open("templates/index.html", "r").read()
print(template)
