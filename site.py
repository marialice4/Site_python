import streamlit as st
st.title(":rainbow[Personalidades]")
st.caption("***Por Mary e Mih***")
tab1, tab2, tab3, tab4 = st.tabs([":red[Anna]", ":orange[Mih]", ":green[Mary]", ":blue[Ka]"])

with tab1:
    st.header(":red[Anna]")
    st.image("https://images6.alphacoders.com/581/thumb-1920-581083.jpg", width=300)
    st.image("https://static.vecteezy.com/system/resources/previews/013/735/149/original/keyboard-piano-music-cartoon-icon-illustration-music-instrument-icon-concept-isolated-premium-flat-cartoon-style-vector.jpg", width=300)
with tab2:
    st.header(":orange[Mih]")
    st.image("https://th.bing.com/th/id/OIP.U8FVhbLLOuyZ-DC-7x47_wHaEo?rs=1&pid=ImgDetMain", width=300)
    st.image("https://imagensemoldes.com.br/wp-content/uploads/2020/09/Desenho-Livros-PNG.png", width=300)

with tab3:
    st.header(":green[Mary]")
    st.image("https://todaatual.com/wp-content/uploads/2014/03/imagens-de-coelho-fofo-1024x768.jpg", width=300)
    st.image("https://th.bing.com/th/id/OIP._3v_FEAgw49izPvK12C1WAHaFa?w=820&h=600&rs=1&pid=ImgDetMain", width=300)
with tab4:
    st.header(":blue[Ka]")
    st.image("https://th.bing.com/th/id/OIP.nr1DkYH2hxZ1il5tB-s1ugHaE8?rs=1&pid=ImgDetMain", width=300)
    st.image("https://th.bing.com/th/id/OIP.wZvoy6DsM16r9D-0n1pg7wAAAA?rs=1&pid=ImgDetMain", width=300)