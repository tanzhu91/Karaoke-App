import streamlit as st
import urllib.parse
import random



st.set_page_config(page_title="Karaoke App", layout="wide")


st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.postimg.cc/tC0wkXnH/neon-microphone-glowing-border-frame-260nw-2457025063.jpg');
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;
    }
    </style>
    <h1 style="color: #DA70D6; font-size: 62px; text-align: left;">🎸🎸🎸 Karaoke List and Search 🎸🎸🎸</h1>
    """,
    unsafe_allow_html=True
)


if "songs_list" not in st.session_state:
    st.session_state.songs_list = []
if "played_songs" not in st.session_state:
    st.session_state.played_songs = set()


with st.sidebar.form("song_entry_form"):
    name = st.text_input("Enter your name: 👤")
    song = st.text_input("Enter a song name: 🎤")
    submit_button = st.form_submit_button("➕ Add to List")

if submit_button:
    if name and song:
        formatted_song = f"{song} (Karaoke Version)" if "(Karaoke Version)" not in song else song
        entry = f"{name} - {formatted_song}"
        if entry not in st.session_state.songs_list:
            st.session_state.songs_list.append(entry)
        else:
            st.sidebar.warning("⚠️ This song is already in the list.")
    else:
        st.sidebar.warning("⚠️ Please enter both your name and a song.")


if st.session_state.songs_list:
    song_to_remove = st.sidebar.selectbox("Select an entry to remove: 🗑️", st.session_state.songs_list)
    if st.sidebar.button("❌ Remove Selected Entry"):
        st.session_state.songs_list.remove(song_to_remove)
        if song_to_remove in st.session_state.played_songs:
            st.session_state.played_songs.remove(song_to_remove)
        st.rerun()


def get_random_color():

    colors = ["#E57373", "#FFB74D", "#FFF176", "#81C784", "#64B5F6", "#9575CD", "#BA68C8"]  
    return random.choice(colors)

'''

'''

'''

'''

st.markdown("<h2 style='font-size: 33px;'>🎶🎶🎶 Song List 🎶🎶🎶</h2>", unsafe_allow_html=True)


'''

'''
if st.session_state.songs_list:
    for index, item in enumerate(st.session_state.songs_list, start=1):
        song_name = item.split(" - ")[-1]  
        youtube_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(song_name)}"
        if item in st.session_state.played_songs:
            st.markdown(f"<p style='text-decoration: line-through; font-size: 20px; color: grey;'>✔ {index}. {item}</p>", unsafe_allow_html=True)
        else:
            random_color = get_random_color()
            st.markdown(
                f'<a href="{youtube_url}" target="_blank" style="color: {random_color}; display: block; font-size: 30px; text-decoration: none;">🎤 {index}. {item}</a>',
                unsafe_allow_html=True
            )
            if st.button(f"✔ Mark as Played: {index}. {item}", key=f"mark_played_{item}"):
                st.session_state.played_songs.add(item)
                st.rerun()

else:
    st.write("No songs added yet. 🎵")

'''

'''
st.markdown("<h2 style='font-size: 33px;'>🎶🎶🎶 Song List 🎶🎶🎶</h2>", unsafe_allow_html=True)
