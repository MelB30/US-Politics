import streamlit as st
import modal
import json
import os

def main():

 with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    col1, col2 = st.columns([2, 8])
    with col1:
        st.image("logo.png", caption="", use_column_width=True)

    with col2:
        st.title("NAVIGATING POLITICS IN AMERICA")

    available_podcast_info = create_dict_from_json_files('.')

    tcol1, tcol2 = st.columns([2, 8])

    with tcol1:

        st.sidebar.image("podcast-live-icon.svg", caption="", width=50, use_column_width=False)


# Dropdown box
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox("Select Podcast", options=available_podcast_info.keys())

    # User Input box
    st.sidebar.subheader("Add and Process New Podcast Feed")
    st.sidebar.markdown(
                f"<p style='margin-bottom: 5px; color:#000; font-style:italic; font-weight: bold;'>Don't Use RSS feed. Use the castbox Podcast URL</p>", unsafe_allow_html=True)

    url = st.sidebar.text_input("Spotify Podcast URL", placeholder="example: https://open.spotify.com/episode/0jbyb1Io0Ge9H0WBrhg70L)

    st.title("AMERICAN POLITICS NEWSLETTER")

process_button = st.sidebar.button("Process Podcast Feed")
    st.sidebar.markdown("**Note**: Podcast processing can take upto 5 mins, please be patient.")

    if selected_podcast:

        podcast_info = available_podcast_info[selected_podcast]

        # Right section - Newsletter content
        st.header(":orange[Newsletter Summary]")
        st.image("podcast-mic.png", use_column_width=False)

        # Display the podcast title
        st.subheader(":orange[Episode Title]")
        # st.write(podcast_info['podcast_details']['episode_title'].replace(".mp3",""))
        st.markdown(
                f"<p style='margin-bottom: 2px; font-size: 22px;'>{podcast_info['podcast_details']['episode_title'].replace('.mp3','')}</p>", unsafe_allow_html=True)

        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])

        with col1:
            # Display the podcast episode summary
            st.subheader(":orange[Podcast Episode Summary]")
            st.write(podcast_info['podcast_summary'])

        with col2:

            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover",  use_column_width=True)

            # Episode Score By AI

            st.markdown(
                    f"""<div style='background-color: #FF5F2A; padding: 11px; border-radius: 9px;'><h3 style='margin-bottom: 5px; color:#273346; text-align: center;'>Score By AI</h3>
                    <p style='margin-bottom: 5px; text-align: center; font-size: 28px; color: #ffffff; font-weight: bold;'>{round(float(podcast_info['podcast_score']['score']),1)}/5.0</p>
                    </div>""", unsafe_allow_html=True)

        # Display the podcast guest and their details

        st.subheader(":orange[Episode Guest]")
        st.write(podcast_info['podcast_guest'])


        st.subheader(":orange[Guest Informarion]")
        # st.write(podcast_info["podcast_guest_details"]['Guest Job'])
        guest_details = podcast_info["podcast_guest_details"]
        for info in guest_details:

            st.markdown(
                f"<p style='margin-bottom: 2px;'><span style='font-weight: bold;'>{info}:</span> {guest_details[info]}</p>", unsafe_allow_html=True)


         # Display the Episode Review
        st.subheader(":orange[Review By AI]")
        # st.write(podcast_info['podcast_score']['review'])
        st.markdown(
                f"<p style='background-color: #FF5F2A; padding: 11px; border-radius: 9px; font-weight: bold;'>{podcast_info['podcast_score']['review']}</p>", unsafe_allow_html=True)

        # Display the four key moments
        st.subheader(":orange[Key Moments]")
        key_moments = podcast_info['podcast_highlights']

        st.markdown(
                f"<ul style='margin-bottom: 5px;>", unsafe_allow_html=True)
        for moment in key_moments:

            st.markdown(
                f"<li style='margin-bottom: 5px;'>{key_moments[moment]}</li>", unsafe_allow_html=True)

        st.markdown(
                f"</ul>", unsafe_allow_html=True)

    if process_button:

        # Call the function to process the URLs and retrieve podcast guest information
        podcast_info = process_podcast_info(url)

        # Display the podcast title
        st.subheader(":orange[Episode Title]")
        # st.write(podcast_info['podcast_details']['episode_title'].replace(".mp3",""))
        st.markdown(
                f"<p style='margin-bottom: 2px; font-size: 22px;'>{podcast_info['podcast_details']['episode_title'].replace('.mp3','')}</p>", unsafe_allow_html=True)

        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])

        with col1:
            # Display the podcast episode summary
            st.subheader(":orange[Podcast Episode Summary]")
            st.write(podcast_info['podcast_summary'])

        with col2:

            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover",  use_column_width=True)

            # Episode Score By AI

            st.markdown(
                    f"""<div style='background-color: #FF5F2A; padding: 11px; border-radius: 9px;'><h3 style='margin-bottom: 5px; color:#273346; text-align: center;'>Score By AI</h3>
                    <p style='margin-bottom: 5px; text-align: center; font-size: 28px; color: #ffffff; font-weight: bold;'>{round(float(podcast_info['podcast_score']['score']),1)}/5.0</p>
                    </div>""", unsafe_allow_html=True)

        # Display the podcast guest and their details

        st.subheader(":orange[Episode Guest]")
        st.write(podcast_info['podcast_guest'])


        st.subheader(":orange[Guest Informarion]")
        # st.write(podcast_info["podcast_guest_details"]['Guest Job'])
        guest_details = podcast_info["podcast_guest_details"]
        for info in guest_details:

            st.markdown(
                f"<p style='margin-bottom: 2px;'>{info}: {guest_details[info]}</p>", unsafe_allow_html=True)


         # Display the Episode Review
        st.subheader(":orange[Review By AI]")
        # st.write(podcast_info['podcast_score']['review'])
        st.markdown(
                f"<p style='background-color: #FF5F2A; padding: 11px; border-radius: 9px; font-weight: bold;'>{podcast_info['podcast_score']['review']}</p>", unsafe_allow_html=True)

        # Display the four key moments
        st.subheader(":orange[Key Moments]")
        key_moments = podcast_info['podcast_highlights']

        st.markdown(
                f"<ul style='margin-bottom: 5px;>", unsafe_allow_html=True)
        for moment in key_moments:

            st.markdown(
                f"<li style='margin-bottom: 5px;'>{key_moments[moment]}</li>", unsafe_allow_html=True)

        st.markdown(
                f"</ul>", unsafe_allow_html=True)


    available_podcast_info = create_dict_from_json_files('.')

    # Left section - Input fields
    st.sidebar.header("Podcast RSS Feeds")

    # Dropdown box
    st.sidebar.subheader("Available Podcasts Feeds")
    selected_podcast = st.sidebar.selectbox("Select Podcast", options=available_podcast_info.keys())

    if selected_podcast:

        podcast_info = available_podcast_info[selected_podcast]

        # Right section - Newsletter content
        st.header("Newsletter Content")

        # Display the podcast title
        st.subheader("Episode Title")
        st.write(podcast_info['podcast_details']['episode_title'])

        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])

        with col1:
            # Display the podcast episode summary
            st.subheader("Podcast Episode Summary")
            st.write(podcast_info['podcast_summary'])

        with col2:
            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)

        # Display the podcast guest and their details in a side-by-side layout
        col3, col4 = st.columns([3, 7])

        with col3:
            st.subheader("Podcast Guest")
            st.write(podcast_info['podcast_guest']['name'])

        with col4:
            st.subheader("Podcast Guest Details")
            st.write(podcast_info["podcast_guest"]['summary'])

        # Display the five key moments
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(
                f"<p style='margin-bottom: 5px;'>{moment}</p>", unsafe_allow_html=True)

    # User Input box
    st.sidebar.subheader("Add and Process New Podcast Feed")
    url = st.sidebar.text_input("Link to RSS Feed")

    process_button = st.sidebar.button("Process Podcast Feed")
    st.sidebar.markdown("**Note**: Podcast processing can take upto 5 mins, please be patient.")

    if process_button:

        # Call the function to process the URLs and retrieve podcast guest information
        podcast_info = process_podcast_info(url)

        # Right section - Newsletter content
        st.header("Newsletter Content")

        # Display the podcast title
        st.subheader("Episode Title")
        st.write(podcast_info['podcast_details']['episode_title'])

        # Display the podcast summary and the cover image in a side-by-side layout
        col1, col2 = st.columns([7, 3])

        with col1:
            # Display the podcast episode summary
            st.subheader("Podcast Episode Summary")
            st.write(podcast_info['podcast_summary'])

        with col2:
            st.image(podcast_info['podcast_details']['episode_image'], caption="Podcast Cover", width=300, use_column_width=True)

        # Display the podcast guest and their details in a side-by-side layout
        col3, col4 = st.columns([3, 7])

        with col3:
            st.subheader("Podcast Guest")
            st.write(podcast_info['podcast_guest']['name'])

        with col4:
            st.subheader("Podcast Guest Details")
            st.write(podcast_info["podcast_guest"]['summary'])

        # Display the five key moments
        st.subheader("Key Moments")
        key_moments = podcast_info['podcast_highlights']
        for moment in key_moments.split('\n'):
            st.markdown(
                f"<p style='margin-bottom: 5px;'>{moment}</p>", unsafe_allow_html=True)

def create_dict_from_json_files(folder_path):
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    data_dict = {}

    for file_name in json_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            podcast_info = json.load(file)
            podcast_name = podcast_info['podcast_details']['podcast_title']
            # Process the file data as needed
            data_dict[podcast_name] = podcast_info

    return data_dict

def process_podcast_info(url):
    f = modal.Function.lookup("corise-podcast-project-full", "process_podcast")
    output = f.call(url, '/content/Podcast/')
    return output

if __name__ == '__main__':
    main()

streamlit run podcast_frontend(2).py
