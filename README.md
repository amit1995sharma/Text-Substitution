# Text-Substitution
Extracting string form HTML file and adding .properties file and from these properties file great a Pseudo Build for different language support

Required command

1) extract-text :- parse the html file and gather text form the tag and replace with with unique key

command : python run.py extract-text

2) generate-resource :- Generate localized Psudo file for the languages
It will add prefix and suffix for example  for hindi prefix is 
"hn":{
    "prefix":"पूर्व",
    "suffix":"पद"
    }
 
similarly If you want to add new language u have to udpate the LangPreffixSuffix.json file

command : python run.py resource --language hindi

3) display-html : -  This will generate the index.hn.html file which will have the localize Psuedo Build

command : python run.py display-html --language hindi

