import streamlit as st
import preprocess
import helper
import matplotlib.pyplot as plt
st.sidebar.title("Whatsapp Chat Analysis")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    # st.text(data) Used to display string data
    df=preprocess.preprocessing(data)
    #st.dataframe(df)
    user_list = df['user'].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)
    if st.sidebar.button("Show Analysis"):
        col1,col2,col3=st.columns(3)
        total_messages, total_emojis, audio_messages, total_stickers, total_words = helper.message_stats(selected_user, df)
        with col1:
            st.header("Total Messages")
            st.title(total_messages)
        with col2:
            st.header("Total Emojis")
            st.title(total_emojis)
        with col3:
            st.header("Total words")
            st.title(total_words)
        col4, col5, col6 = st.columns(3)
        with col4:
            st.header("Stickers")
            st.title(total_stickers)
        with col5:
            st.header("VoiceMessages")
            st.title(audio_messages)
    # df_wc = helper.create_wordcloud(selected_user, df)
    # fig, ax = plt.subplots()
    # ax.imshow(df_wc)
    # st.pyplot(fig)