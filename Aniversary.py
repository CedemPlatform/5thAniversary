from numpy import complex128
import streamlit as st


st.sidebar.title('Ai Shite Van San')
st.sidebar.image('images/us.jpeg')

st.title('Nuestro Quinto Aniversario Van San')
st.image('images/mainmenu.jpg')

col1, col2 = st.columns(2)

a = 'Mi razón de existir'
b = 'Lo que siempre pienso'
c = 'Tu eres'
d = 'Siempre te'
e = 'Mi premio por que me aguantas'

menu = col1.radio('Menú de Carta Aniversario', (a, b, c, d, e))

if menu == a:
    col2.image('images/mimp.jpeg')
    st.subheader('No sólo eres la Mujer de mi vida, Eres Mi Vida!')
    st.write('Cada que te veo, tu forma de ser, tu forma de pelearme, de amarme de exigirme, de cuidarme, tu forma de querer que te chiquee, tu forma de comer, todo me encanta, te veo y sé que eres la mujer de mi vida, mi mujer perfecta, mi Persona Favorita.')

elif menu == b:
    col2.image('images/atuspies.jpg')
    st.subheader('Me tienes a tus Pies')
    st.write('No soy bueno expresandome, siempre fui hermético y tal vez bromeo con la vida para no mostrar todo lo que pueda sentir o pensar.')
    st.write('Pero hay algo que debes saber y es en primer lugar que te amo, que mi esfuerzo extremo es por ti y para poder ofrecerte todo lo que quieras en tu vida, quiero disfrutar mi vida contigo, quiero entregarte mi vida, por eso trabajo tanto.')
    st.write('En mi mente siempre estás tu en todos los ámbitos, en lo cachondo muero por siempre besar tus pies, los tienes hermosos y toda tu eres hermosa, eres mi Fetish Completo, siempre Estoy a tus Pies.')
elif menu == c:
    col2.image('images/eresmilady.jpg')
    col1.subheader('Eres Milady')
    col1.write('Milady, la mujer más hermosa que han visto y verán mis ojos')

elif menu == d:
    col2.image('images/teprote.jpeg')
    st.subheader('Siempre voy a protegerte, Soy tu Escudo')
    st.write('Quiero pasar toda mi vida a tu lado, cuidandote, mimándote, protegiendote.')

elif menu == e:
    col2.image('images/achievementunlock.png')
    col1.subheader('Mi mayor logro y mayor regalos Eres tu y que sigas a mi lado a pesar de mis defectos')
    st.subheader('Gracias por Estar a mi lado siempre.')
    if st.button('Secret Message'):
        st.title('Te Amo con toda mi Alma mi Reina Hermosa')
        st.subheader('Feliz Quinto Aniversario!!')
        st.image('images/besos.jpeg')