# -*- coding: utf-8 -*-
import json
import codecs

class PropertiesGen():
    def __init__(self):
        pass

    def properties_creator(self , dictData,lang):
        outputProperties = open("index."+lang+".properties", "w",encoding="utf-8")

        for keys, values in dictData.items():
            outputProperties.write(keys + "=" + values + "\n")
        outputProperties.close()

    def convert(self,fileName,lang):
        print(fileName)
        print(lang)
        FileProperties = dict(l.rstrip().split('=') for l in open(fileName) if not l.startswith("#") )
        #LangPreffixSuffix.json
        JsonFile = codecs.open( "LangPreffixSuffix.json", "r", "utf-8" )
        Data = json.loads(JsonFile.read())
        prefix = Data[lang]["prefix"]
        suffix = Data[lang]["suffix"]
        ##creating dict with unicode file
        for keys, values in FileProperties.items():
            FileProperties[keys] = prefix + values + suffix
        self.properties_creator(FileProperties,lang)




#convertor = PropertiesGen()

#convertor.convert("index.en.properties","hn")




