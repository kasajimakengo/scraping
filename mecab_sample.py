import MeCab

tagger = MeCab.Tagger()
tagger.parse('')

node = tagger.parseToNode('すもももももももものうち')

while node:
    print(node.surface, node.feature)
    node = node.next