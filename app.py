import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(mov):
    mov_index = movies[movies['title']==mov].index[0]
    distances = similarity[mov_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies =[]
    recommended_movie_posters = []
    
    for i in movies_list:
        recommended_movies.append(movies['title'][i[0]])
        recommended_movie_posters.append(fetch_poster(movies['movie_id'][i[0]]))
    
    return recommended_movies, recommended_movie_posters


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=df7879a285a6ec7197f93149e9eb97bb&language=en-US'.format(movie_id))
    data = response.json()
    
    return "https://image.tmdb.org/t/p/original"+data['poster_path']

    


st.title('Movie Recommender System')

option = st.selectbox(
     'Enter the Movie Name',
     (movies_list))

if st.button('Recommend'):
    names, posters = recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
       st.text(names[2])
       st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])