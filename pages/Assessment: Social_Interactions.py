import streamlit as st
import numpy as np

# Initialize session state for storing responses if not already done
if 'responses' not in st.session_state:
    # Prefill all dimensions with a neutral value of 3
    st.session_state.responses = {
        "Identity & Reputation": 3,
        "Presence": 3,
        "Social Interactions": 3,
        "Collaboration": 3,
        "Accessibility": 3,
        "Economy & Transactions": 3,
        "Technology, Structure & Ecosystems": 3,
        "Simulation & Modelling": 3
    }

# Survey questions for "Identity & Reputation"
dimension = "Social Interaction"
subdimensions = {
    "Collaboration": [
        "Our IIP shall enable remote collaboration.",
        "Our IIP could function as a virtual workspace with natural interaction, prompt communication and a high immersion.",
        "The creation of communities and the active participation within them could be benefitial for our use-case.",
        "Enabling stakeholders to collaborate in several ways such as engaging in discussions or analyzing cases from different perspectives is beneficial for our use-case.",
        "Enabling collaborative interactions between users is a goal."
    ],
    "Interactive Environment": [
        "A seamless connectivity between users and users, between users and platforms, between platforms and platforms, and between operating systems and operating systems is beneficial for our use-case.",
        "We want to integrate social elements through interactivity, new interaction modalities with plenty of opportunities for novel social networking and community development in our use-case.",
        "Enabling proactive interactions across the real and virtual world could be beneficial for our use-case.",
        ],
    "Communication": [
        "We want our users to share experiences, give advice, and support others within the IIP.",
        "If our users could remotely check on tasks, and communicate to update each other on task status, it would help our workflow.",
        "We aim to build designated virutal work spaces (such as Meeting Rooms, Collaboration Rooms, Training Rooms, Simulation Rooms, Interview Rooms) for our workers.",
        "We want to enable our users to have the opportunity to observe and actively participate in interactions with other users.",
        "We wish for an additional channel of communication with existing Users, Customers."
    ],
    "Interaction": [
        "we want our users to experience sensory feedback from the stakeholders within the new IIP, such as body language, facial expressions, and eye contact.",
        "We believe that successful interactions and creating an immersive environment can be beneficial for our use-case.",
        "We want to simulating face-to-face interactions within our IIP to enhance our day-to-day interactions.",
        "We want to foster user-user interaction in our use-case."
    ]
}
# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("in this section you should assess your usecase DESCRIBE!!!")
subdimension_scores = []
for subdimension, questions in subdimensions.items():
    st.subheader(subdimension)
    scores = []
    for question in questions:
        score = st.radio(question, ('Strongly Disagree', 'Somewhat Disagree', 'Neutral', 'Somewhat Agree', 'Strongly Agree'), 
                         index=2, key=f"{dimension}-{subdimension}-{question}")
        score_value = {'Strongly Disagree': 1, 'Somewhat Disagree': 2, 'Neutral': 3, 'Somewhat Agree': 4, 'Strongly Agree': 5}
        scores.append(score_value[score])
    
    # Calculate the average score for the subdimension and store in session state
    subdimension_average = np.mean(scores)
    subdimension_scores.append(subdimension_average)

# Calculate the overall score for the dimension by averaging subdimension scores
overall_dimension_score = np.mean(subdimension_scores)
st.session_state.responses[dimension] = overall_dimension_score

# Progress bar calculation (1/8 for the first page)
progress = 7 / 8  # Adjust this number based on the current dimension page
st.progress(progress)

# Navigation
col1, col2 = st.columns([1, 1])

if col1.button("Previous"):
    st.write("Navigate to the previous page in the sidebar.")

if col2.button("Next"):
    st.write("Navigate to the next page in the sidebar.")