import streamlit as st 
import tools
import pandas as pd

st.set_page_config(page_title="Bnak of Maazin", page_icon="🏦")
st.title("Bank of Maazin: Admin Dashboard")

st.sidebar.header("Actions")
option = st.sidebar.selectbox("Choose a tool:",["View All Users","Create New User"])

if option == "View All Users":
    st.subheader("Live Custumer Database")

    if st.button("Refresh Data"):
        with st.spinner("Connecting to Cloud..."):
            data = tools.get_all_users()

            if "user" in data:
                users = data["user"]
                df = pd.DataFrame(users)
                st.dataframe(df,use_container_width=True)
                st.success(f"Found {len(users)} custumers.")
            else:
                st.error("Could not fetch data.")

elif option == "Create New User":
    st.subheader("OnBoard New Custumer")

    new_name = st.text_input("Custumer Name")
    new_balance = st.number_input("Opening Balance", min_value=0.0, step=100.0)

    if st.button("Create Account"):
        if new_name:
            with st.spinner("Talking to Bank API..."):
                result = tools.create_user_tool(new_name, new_balance)
                st.success(f"Response: {result}")
        else:
            st.warning("Please enter a name.")         
            