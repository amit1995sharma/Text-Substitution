# -*- coding: utf-8 -*-
import re
import random

dict = {}
regexsmall = r'(<b(.)*>|<i(.)*>|<span(.)*>)((.)*)(</i>|</b>|</span>)'
regexNor = r'(<h[12345](.)*>|<td(.)*>|<p(.)*>)((.|(?!</i))*)(</h[12345]>|</td>|</p>)'


class ExtactTexts():
    def __init__(self):
        with open('index.html', 'r') as inputfile:
            lines = inputfile.read()
        FirstFilter = self.fileGenerator(regexsmall, lines, "Stag")
        # print(dict)
        FullFilter = self.fileGenerator(regexNor, FirstFilter, "Ntag")

        # print(FullFilter)

        # print(dict)

        self.properties_creator(dict)

        self.createHTML(FullFilter)

    def properties_creator(self, dictData):
        outputProperties = open("index.en.properties", "w")

        for keys, values in dictData.items():
            outputProperties.write(keys + "=" + values + "\n")
        outputProperties.close()

    def createHTML(self, FileHTML):
        outputHTML = open("index.en.html", "w")
        outputHTML.write(FileHTML)
        outputHTML.close()

    def keyCreator(self, valString, group):
        genstr = re.sub(r' ', '', valString.title())
        keypair = group + "_" + genstr[0:7] + "_" + str(random.randint(0, 10000))
        # print(keypair)
        return keypair

    def fileGenerator(self, regular_regex, Filedata, group="Ntag"):
        Regexdata = re.findall(regular_regex, Filedata)
        # print(len(Regexdata))
        for i in range(len(Regexdata)):
            # print(Regexdata[i][4])

            # key value generator
            while (1):
                keyPair = self.keyCreator(Regexdata[i][4], group)
                if keyPair not in dict:
                    dict[keyPair] = Regexdata[i][4]
                    break
            keyDecorator = "%(" + keyPair + ")s"
            Filedata = re.sub(Regexdata[i][4], keyDecorator, Filedata)
        return Filedata
