from urllib import request
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import pandas as pd
import nltk, re
import glob 
import sys
import subprocess


txt_files = glob.glob("books/*.txt")
print("\n\n\n--------LET THE REVOLUTION-----------\n\n\n")

all_keywords = []

for i in txt_files:
    
    print("Reading Book : "+i)
    
    # 1.1------------------ imporing the dataset from files
    with open(i,"r") as f:
        dataset = f.read()
    
    # 1.2----------------- importing the dataset from url
    
    '''
    url = "http://www.gutenberg.org/files/2554/2554-0.txt"
    response = request.urlopen(url)
    dataset = response.read().decode('utf8')
    '''
    
    # ----------------- tokenize the dataset
    print("Tokenizing the book")
    tokens = word_tokenize(dataset)
    #len(tokens)
    
    
    # --------------bringing the alphabetic words into lower case
    print("Transforming the tokens into lower case")
    words = [w.lower() for w in tokens if w.isalpha()]
    #len(words)
    
    
    #------------- remove stop words
    print("Removing the stop words")
    stop_words = set(stopwords.words('english'))
    stop_words = list(stop_words)
    stop_files = glob.glob("StopWordList/*.txt")
    for k in range(0,len(stop_files)):
        file1 = open(stop_files[k])
        line = file1.read()
        wtr = line.split()
        for r in wtr:
            if not r in stop_words:
                stop_words.append(r)
                
    
    filtered_sentence = [w for w in words if not w in stop_words]
    #len(filtered_sentence)
    
    
    # ------------------- Lemmatizer
    print("Lemmatizing the remaing words")
    wnl = WordNetLemmatizer()
    lemmatized = [wnl.lemmatize(k) for k in filtered_sentence]
    #print(sorted(lemmatized))
    #len(lemmatized)
    
    
    
    # ------------- Frequency calculation
    print("Calculating the frequency distribution")
    fdist = nltk.FreqDist(ch.lower() for ch in lemmatized if ch.isalpha())
    final = fdist.most_common(200)
    
    for q in final:
        if not q in all_keywords:
            all_keywords.append(q)
    
            
    #type(final)
    
    newn1 = i.replace('books/',"")
    newn2 = newn1.replace(".txt","")
    # ------------ saving the list as CSV
    df = pd.DataFrame(final, columns=['word','freq'])
    df1 = df.set_index('word')
    df1.to_csv("csv/"+newn2+".csv")
    print("Storing the frequency into csv named : "+newn2+".csv\n\n")
    

print("------Calling R to make wordclouds---------\n\n")
subprocess.call ("/Library/Frameworks/R.framework/Resources/Rscript --vanilla Frequency.R", shell=True)