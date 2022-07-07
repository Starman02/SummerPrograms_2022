import pickle

# jimbo = {'scrimb':25, 'jimmy':27, 26:"""flim grimbo""", "c4":"""Shrimplypibin
# oh my lord i cant believe it 
#     jesus christ you wouldnt believe it.


#     Shrimpy"""}









pickles = open('test.dat', 'rb')






pickle_holder = pickle.load(pickles)
print(pickle_holder)


import pyperclip
pyperclip.copy(pickle_holder("c4"))


# pickle.dump(jimbo, pickles)


