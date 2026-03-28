import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = """Python Data Science Machine Learning Pandas Matplotlib
          NumPy Statistics Visualization Analysis Deep Learning
          Neural Networks Regression Classification Clustering
          DataFrame Plot Chart Graph Model Training Testing"""

wc = WordCloud(width=800, height=400, background_color='white',
               colormap='coolwarm', max_words=50,
               collocations=False).generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud', fontsize=16, fontweight='bold')
plt.show()
# width/height     — size of the word cloud image
# colormap         — color scheme for the words
# max_words        — maximum number of words to display
# collocations=False — avoids repeating word pairs
# install with: pip install wordcloud