#!/usr/bin/python3
import cgi
import importlib
import json
import os
import random

print("Content-Type: text/html")
print("")

template = open("templates/index.html", "r").read()

methods = os.listdir("methods/")


def make_checkbox(name, value, classes="", checked=False):
    checked_str = "checked" if checked else ""
    return "<input type=\"checkbox\" name=\"" + name + "\" value=\"" + value + "\" class=\"" + classes + "\" " + checked_str + ">"


method_checkboxes = ""

for x in methods:
    method_checkboxes += make_checkbox("", x[:-3], "method-check", True) + x[:-3] + "<br>\n"

template = template.replace("#METHOD_CHECKBOXES#", method_checkboxes)
template = template.replace("#RAND_INT#", str(random.randrange(1, 100000)))


print(template)
