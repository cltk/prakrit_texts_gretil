import os, re
import json
import pdb
import collections
from django.utils.text import slugify

sourceLink = 'http://gretil.sub.uni-goettingen.de/#Prakrit'
source = 'GRETIL'

def main():
    if not os.path.exists('cltk_json'):
        os.makedirs('cltk_json')

    for root, dirs, files in os.walk("."):
        path = root.split('/')
        for fname in files:
            if fname.endswith('txt'):
                #print((len(path) - 1) * '---', os.path.basename(root))
                work = {
                            'originalTitle': fname[:-4],
                            'englishTitle': fname[:-4],
                            'author': "Not Available",
                            'source': source,
                            'sourceLink': sourceLink,
                            'language': 'Prakrit',
                            'text': {},
                        }
                text = open(os.path.join(root, fname)).read().splitlines()
                text = [textNode.strip() for textNode in text if len(textNode.strip())]
                for i, textNode in enumerate(text):
                    work['text'][i] = textNode
                
                fname = slugify(work['source']) + '__' + slugify(work['englishTitle']) + '__' + slugify(work['language']) + '.json'
                fname = fname.replace(" ", "")
                with open('cltk_json/' + fname, 'w') as f:
                    json.dump(work, f)

if __name__ == '__main__':
    main()