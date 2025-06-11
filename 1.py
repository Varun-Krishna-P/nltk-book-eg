from nltk.book import *
import matplotlib.pyplot as plt

# searching text

print(">>>concordance is used to view the every occurence of the given string together with some context.....>>>")
text1.concordance("monstrous")

print(">>>To see similar words within the same range use 'similar' and the word in paranthesis...>>>")
text1.similar("monstrous")

print(">>> common_contexts allows to examine the contexts that are shared by two or more words, enclose the words in a [].... >>>")

text2.common_contexts(["monstrous", "very"])

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
plt.show()
