import streamlit as st
import random

choices={
    "rock":"WhatsApp Image 2026-04-15 at 14.59.15.jpeg",
    "paper":"WhatsApp Image 2026-04-15 at 14.59.14.jpeg",
    "scissor":"WhatsApp Image 2026-04-15 at 14.59.16.jpeg"
}
user_choice=st.selectbox("Choose your option",list(choices.keys()))

if st.button("PLAY"):
    com_choice=random.choice(list(choices.keys()))

    col1,col2,col3=st.columns([1,1,1])
    with col1:
        st.write("MY CHOICE")
        st.image(choices[user_choice])

    with col2:
        st.write("V/S")
    with col3:
        st.write("COM CHOICE")
        st.image(choices[com_choice])

     # Determine the winner
    if user_choice == com_choice:
        st.markdown("### It's a tie! 🤝")
    
    elif (
         (user_choice == "rock" and com_choice == "scissor") or \
         (user_choice == "paper" and com_choice == "rock") or \
         (user_choice == "scissor" and com_choice == "paper")
    ):
        st.markdown("### You win! 🏆")
    
    else:
        st.markdown("### You lose! 😢")