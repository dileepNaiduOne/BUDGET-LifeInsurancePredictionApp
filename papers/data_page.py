import streamlit as st


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

c1, c2, c3 = st.columns([2, 3, 2])

inputs = []

with c2:
    st.title(":gray[Prediction Form]", anchor=False)
    st.caption(":red[*] Providing correct information will ensure precise predictions")

    st.divider()

    with st.form("prediction_form", enter_to_submit=False, border=False):
        # Age
        age = st.number_input(":red[Age]", min_value=0, max_value=100)
        
        # Gender
        gender = st.segmented_control(":red[Gender]", options=["Male - :material/male:", "Female - :material/female:"], selection_mode="single")

        # Education Level
        edu = st.segmented_control(label=":red[Education Level]", options=["Bachelor's", "Master's", "High School", "PhD"], selection_mode="single",)

        # Occupation
        occupation = st.segmented_control(label=":red[Occupation]", options=['Self-Employed', 'Employed', 'Unemployed'], selection_mode="single")

        # Marital Status
        marry = st.segmented_control(":red[Marital Status]", options=['Single - :material/man_4:', 'Married - :material/wc:', 'Divorced - :material/taunt:'], selection_mode="single")

        # Location
        location = st.segmented_control(":red[Location]", options=['Rural', 'Suburban', 'Urban'], selection_mode="single")

        # Property Type
        property_type = st.segmented_control(":red[Property Type]", options=['House', 'Apartment', 'Condo'], selection_mode="single")

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------

        # Smoking Status
        smoking_status = st.radio(label=":red[Smoking Status]", options=["Yes", "No"], horizontal=True, index=None)

        # Exercise Frequency
        exercise_frequency = st.segmented_control(":red[Exercise Frequency]", options=['Weekly', 'Monthly', 'Daily', 'Rarely'], selection_mode="single")

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------

        # Annual Income
        income = st.number_input(":red[Annual Income (₹)]", format="%.2f")
        
        # Number of Dependents
        dependents = st.radio(":red[No. of Dependents]", options=[0, 1, 2, 3, 4], horizontal=True, index=None)

        # Health Score
        health = st.number_input(":red[Health Score]")

        # Credit Score
        credit = st.number_input(":red[Credit Score]")

        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------


        # Policy Start Date
        policy_start_date = st.date_input(":red[Policy Start Date]", format="DD/MM/YYYY")

        # Policy Type
        policy = st.segmented_control(":red[Policy Type]", options=['Basic', 'Comprehensive', 'Premium'], selection_mode="single")

        # Insurance Duration
        insurance_duration = st.number_input(":red[Insurance Duration]", min_value=0, max_value=10)

        # Previous Claims
        previous_claims = st.number_input(":red[Previous Claims]", min_value=0, max_value=10)

        # Vehicle Age
        vehicle_age = st.number_input(":red[Vehicle Age]", min_value=0, max_value=30)

        
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        st.divider()
        # -----------------------------------------------------------------------------------------------------------------------------------------------
        

        # Customer Feedback
        customer_feedback = st.segmented_control(":red[Customer Feedback]", options=['Poor', 'Average', 'Good'], selection_mode="single")
        

        st.divider()


        @st.dialog("PREDICTION", width="large")
        def prediction(inputs):
            st.write(f"# Prediction comes, Here")

        st.write("\n")
        st.write("\n")
        pre = st.form_submit_button(f"# PREDICT", type="primary", icon=":material/currency_rupee:", use_container_width=True)

        if pre:
            prediction(inputs)