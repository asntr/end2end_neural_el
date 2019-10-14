import bilm
from bilm import TokenBatcher
import model.config as config
import preprocessing.util as util

if __name__ == '__main__':
    entity_batcher = TokenBatcher(config.base_folder+"data/vocabulary/"+"wiki_vocab.txt")
    with open(
        '/Users/asntr/Projects/university/course_work/end2end_neural_el/data/entities/ent2toks.txt',
        'w+'
    ) as dst, open(
        '/Users/asntr/Projects/university/course_work/end2end_neural_el/data/entities/summary.txt_prep',
        'r'
    ) as src:
        entity2summary = util.load_entity_summary_map()
        for i, (k, v) in enumerate(entity2summary.items()):
            tokens = entity_batcher.batch_sentences([v]).tolist()[0]
            dst.write(k + '\t' + ' '.join([str(i) for i in tokens]) + '\n')
