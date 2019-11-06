import argparse
import logging
import os

import wiki as w

from gensim.models.fasttext import FastText
from gensim.models.word2vec import Word2Vec
from tqdm import tqdm

WIKIXML = 'data/{lang}wiki.xml.bz2'


def get_args():
    parser = argparse.ArgumentParser(description='Train embedding')
    parser.add_argument('--lang', type=str, default='en', help='language')
    parser.add_argument('--model', type=str, default='word2vec', help='word embedding model')
    parser.add_argument('--output', type=str, required=True, help='output for word vectors')
    parser.add_argument('--size', type=int,default=300, help='embedding size')
    return parser.parse_args()


def main():
    args = get_args()
    # download latest wiki dump
    w.download_wiki_dump(args.lang, WIKIXML.format(lang=args.lang))

    # parse wiki dump
    wiki_sentences = w.WikiSentences(WIKIXML.format(lang=args.lang), args.lang)

    logging.info('Training model %s', args.model)
    if args.model == 'word2vec':
        model = Word2Vec(wiki_sentences, sg=1, hs=1, size=args.size, workers=12, iter=5, min_count=10)
    elif args.model == 'fasttext':
        model = FastText(wiki_sentences, sg=1, hs=1, size=args.size, workers=12, iter=5, min_count=10)
    else:
        logging.info('Unknown model %s, should be "word2vec" or "fasttext"', args.model)
        return
    logging.info('Training done.')

    logging.info('Save trained word vectors')
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('%d %d\n' % (len(model.wv.vocab), args.size))
        for word in tqdm(model.wv.vocab):
            f.write('%s %s\n' % (word, ' '.join([str(v) for v in model.wv[word]])))
    logging.info('Done')


if __name__ == "__main__":
    logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.INFO)
    os.makedirs('data/', exist_ok=True)
    main()