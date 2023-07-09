import re

import pandas as pd
import streamlit
import wordcloud as WordCloud
def message_stats(selected_user,df):
    if selected_user!='Overall':
        df=df[df['user']==selected_user]
    streamlit.dataframe(df.message)
    emojis = []
    emoji_pattern = "[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF\U00002702-\U000027B0\U000024C2-\U0001F251]+"
    for i in df.message:
        if re.findall(emoji_pattern, i):
            emojis.append(re.findall(emoji_pattern, i))
    words = []
    for message in df['message']:
        words.extend(message.split())
    df2=pd.DataFrame({"Messages" : df['message'] == 'audio omitted'})
    print(df2.value_counts())
    print(df2.shape())
    audio_count = df2.value_counts()[1]
    print(audio_count)
    df3 = pd.DataFrame(df['message'] == ' \u200eaudio omitted\n\u200e')
    audio1_count = df3.value_counts()[1]
    voice_messages=audio_count+audio1_count
    df4 = pd.DataFrame(df['message'] == 'sticker omitted')
    print(df4.value_counts())
    sticker = df4.value_counts()[1]
    df5 = pd.DataFrame(df['message'] == ' \u200esticker omitted\n\u200e')
    sticker1 = df5.value_counts()[1]
    total_stickers = sticker+ sticker1
    return (df.shape[0], len(emojis), voice_messages, total_stickers, len(words)-len(emojis))
# def create_wordcloud(selected_user, df):
#     if selected_user!='Overall':
#         df=df[df['user']==selected_user]
#     wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
#     df_wc = wc.generate(df['message'].str.cat(sep=" "))
#     return df_wc
