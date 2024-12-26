import streamlit as st


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([2, 3, 2])

with c2:
    # st.title(":gray[Use of] BUDGET :gray[app:]", anchor=False)
    st.write('''
                <p style=color:#BFBEBA>  
                    Ever wondered how life insurance premiums are calculated? 
                </p> 
                <p style=color:#BFBEBA> 
                    <strong style=color:#f3626f> BUDGET </strong> is a web app that lets you explore just that, using the power of machine learning. 
                    You can see how different factors might impact your potential costs by trying out your own data, or by generating random 
                    scenarios—like a fun 'what if' game with real-world numbers. 
                </p>
                <p style=color:#BFBEBA> 
                    I'm building this app to be both insightful and transparent, letting you peek at the data processing 'pipeline' behind the scenes. 
                    While still in development, <strong style=color:#f3626f> BUDGET </strong> isn't just about spitting out a number; it's about empowering you to understand the often-complex world of insurance. 
                    Think of it as your personal data-driven exploration tool for life insurance, making a seemingly daunting topic surprisingly accessible and engaging.
                </p>
             '''
             , unsafe_allow_html=True)

    b1 = st.button("Show Pipeline", type="primary")
    if b1:
        st.switch_page("papers/pipe_page.py")


    st.divider()

    st.title(":gray[Predict with:]", anchor=False)

    cc1, cc2, cc3 = st.columns([2, 3, 5])

    with cc1:
        b2 = st.button("My Data", type="primary")
        if b2:
            st.switch_page("papers/data_page.py")

    with cc2:
        b3 = st.button("Random Data", type="primary")
        if b3:
            st.switch_page("papers/random_page.py")