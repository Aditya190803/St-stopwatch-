import streamlit as st
import time

def main():
    st.title("Stopwatch App")
    
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    if 'elapsed_time' not in st.session_state:
        st.session_state.elapsed_time = 0.0
    if 'running' not in st.session_state:
        st.session_state.running = False
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Start"):
            if not st.session_state.running:
                st.session_state.start_time = time.time() - st.session_state.elapsed_time
                st.session_state.running = True
    
    with col2:
        if st.button("Stop"):
            if st.session_state.running:
                st.session_state.elapsed_time = time.time() - st.session_state.start_time
                st.session_state.running = False
    
    with col3:
        if st.button("Reset"):
            st.session_state.start_time = None
            st.session_state.elapsed_time = 0.0
            st.session_state.running = False
    
    if st.session_state.running:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
    
    st.subheader(f"Elapsed Time: {st.session_state.elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
