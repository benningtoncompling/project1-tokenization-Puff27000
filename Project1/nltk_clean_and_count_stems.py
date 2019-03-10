#!/usr/bin/env python3
#Author: Puff Marx
#03/2019
import re
import nltk
import sys #justin helped with argv
#nltk.download("punkt")

raw_wiki_file = "Wikipedia-LexicalAnalysis.xml"
raw_sample_file = "sample.xml"

def clean_and_stem_XML_data():

    def clean_xml_tags(file):
        with open(file, 'r') as in_file:
            with open("working_file_2.txt", 'w+') as out_file:
                text = in_file.read()
                cleaned_up_text = re.sub(r'<.*?>', r' ', text) #got the question mark meaning nongreedy (smallest possible) match from stackoverflow, sub a space instead of nothing from Justin
                out_file.write(cleaned_up_text)
        return "working_file_2.txt" #Justin

#Level 2: after cleaning tags but before counting the tokens, use nltk's word_tokenizer and porter stemmer

    def stem_and_tokenize(file):
        with open(file, 'r') as raw_text_file:
            tokens = nltk.word_tokenize(raw_text_file.read()) #nltk's list of words
            #print(tokens)
            porter_stemmer = nltk.PorterStemmer()
            stemmed_tokens = []
            for token in tokens:
                stemmed_tokens.append(porter_stemmer.stem(token))

        word_dict = {}  # self-plagiarized from outside project
        for i in range(0, len(stemmed_tokens)):
            if stemmed_tokens[i] in word_dict:
                word_dict[stemmed_tokens[i]] += 1
            else:
                word_dict[stemmed_tokens[i]] = 1

        with open(sys.argv[2], 'w+') as tsv_file:
            alphabetical_word_dict = sorted(word_dict.items())
            for key, value in sorted(alphabetical_word_dict, key=lambda x: (x[1]),
                                     reverse=True):  # lambda idea from stackoverflow
                tsv_file.write('%s\t%s\n' % (key, value))  # idea from Quora

    no_tags_file = clean_xml_tags(sys.argv[1])
    stem_and_tokenize(no_tags_file)

clean_and_stem_XML_data()