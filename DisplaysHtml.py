# -*- coding: utf-8 -*-
import io


class DisplayHtml():
    def __init__(self):
        pass

    def PageCreator(self,filename,lang):
        f_encripted = open(filename, "r").read()
        #print(f_encripted)
        FileProperties = dict(l.rstrip().split('=') for l in io.open("index."+lang+".properties",encoding='utf8') if not l.startswith("#"))
        #print(FileProperties)
        f_decripted = f_encripted % FileProperties
        #print(f_decripted)
        with io.open("index."+lang+".html", 'w', encoding='utf8') as f:
            f.write(f_decripted)







#display = DisplayHtml()
#display.PageCreator("index.en.html","hn")