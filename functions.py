from datetime import datetime
from bs4 import BeautifulSoup as bsp
import os, time, spacy, nltk, requests


# Start timer for functinos
def start_function(func_name):
    start_time = time.time()
    print('\n' + ('#' * 80))
    print('Function: %s\nStarting...' % (func_name))
    return start_time


# End timer for functions
def end_function(start_time):
    end_time = time.time() - start_time
    if end_time > 60:
        res = end_time / 60
        res_spl = str(res).split('.')
        mins = res_spl[0]
        secs = round(float('.' + res_spl[1]) * 60, 3)
        print('''Function finished in %s' %s"''' % (mins, secs))
    else:
        print('Function finished in %s"' % round(time.time() - start_time, 3))


# Run
def convert_all():
    start_time = start_function('convert_all')    
    # First move all files in 'converted_resumes' to 'resumes'
    ld = os.listdir('resumes_converted')
    if len(ld) > 0:
        while True:
            answer = input('Move files in the "resumes_converted" folder before proceeding? (y/n): ')
            if answer.lower().strip() not in ('y', 'n'):
                print("You must type either 'y' or 'n'.")
            else:
                break
        if answer.lower().strip() == 'y':
            for i in ld:
                os.rename('resumes_converted/' + i, 'resumes/' + i)
                print('Moved: ' + i)
    print('\nProceeding to file conversions...\n')
    for x, i in enumerate(os.scandir('resumes_working')):
        fname = i.name
        if i.name.endswith('.txt'):
            print('Converting: ' + fname)
            convert_file(fname, x)
        else:
            print("'%s' file is not a .txt file; skipping...\n" % (fname))
    end_function(start_time)


# Check file
def convert_file(file_name, iteration):
    # Read file
    with open('resumes_working/' + file_name, encoding = 'utf8') as mr:
        lines = mr.readlines()
        mr.close()
    # Start appending resume after the line it starts
    file_text = ''
    for x, i in enumerate(lines):
        # Continue if empty line
        if i == '\n':
            continue
        # Start at first character, remove line break, add period and space
        file_text += i[int(i.find(next(filter(str.isalpha, i)))):].rstrip() + '. '
        # Remove extra period
        file_text = file_text.replace('..', '.')
    # Pull data from file name
    resume_info = file_name.replace('.txt', '').split('_')
    header_text = '%s\nLENGTH: %s' % (resume_info[1].upper(), len(file_text.rstrip()))
    print(header_text + '\n')
    # Append text to final converted resumes
    if iteration == 0:
        with open('resumes_converted/' + resume_info[2] + '_' + datetime.now().strftime('%Y%m%d') + '.txt', 'w', encoding = 'utf8') as wf:
            wf.writelines('%s\n%s\n\n' % (header_text, file_text.rstrip()))
    else:
        with open('resumes_converted/' + resume_info[2] + '_' + datetime.now().strftime('%Y%m%d') + '.txt', 'a', encoding = 'utf8') as wf:
            wf.writelines('%s\n%s\n\n' % (header_text, file_text.rstrip()))


# Find keywords
def keyword_search(html_address):
    hres = requests.get(html_address).text
    soup = bsp(hres, 'html.parser')
    # Parse job, department, and office
    banner = soup.find('div', {'class': 'usajobs-joa-banner__body usajobs-joa-banner--pilot__body'})
    jtitle = banner.find('h1').text.strip()
    dtitle = banner.find('h5', {'class': 'usajobs-joa-banner__dept'}).text.strip()
    otitle = banner.find('h5', {'class': 'usajobs-joa-banner__hiring-organization'}).text.strip()
    # Parse all duties
    dsection = soup.find('div', {'id': 'duties'})
    duties = dsection.find_all('li')
    # Append duties to list
    all_duties = []
    for i in duties:
        all_duties.append(i.text.lower())
    # Analyze each list item
    for i in all_duties:
        tags = nltk.pos_tag(nltk.word_tokenize(i))
        #nouns = [word for word, pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
        print(tags[0:])
    # for i in all_duties:
    #     print(i)
    #     doc = spcy(i)
    #     for j in doc.ents:
    #         print(j.text, j.label_)
    # # returns a document of object
    # doc = spcy(text)
      
    # # checking if it is a noun or not
    # if(doc[0].tag_ == 'NNP'):
    #     print(text, " is a noun.")
    # else:
    #     print(text, " is not a noun.")


def keyword_search2():
    sent = 'The man walks to the tree.'
    tkns = nltk.word_tokenize(sent)
    print(tkns)
    tags = nltk.pos_tag(tkns)
    print(tags[0:])

keyword_search('https://www.usajobs.gov/job/707979000')
#keyword_search2()


# pos_tag meanings
# Abbreviation	Meaning
# CC	coordinating conjunction
# CD	cardinal digit
# DT	determiner
# EX	existential there
# FW	foreign word
# IN	preposition/subordinating conjunction
# JJ	This NLTK POS Tag is an adjective (large)
# JJR	adjective, comparative (larger)
# JJS	adjective, superlative (largest)
# LS	list market
# MD	modal (could, will)
# NN	noun, singular (cat, tree)
# NNS	noun plural (desks)
# NNP	proper noun, singular (sarah)
# NNPS	proper noun, plural (indians or americans)
# PDT	predeterminer (all, both, half)
# POS	possessive ending (parent\ ‘s)
# PRP	personal pronoun (hers, herself, him, himself)
# PRP$	possessive pronoun (her, his, mine, my, our )
# RB	adverb (occasionally, swiftly)
# RBR	adverb, comparative (greater)
# RBS	adverb, superlative (biggest)
# RP	particle (about)
# TO	infinite marker (to)
# UH	interjection (goodbye)
# VB	verb (ask)
# VBG	verb gerund (judging)
# VBD	verb past tense (pleaded)
# VBN	verb past participle (reunified)
# VBP	verb, present tense not 3rd person singular(wrap)
# VBZ	verb, present tense with 3rd person singular (bases)
# WDT	wh-determiner (that, what)
# WP	wh- pronoun (who)
# WRB	wh- adverb (how)



