#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().system(' pip install pyarrow')


# In[8]:


comments = pd.read_csv(r'/Users/sandeepkumar/Downloads/UScomments.csv', error_bad_lines=False)


# In[9]:


comments.head()


# In[10]:


comments.tail()


# In[12]:


comments.isnull().sum()   #find out missing values in your data


# In[13]:


comments.dropna(inplace=True) # drop missing values as we have few and lets update dataframe as well


# In[14]:


comments.isnull().sum()


# In[ ]:





# In[15]:


#Perform Sentiment Analysis -- analyzing sentiments of users.


# In[16]:


get_ipython().system('pip install textblob')


# In[18]:


from textblob import TextBlob


# In[19]:


comments.head(6)


# In[20]:


TextBlob("Logan Paul it's yo big day ‼️‼️‼️").sentiment.polarity


# In[22]:


comments.shape


# In[23]:


sample_df = comments[0:1000]


# In[24]:


sample_df.shape


# In[ ]:





# In[ ]:





# In[25]:


polarity = []
for comment in comments['comment_text']:
    try:
        polarity.append(TextBlob(comment).sentiment.polarity)
    except:
        polarity.append(0)
            


# In[26]:


len(polarity)


# In[27]:


comments['polarity']=polarity


# In[28]:


comments.head(5)


# In[ ]:





# In[29]:


#word cloud analysis of data


# In[30]:


filter1 = comments['polarity']==1


# In[31]:


comments_positive = comments[filter1]


# In[32]:


filter2 = comments['polarity']==-1


# In[33]:


comments_negative = comments[filter2]


# In[34]:


comments_positive.head(5)


# In[35]:


comments_negative.head(5)


# In[36]:


get_ipython().system('pip install wordcloud')


# In[38]:


from wordcloud import WordCloud, STOPWORDS


# In[39]:


set(STOPWORDS)


# In[40]:


comments['comment_text']


# In[41]:


type(comments['comment_text'])


# In[42]:


#for wordcloud, we need to frame our 'comment_text' feature into string...


# In[43]:


total_comments_positive=' '.join(comments_positive['comment_text'])


# In[49]:


wordcloud = WordCloud(stopwords=set(STOPWORDS)).generate(total_comments_positive)


# In[50]:


plt.imshow(wordcloud)
plt.axis('off')


# In[ ]:





# In[51]:


total_comments_negative =' '.join(comments_negative['comment_text'])


# In[53]:


wordcloud = WordCloud(stopwords = set(STOPWORDS)).generate(total_comments_negative)


# In[54]:


plt.imshow(wordcloud)
plt.axis('off')


# In[ ]:





# In[ ]:





# In[55]:


#perform Emojis Analysis


# In[56]:


get_ipython().system('pip install emoji')


# In[57]:


import emoji


# In[58]:


emoji.__version__


# In[59]:


comments['comment_text'].head(6)


# In[63]:


comment = 'trending 😉'


# In[84]:


[char for char in comment if char in emoji.EMOJI_DATA]   #by using list comprehension


# In[85]:


emoji_list = []
for char in comment:
    if char in emoji.EMOJI_DATA:
        emoji_list.append(char)


# In[86]:


emoji_list


# In[109]:


all_emojis_list = []
for comment in comments['comment_text'].dropna():
    for char in comment:
        if char in emoji.EMOJI_DATA:
            all_emojis_list.append(char)


# In[116]:


all_emojis_list[0:10]


# In[ ]:





# In[119]:


from collections import Counter


# In[120]:


Counter(all_emojis_list).most_common(10)


# In[124]:


Counter(all_emojis_list).most_common(10)[0]
                                    


# In[125]:


Counter(all_emojis_list).most_common(10)[0][0]


# In[126]:


Counter(all_emojis_list).most_common(10)[1][0]


# In[127]:


Counter(all_emojis_list).most_common(10)[2][0]


# In[128]:


emojis = [Counter(all_emojis_list).most_common(10)[i][0] for i in range(10)]


# In[133]:


Counter(all_emojis_list).most_common(10)[1][1]

                                           


# In[134]:


Counter(all_emojis_list).most_common(10)[0][1]


# In[135]:


Counter(all_emojis_list).most_common(10)[2][1]


# In[138]:


freqs = [Counter(all_emojis_list).most_common(10)[i][1] for i in range(10)]


# In[139]:


freqs


# In[ ]:




