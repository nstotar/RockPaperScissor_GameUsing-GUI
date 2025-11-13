import streamlit as st
import random

st.title("Rock Paper Scissors - Best of Three")

if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.rounds_played = 0
    st.session_state.result = ""

def play(choice):
    if st.session_state.rounds_played >= 3:
        return

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        st.session_state.player_score += 1
    else:
        result = "You lose!"
        st.session_state.computer_score += 1

    st.session_state.result = f"Player: {choice} | Computer: {computer_choice}\n{result}"
    st.session_state.rounds_played += 1

    if st.session_state.rounds_played == 3:
        if st.session_state.player_score > st.session_state.computer_score:
            winner = "Player"
        elif st.session_state.computer_score > st.session_state.player_score:
            winner = "Computer"
        else:
            winner = "It's a tie!"
        st.success(f"Game Over! Winner: {winner}")

st.write(f"Player: {st.session_state.player_score} | Computer: {st.session_state.computer_score}")
st.write(st.session_state.result)

if st.session_state.rounds_played < 3:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Rock"):
            play("Rock")
    with col2:
        if st.button("Paper"):
            play("Paper")
    with col3:
        if st.button("Scissors"):
            play("Scissors")

if st.button("Reset Game"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.rounds_played = 0
    st.session_state.result = ""
