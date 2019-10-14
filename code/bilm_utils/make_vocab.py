import argparse
import nltk
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from bilm import dump_token_embeddings
import re

words = set(nltk.corpus.words.words())

def to_keep(word):
    return word.lower() in words or word.isnumeric() or word in string.punctuation

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest='input')
    parser.add_argument("--output", dest='output')
    return parser.parse_args()

def main():
    args = _parse_args()
    # vocab = set(['<S>', '</S>'])
    # braces = re.compile('\(.*\)')
    # preproc = []
    # max_len = 0
    # with open(args.input, 'r') as src:
    #     for line in src:
    #         try:
    #             docid, text = line.split('\t', 1)
    #             text = re.sub(braces, '', text) or text
    #             sentence = sent_tokenize(text)[0]
    #             tokens = word_tokenize(sentence)
    #             max_len = max(len(tokens), max_len)
    #             preproc.append(docid + '\t' + ' '.join(tokens[:20]) + '\n')
    #             for token in tokens:
    #                 vocab.add(token)
    #         except IndexError:
    #             pass
    # print(max_len)
    # with open(args.input + '_prep', 'w+') as dst:
    #     dst.writelines(preproc)
    # with open(args.output, 'w+') as bilm_handle:
    #     bilm_handle.write('\n'.join(vocab))

    options_file = "/Users/asntr/Projects/university/course_work/end2end_neural_el/data/basic_data/elmo/elmo_2x1024_128_2048cnn_1xhighway_options.json"
    weight_file = "/Users/asntr/Projects/university/course_work/end2end_neural_el/data/basic_data/elmo/elmo_2x1024_128_2048cnn_1xhighway_weights.hdf5"
    token_embedding_file = "/Users/asntr/Projects/university/course_work/end2end_neural_el/data/vocabulary/" + 'embeddings.hdf5'
    dump_token_embeddings(
        args.output, options_file, weight_file, token_embedding_file
    )

if __name__ == '__main__':
    main()
