#!/usr/bin/env python3
import re
#import nltk
#from nltk import word_tokenize

#after data has been cleaned of tags:
# if regex finds a word, if word in dict
# check to see if a dictionary with that key exists.
# if yes, increment the dictionary's value by 1.
# if no, make a dictionary with key word and value set to 1.
# when we've gotten to the end of the document,
# sort the dictionaries with highest integer value at the top
# if the integer values are the same,
# sort by first letter of key value, then second letter, etc
# print key,tab,value, newline of the sorted order to the properly named outfile

raw_wiki_file = "Wikipedia-LexicalAnalysis.xml"
raw_sample_file = "sample.xml"

def clean_XML_data():

    def clean_xml_tags():
        with open(raw_wiki_file, 'r') as in_file:
            with open("working_file.txt", 'w+') as out_file:
                text = in_file.read()
                cleaned_up_text = re.sub(r'<.*?>', r' ', text) #got the question mark meaning nongreedy (smallest possible) match from stackoverflow, sub a space instead of nothing from Justin
                out_file.write(cleaned_up_text)
        return "working_file.txt" #Justin


    def find_and_count_words(file):
        with open(file, 'r') as source_file:
            text = source_file.read()
            all_the_words = re.findall(r'([a-z]+(?:\.?\'?[a-z]+)*)', text.lower()) #?: means non-capturing group, would like to eventually deal with apostrophes better
            #print(all_the_words)
            word_dict = {} #self-plagiarized from outside project
            for i in range(0, len(all_the_words)):
                if all_the_words[i] in word_dict:
                    word_dict[all_the_words[i]] += 1
                else:
                    word_dict[all_the_words[i]] = 1

            with open("lexical_analysis_out.txt", 'w+') as tsv_file:
                alphabetical_word_dict = sorted(word_dict.items())
                for key, value in sorted(alphabetical_word_dict, key=lambda x:(x[1]), reverse=True): #lambda idea from stackoverflow
                    tsv_file.write('%s\t%s\n' % (key, value)) #idea from Quora

    no_tags_file = clean_xml_tags()
    find_and_count_words(no_tags_file)




clean_XML_data()