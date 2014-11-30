__author__ = ' '


class Tokenize:

    def get_tokens(self,str):
        n=''
        r=[]
        count=0
        for ch in str:
            if ch.isdigit():
                n+=ch
            else:
                if n!='':
                   r.append(n)
                r.append(ch)
                n=''
            count+=1
            if count==len(str):
                r.append(n)
        return r
