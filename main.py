from textblob import TextBlob
text_Russian= TextBlob(яблоко апельсин банан конец)
print(text_Russian.translate(to='rus')
