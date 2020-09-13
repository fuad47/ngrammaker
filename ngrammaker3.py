from textblob import TextBlob
import csv
from collections import Counter
print('imported')

def text_sentences(file_name):
    # Text fayli acib textblob() obyekti yaradiriq:
    file=open(file_name, 'r')
    comment_list=list(file)
    merged_comments=' '.join(comment_list)
    #merged_comments="I have a blue car. The weather ' is stormy. Do not let him go. I have a blue car."
    comments=TextBlob(merged_comments)
    comments=comments.lower().strip().replace(" ' "," ") # some cleaning..
    print(comments[:1000].sentences)

    # Dublikat cumleleri cixarmaq ucun:
    '''sentence_list=[]
    for sentence in comments.sentences: #sentence adi stringdir, listed[str] yox.
        #print(sentence.ngrams(n)[:1])
        sentence_list.append(sentence)
    sentence_list=list(set(sentence_list))'''
    sentence_list=list(set(comments.sentences))
    return sentence_list
    file.close()

def ngram(n=3): # size of ngrams
# Ngram construction from sentence_list:
    ngram_list=[]
    ngram_list2=[]
    for sentence in text_sentences(): #sentence_list:
        for gram in sentence.ngrams(n):
            ngram_list.append(list(gram)) # convert wordlist object to list () and append to new list.

    for gram in ngram_list: # unnest nested list.
        t=' '.join(gram)
        ngram_list2.append(t)

    print('Ngram_list2: ', ngram_list2[:5])

    # Ngram_list2 Counter() edib fayla yaziriq:
    file=open(str(n)+'gram.csv','w')
    ngram_dict=Counter(ngram_list2)
    for key in ngram_dict:
        #print(Counter(ngram_list2)[key])
        if ngram_dict[key]>1:
            file.writelines(key+','+str(ngram_dict[key])+'\n')
    file.close()

def noun_phrase_gram(file_name,write_file):
# Nounphrase ngram construction from sentence_list:
    nounp_list=[]
    nounp_list2=[]
    for sentence in text_sentences(file_name):   #sentence_list:
        nounp_list.append(sentence.noun_phrases)

    # Noun phraseleri-list2 Counter() edib fayla yaziriq:
    file=open(write_file,'w')
    for phrases in nounp_list:
        for phrase in phrases:
            nounp_list2.append(phrase)
    nounp_dict=Counter(nounp_list2)
    for key in nounp_dict:
        if nounp_dict[key]>1:
            file.writelines(key+','+str(nounp_dict[key])+'\n')

    print('Nounp_list: ',nounp_list[:5])
    file.close()

#ngram()
#noun_phrase_gram()
print('done')
