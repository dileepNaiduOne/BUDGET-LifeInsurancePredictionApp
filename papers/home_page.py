import streamlit as st


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([2, 3, 2])

with c2:
    st.title(":gray[Use of] BUDGET :gray[app:]", anchor=False)

    b1 = st.button("Show Pipeline", type="primary")
    if b1:
        st.switch_page("papers/pipe_page.py")


    st.divider()

    st.title(":gray[Predict with:]", anchor=False)
    bs = st.pills("SELECT", ["My Data", "Random Data"], label_visibility="collapsed", selection_mode="single")

    if bs == "My Data":
        st.switch_page("papers/data_page.py")
    elif bs == "Random Data":
        st.switch_page("papers/random_page.py")