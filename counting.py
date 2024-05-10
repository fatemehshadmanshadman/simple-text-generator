import pickle
import os

dir=os.path.dirname(__file__)

def simple_learner(tweets,lens):
    poss_dic={}
    for index in range(max(lens)):
        poss_dic[index]={}
    
    if "poss_pickle" not in os.listdir(dir):     
        for tweet in tweets:
            for i,word in enumerate(tweet):
                try :
                    poss_dic[i][tweet[i]]+=1
                except KeyError:
                    poss_dic[i][tweet[i]]=1
                except IndexError:
                    break
        
        with open(dir+"/poss.pickle",'wb')as handle:
            pickle.dump(poss_dic,handle)
    
    else:
        with open(dir+"/poss.pickle",'rb')as handle:
            poss_dic=pickle.load(handle)
            
    return poss_dic