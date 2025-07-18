import streamlit as st
from explainer import explain_code

# Set up the Streamlit page
st.set_page_config(page_title="Jac Code Explainer", layout="wide")
st.title("Jac Code Explainer")
st.write("Enter a snippet of Jac code, and an LLM will explain it to you.")

# Create a text area for user input
code_input = st.text_area("Enter Jac Code Here:", height=200, value="""
walker code_explainer {
    has code_to_explain: str;
    can explain with `root entry;
}
""")

# Create a button to trigger the explanation
if st.button("Explain Code"):
    if code_input:
        with st.spinner("Generating explanation..."):
            # Call the Jac function to get the explanation
            explanation = explain_code(code_input)
            st.subheader("Explanation:")
            st.markdown(explanation)
    else:
        st.warning("Please enter some code to explain.")
