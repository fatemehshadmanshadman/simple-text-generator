from proj5.preprocess import *
from proj5.counting import *
from proj5.GenerateText import *

text_number=input('write your text number witch you want\n')
tweet,len=read_preprocess_file()
pd=simple_learner(tweet,len)
generate(int(text_number),pd,len)  