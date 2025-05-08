# app.py
import streamlit as st
# Assuming 'src' is in the same directory or Python path is configured
from src.doc_analyzer.analyzer import generate_material, provide_feedback, grade_document

# --- Page Config ---
st.set_page_config(
    page_title="LLM Teacher Tool",
    page_icon="📚",
    layout="wide"
)

# --- Sidebar ---
with st.sidebar:
    st.title("🛠️ Tools")
    # Radio button to select the tool
    tool_option = st.radio(
        "Choose a tool:",
        ("📝 Generate Material", "💬 Provide Feedback", "💯 Grade Document"),
        key="tool_selection" # Add a key for state management
    )
    st.markdown("---")
    st.info("Final Project Demo")

# --- Main Page ---
st.title("📚 LLM Teacher Tool")
st.write("> AI-powered assistance for educators")

# --- Tool Interfaces ---

# Initialize session state keys if they don't exist
if 'feedback_result' not in st.session_state:
    st.session_state['feedback_result'] = ""
if 'grading_result' not in st.session_state:
    st.session_state['grading_result'] = ""

# == Generate Material Tool ==
if tool_option == "📝 Generate Material":
    st.header("📝 Generate Teaching Material")
    
    col1, col2 = st.columns([2, 1]) # Layout columns

    with col1:
        # Input for topic
        topic = st.text_input("Enter the topic:", placeholder="e.g., Photosynthesis", key="gen_topic")
    with col2:
        # Selection for length
        length_options = ["brief", "medium", "detailed"]
        length = st.selectbox("Select desired length:", length_options, index=0, key="gen_length")

    # Button to trigger generation
    if st.button("✨ Generate Now!", key="gen_button"):
        if topic: # Check for input
            # Show spinner during generation
            with st.spinner("🧠 Generating material..."):
                # Call backend function
                generated_text = generate_material(topic=topic, length=length)
                st.subheader("Generated Material:")
                # Display result in an expander
                with st.expander("View Generated Material", expanded=True):
                    st.markdown(generated_text)
                st.success("Generation complete!")
        else:
            # Show warning if no topic entered
            st.warning("⚠️ Please enter a topic.")

# == Provide Feedback Tool ==
# In app.py
elif tool_option == "💬 Provide Feedback":
    st.header("💬 Provide Feedback on Document")
    
    col1_fb, col2_fb = st.columns(2)

    with col1_fb:
        st.subheader("Upload Document")
        # File uploader allows txt files
        uploaded_file_fb = st.file_uploader(
            "Choose a text file (.txt):", 
            type=['txt'], 
            key="fb_uploader"
        )
        
        doc_text_feedback = "" # Initialize variable
        if uploaded_file_fb is not None:
            # Read the content of the uploaded file
            try:
                # Read as bytes first, then decode assuming UTF-8
                bytes_data = uploaded_file_fb.getvalue()
                doc_text_feedback = bytes_data.decode("utf-8")
                # Display a preview (optional)
                st.text_area(
                    "File Content Preview (first 500 chars):", 
                    doc_text_feedback[:500] + ("..." if len(doc_text_feedback) > 500 else ""), 
                    height=150,
                    disabled=True # Make preview read-only
                )
            except UnicodeDecodeError:
                st.error("Error: Could not decode the file. Please ensure it is a valid UTF-8 text file.")
                doc_text_feedback = "" # Reset on error
            except Exception as e:
                st.error(f"Error reading file: {e}")
                doc_text_feedback = "" # Reset on error

        # Button to trigger feedback
        if st.button("🔍 Get Feedback", key="fb_button"):
            if doc_text_feedback: # Check if text was successfully read
                with st.spinner("🤔 Analyzing and generating feedback..."):
                    feedback_text = provide_feedback(document_text=doc_text_feedback)
                    st.session_state['feedback_result'] = feedback_text
                    st.success("Feedback generated!")
            elif uploaded_file_fb is None:
                 st.warning("⚠️ Please upload a document file.")
                 st.session_state['feedback_result'] = "" # Clear result
            # If file was uploaded but reading failed, error shown above

    with col2_fb:
        st.subheader("Generated Feedback")
        if st.session_state.get('feedback_result'): # Use .get for safer access
            with st.expander("View Feedback", expanded=True):
                st.markdown(st.session_state['feedback_result'])
        else:
            st.info("Feedback will appear here.")

# == Grade Document Tool ==
# In app.py
elif tool_option == "💯 Grade Document":
    st.header("💯 Grade Document")

    col1_gr, col2_gr = st.columns(2)

    with col1_gr:
        st.subheader("Upload Document & Enter Criteria")
        # File uploader for the document
        uploaded_file_gr = st.file_uploader(
            "Choose a text file (.txt):", 
            type=['txt'], 
            key="gr_uploader"
        )
        
        doc_text_grade = "" # Initialize variable
        if uploaded_file_gr is not None:
            # Read the content of the uploaded file
            try:
                bytes_data = uploaded_file_gr.getvalue()
                doc_text_grade = bytes_data.decode("utf-8")
                # Display preview
                st.text_area(
                    "File Content Preview (first 500 chars):", 
                    doc_text_grade[:500] + ("..." if len(doc_text_grade) > 500 else ""), 
                    height=100,
                    disabled=True
                )
            except UnicodeDecodeError:
                st.error("Error: Could not decode the file. Please ensure it is a valid UTF-8 text file.")
                doc_text_grade = ""
            except Exception as e:
                st.error(f"Error reading file: {e}")
                doc_text_grade = ""

        # Text area for criteria
        criteria = st.text_area(
            "Enter grading criteria/rubric:", height=100,
            placeholder="e.g., Clarity (5pts), Grammar (3pts)...", key="gr_criteria"
        )

        # Button to trigger grading
        if st.button("📊 Grade Now!", key="gr_button"):
            if doc_text_grade and criteria: # Check for both inputs
                with st.spinner("⚖️ Analyzing and grading..."):
                    grading_result = grade_document(document_text=doc_text_grade, criteria=criteria)
                    st.session_state['grading_result'] = grading_result
                    st.success("Grading complete!")
            elif uploaded_file_gr is None:
                 st.warning("⚠️ Please upload a document file.")
                 st.session_state['grading_result'] = "" # Clear result
            elif not criteria:
                 st.warning("⚠️ Please enter grading criteria.")
                 st.session_state['grading_result'] = "" # Clear result
            # If file uploaded but reading failed, error shown above

    with col2_gr:
        st.subheader("Grading Result")
        if st.session_state.get('grading_result'): # Use .get
             with st.expander("View Grading Result", expanded=True):
                st.markdown(st.session_state['grading_result'])
        else:
            st.info("Grading result will appear here.")