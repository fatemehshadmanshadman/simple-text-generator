import random
import os

dir=os.path.dirname(__file__)

def generate(tweets_num,poss_dict,lens):
    for num in range(tweets_num):
        generated_text=""
        text_len=random.randint(min(lens),max(lens))
        for index in range(text_len):
            words=list(poss_dict[index].keys())
            freqs=list(poss_dict[index].values())
            selected_word=random.choices(words,freqs)[0]
            generated_text=generated_text+selected_word+' '
        
        with open(dir+'/generatedText.txt','a+')as f:
            f.write(generated_text+'\n')

# tweet,lens=read_preprocess_file()
# result=simple_learner(tweet,lens)
# generate(50,tweet,lens)       