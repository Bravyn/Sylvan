import streamlit as st
from neuro import nates_calling, what_is_a_neurotransmitter, how_do_they_work

    
c1, c2 = st.columns(2)

with c1:
    what_is_a_neurotransmitter()
with c2:
    how_do_they_work()
nates_calling()

