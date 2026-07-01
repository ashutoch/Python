
#! Streamlit is an open-source Python framework for data scientists and AI?ML engineers to deliver dynamic data apps with only a few lines of code. Build and deply powerful data apps in minutes



#? Study Break Timer with an Alarm Project

import streamlit as st
import time
import winsound

def beep(frequency = 1000, duration = 500):
    winsound.Beep(frequency, duration)


def countdown(t, phase):
    placeholder = st.empty()
    while t:
        mins, secs = divmod(t, 60)   # divides the minutes into seconds
        
        timer = f"{mins :02d} : {secs :02d}"
        placeholder.markdown(f"### {phase}⏱️ : {timer}")        # markdown constantly keeps updating the timer
        
        if t == 10:
            beep(600, 1000)
        
        time.sleep(1)
        t -= 1
    
    placeholder.markdown(f"## {phase} Over! ")
    beep(800, 1500)


def run_timer(study_time, break_time, cycles):
    for cycle in range(1, cycles + 1):
        st.success(f"Cycle {cycle}: Study for {study_time} minutes")
        countdown(study_time * 60, "Study")
        
        st.warning("Study for a cycle has finished! Take a well deserved break")
        countdown(break_time * 60, "Break Time")
        
        st.info(f"Break finished!! Back to studying")
        
        st.balloons()
        st.success("All cycles are completed! Great work boi")



st.title("📚Pomodoro Timer")
study_time = st.number_input("Enter your study time (in minutes): ", min_value = 1, step = 1, value = 30)
break_time = st.number_input("Enter your break time (in minutes): ", min_value = 1, step = 1, value = 5)
cycles = st.number_input("Enter the number of cycles: ", min_value = 1, step = 1, value = 2)

if st.button("Start the Timer"):
    run_timer(study_time, break_time, cycles)