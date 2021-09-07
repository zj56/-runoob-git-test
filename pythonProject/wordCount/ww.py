from jieba.finalseg import cut
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
text = open('d:/ee/彩虹-歌词.txt',"r",encoding="utf-8").read()
# print(text)
cut_text = jieba.cut(text)
result = " ".join(cut_text)
print(result)
wc = WordCloud(
    font_path=r'd:\ee\simhei.ttf',
    background_color='white',
    width=500,
    height=350,
    max_font_size=50,
    min_font_size=10,
)
wc.generate(result)
wc.to_file("d:/ee/wordcloud.png")
plt.figure("jay")
plt.imshow(wc)
plt.axis("off")
plt.show()