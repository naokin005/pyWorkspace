start=('Na'*4+'\n')
midle=("Hey"*3+"\n")
print(start[0]+midle)

crypto_list=['Yeti','Bigfoot','Loch Ness Monster']
crypto_string=','.join(crypto_list)
print('UMA:',crypto_string)
crypto='Yety,Bigfoot,Loch Ness Monster'
print(crypto.split(','))

de='''最適化問題とは、与えられた制約条件の下である目的関数の値を最大、
または最小にする解を求めることである。
差分進化とは、決定変数が実数値をとる関数最適化問題
を対象とした進化計算アルゴリズムの一種であり、
目的化関数に微分可能性や凸性の仮定を必要とせず大域的最適解を探索できる。
DEの最大の魅力は制御パラメータが少なくアルゴリズム
が非常にシンプルであるにもかかわらずまずまずの探索性能が期待できる。'''

print(len(de))
print(de.startswith('最適'))
word='差分'
print(de.find(word))

seconds_per_hour=60*60
print(seconds_per_hour)

seconds_per_day=seconds_per_hour*24
print(seconds_per_day)

print(seconds_per_day/seconds_per_hour)

print(seconds_per_day//seconds_per_hour)

