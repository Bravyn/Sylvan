import streamlit as st
from maze import maze

def what_is_a_neurotransmitter():
    st.subheader(":blue[NEURO]*DASH*")
    st.info("""A neurotransmitter is a **chemical messanger**
    that transmits signals between neurons(nerve cells)
    in the brain and throughtout the nervous system. """)
    with st.expander("Read about Neuro Transmitters"):
        st.info("""
        Imagine your brain as a bustling city with millions of tiny messengers running around, carrying important information from one place to another. These messengers are called neurotransmitters, and they have a vital job in making sure that different parts of your brain and nervous system can communicate effectively.

Neurotransmitters are like chemical signals that help neurons (nerve cells) talk to each other. They act as messengers, relaying information from one neuron to the next. It's like passing notes in a classroom, but instead of paper, they use special chemicals to send their messages.

When a neuron wants to send a signal, it releases neurotransmitters into the small gaps between neurons called synapses. These neurotransmitters then travel across the synapse and attach themselves to receptors on the receiving neuron, kind of like a key fitting into a lock. Once attached, they deliver their message to the receiving neuron.

The receiving neuron receives these messages and decides what to do next based on the information it received. It may continue passing the signal to other neurons, or it may trigger a response in the body, like moving a muscle or releasing hormones.

Think of neurotransmitters as the communication superheroes of your brain. They help coordinate your thoughts, emotions, movements, and all the things that make you, well, you! Without neurotransmitters, the different parts of your brain wouldn't be able to work together and communicate effectively.

So, next time you're amazed by your brain's incredible abilities, remember to give a shout-out to these little chemical messengers, the neurotransmitters, who make it all possible!
        """)
    st.caption("""These chemical substances 
    play a crucial role in facilatating 
    communication and information transfer between 
    nerve cells.""")

def how_do_they_work():
    st.info("""When an electrical signal, called an
            *action potential* reaches the end of 
             of a neuron, it triggers the release of 
              neurotransmitter from specialized structures called 
               synaptic vesicles.""")

def nates_calling():
    st.header("GAME ON")
    st.write("Hello, my name is **Neuron Nate**.")
    name = st.text_input("May I know your name please...")
    st.caption("Your name isn't saved across game sessions.")
    if name:
        st.info(f"""
        Okay **{name.capitalize()}**, 
        help the main character, Neuron Nate, 
        navigate through the brain and collect 
        neurotransmitters while avoiding obstacles
        and challenges.

        """)
        if st.button("Yes, I'm In!"):
            st.info(maze)


what_is_a_neurotransmitter()
how_do_they_work()
nates_calling()

