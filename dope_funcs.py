import streamlit as st

def dopamine_functions():

    st.caption("Dopamine main functions")
 
    options = ["Reward and Pleasure", "Motivation and Drive", 
                                  "Movement Control", "Learning and Memory",
                                  "Executive Functions", "Mood Regulation"]
    
    
    
    t1, t2, t3 = st.tabs(options[:3])
    with t1:
        st.info("""Dopamine is closely linked to the brain's reward system. 
        It is released when we engage in pleasurable activities or receive rewarding stimuli, 
        reinforcing those behaviors and creating a sense of pleasure.""")
    with t2:
        st.info(
        """Dopamine plays a crucial role in motivation and goal-directed behavior.
          It helps to provide the drive and energy needed to pursue rewards and achieve goals. 
          Insufficient dopamine levels can lead to a lack of motivation and difficulty in initiating or sustaining activities"""
        )
    with t3:
        st.info("""
        Dopamine is involved in the regulation of movement.
          It helps coordinate and fine-tune motor functions, allowing smooth and coordinated movements. 
          The loss of dopamine-producing cells in the substantia nigra leads to motor symptoms characteristic of Parkinson's disease."
        """
        )
    t4, t5, t6 = st.tabs(options[3:])
    with t4:
        st.info("""
        Dopamine plays a role in learning and memory processes. It aids in the consolidation of memories and facilitates the formation of associations between actions, behaviors, and outcomes. This contributes to the reinforcement of learned behaviors.
        """
        )
    with t5:
        st.info("""
Dopamine is involved in executive functions such as attention, cognitive control, and decision-making. It helps to regulate and optimize cognitive processes, allowing for flexible thinking, problem-solving, and making choices based on potential rewards and outcomes.        """
        )
    with t6:
        st.info("""
 Dopamine influences mood and emotional well-being. Imbalances in dopamine levels have been associated with various psychiatric disorders, including depression, bipolar disorder, and addiction. Proper dopamine regulation is essential for maintaining stable mood states.        """
        )

   
    st.caption("""It's important to note that dopamine's functions are complex and interconnected with other neurotransmitters and brain systems. Its precise effects can vary depending on the specific brain regions involved and the context in which it is released.""")

    