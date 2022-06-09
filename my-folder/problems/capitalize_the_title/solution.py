class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.split()
        newtitle=[]
        for word in title:
            word=word.lower()
            if len(word)>2:
                word=str(str(word[0]).upper())+str(word[1:])
            newtitle.append(word)
        return(' '.join(newtitle))
        