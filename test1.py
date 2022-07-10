from janome.tokenizer import Tokenizer
import numpy as np
from numpy.random import *
import random

#import tensorflow






#設定


#素材の選択
SozaiNum = '1'

#numpyの表示形式
np.set_printoptions(suppress=True,linewidth=1000000)



#宣言

input = str()
output = str()

dna = ()    #配列
tango = ()  #連想配列からの連想配列（やけくそ） tango[単語][Vector,Next]

Sozai = str()
wakatied = list()




#ファイル読み込み

with open('input.txt', 'r', encoding="utf-8") as f:
    input =f.read()

with open('sozai/' + SozaiNum + '.txt', 'r', encoding="utf-8") as f:
    Sozai =f.read()


tango = np.load('SaveData/tango.npy', allow_pickle=True)
dna = np.load('SaveData/dna.npy', allow_pickle=True)



#こっからメイン処理



#分かち書き
tokenizer = Tokenizer(wakati=True)
wakatied = list(tokenizer.tokenize(Sozai))


#単語の辞書作る

tango = {}

for element in set(wakatied):
    tango[element] = {}
    tango[element]['Vector'] = rand(25)
    tango[element]['Next'] = list()
    
for i in range(len(wakatied) - 1):
    tango[wakatied[i]]['Next'].append(wakatied[i+1])



#文章生成

output = list()

output.append(random.choice(list(tango)))

for _ in range(1000):
    output.append(random.choice(tango[output[-1]]['Next'])) #最後尾の単語を辞書で引いて、次の単語を決める。

#見た目を整える

output = (''.join(output))




#アウトプット

#output = str(tango).replace("]}, '","]}, \n'")
#output = tango['乱入']['Next']



print(output)




#ファイル出力

with open('output.txt', 'w', encoding="utf-8") as f:
    f.write(str(output))

with open('SaveData/tango.txt', 'w', encoding="utf-8") as f:
    f.write(str(tango))
np.save('SaveData/tango', tango)
    
with open('SaveData/dna.txt', 'w', encoding="utf-8") as f:
    f.write(str(dna))
np.save('SaveData/dna', dna)

