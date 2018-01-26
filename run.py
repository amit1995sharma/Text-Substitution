# -*- coding: utf-8 -*-
import ExtractTestFinal
import GenerateResource
import DisplaysHtml

import sys
import os

languages = {"hindi": "hn", "tamil": "tn", "punjabi": "pb", "marathi": "mh"}

if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg1 = sys.argv[1]
        if arg1 == "extract-text":
            ExtractTestFinal.ExtactTexts()
            print("Creates english properties file you : \n" + os.getcwd() + "/index.en.properties")
    elif len(sys.argv) == 4:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        lang1 = sys.argv[3]
        if arg1 == "resource" and arg2 == "--language":
            if "index.en.properties" in os.listdir() and lang1 in languages.keys():
                convertor = GenerateResource.PropertiesGen()
                convertor.convert("index.en.properties", languages[lang1])
                print("proterties file created \n" + os.getcwd() + "/index." + languages[lang1] + ".properties")
            else:
                print(
                    "Please run the \"python run.py extract-text\" before using the command\nor check the langage first")
        elif arg1 == "display-html" and arg2 == "--language":
            if "index.en.properties" in os.listdir() and lang1 in languages.keys() and "index." + languages[
                lang1] + ".properties" in os.listdir():
                display = DisplaysHtml.DisplayHtml()
                display.PageCreator("index.en.html", languages[lang1])
                print("htmlfile file created \n" + os.getcwd() + "/index." + languages[lang1] + ".html")
            else:
                print("Please run the extract-text and resource --language hindi command \nfirst or check the language")
