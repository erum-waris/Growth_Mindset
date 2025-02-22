import streamlit as st
import random
import json
import os

# Function to load data from a JSON file
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

# Function to save data to a JSON file
def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)

# Page title and introduction
st.title("🏆 Growth Mindset Challenge🌟")
st.write("Created By ERUM WARIS")


# Sidebar for navigation
st.sidebar.markdown("""
# 🧭 ***Start exploring now!***  
*Where would you like to go today?*  
""")

# Adding a divider for visual appeal
st.sidebar.markdown("---")

# Radio button with emojis and descriptions
page = st.sidebar.radio(
    "Go to", 
    options=[
        "🏠 Home", 
        "🎯 Daily Challenge", 
        "📔 Reflection Journal", 
        "🎯 Goal Setting", 
        "📊 Progress Tracker", 
        "💬 Motivational Quotes"
    ],
    help="Select a page to explore!"
)

# Adding a fun footer to the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("✨ *Your growth journey starts here!* ✨")

# Home Page
if page == "🏠 Home":
    
    st.header("What is a Growth Mindset?")
    st.write("""
  A growth mindset is the belief that **your abilities can grow** through effort, learning, and resilience.  
    It’s about embracing challenges, learning from failures, and valuing progress over perfection.  
    With a growth mindset, every setback becomes a stepping stone to success.  

    """)

# Daily Challenge Page
elif page == "🎯 Daily Challenge":
    st.header("Today's Growth Mindset Challenge")
    challenges = [
        "Try learning something new today, even if it feels difficult.",
        "Reflect on a recent mistake and write down what did you learn from it.",
        "Ask for feedback from a friend or colleague and use it to improve.",
        "Set a small, achievable goal and work towards it today.",
        "Celebrate your effort, not just the outcome."
    ]
    challenge = random.choice(challenges)
    st.write(f"**Your challenge for today:** {challenge}")

# Reflection Journal Page
elif page == "📔 Reflection Journal":
    st.header("Reflection Journal")
    
    # Load reflections
    reflections = load_data("reflections.json")
    
    # Input for new reflection
    reflection = st.text_area("Write about your 🔍 learning experiences today:")
    if st.button("Save Reflection"):
        if reflection.strip():  # Check if the reflection is not empty
            reflections.append({"text": reflection, "id": len(reflections) + 1})
            save_data("reflections.json", reflections)
            st.success("Reflection saved!🌻")
        else:
            st.warning("Please write something before saving.")
    
    # Display and manage existing reflections
    if reflections:
        st.subheader("Your Reflections")
        for idx, ref in enumerate(reflections):
            st.write(f"{idx + 1}. {ref['text']}")
            if st.button(f"Delete Reflection {idx + 1}"):
                del reflections[idx]
                save_data("reflections.json", reflections)
                st.success("Reflection deleted!")
                st.rerun()  # Refresh the page
            if st.button(f"Edit Reflection {idx + 1}"):
                edited_reflection = st.text_area(f"Edit Reflection {idx + 1}", value=ref['text'])
                if st.button(f"Save Edited Reflection {idx + 1}"):
                    if edited_reflection.strip():  # Check if the edited reflection is not empty
                        reflections[idx]['text'] = edited_reflection
                        save_data("reflections.json", reflections)
                        st.success("Reflection updated!")
                        st.rerun()  # Refresh the page
                    else:
                        st.warning("Please write something before saving.")

# Goal Setting Page
elif page == "🎯 Goal Setting":
    st.header("Set Your Goals")
    
    # Load goals
    goals = load_data("goals.json")
    
    # Input for new goal
    goal = st.text_input("What is your goal?")
    timeline = st.selectbox("Timeline", ["Short-term", "Long-term"])
    if st.button("Save Goal"):
        if goal.strip():  # Check if the goal is not empty
            goals.append({"goal": goal, "timeline": timeline, "id": len(goals) + 1})
            save_data("goals.json", goals)
            st.success("Goal saved! 🌻")
        else:
            st.warning("Please enter a goal before saving.")
    
    # Display and manage existing goals
    if goals:
        st.subheader("🎯 Goal Setting")
        for idx, g in enumerate(goals):
            st.write(f"{idx + 1}. {g['goal']} ({g['timeline']})")
            if st.button(f"Delete Goal {idx + 1}"):
                del goals[idx]
                save_data("goals.json", goals)
                st.success("Goal deleted!")
                st.rerun()  # Refresh the page
            if st.button(f"Edit Goal {idx + 1}"):
                edited_goal = st.text_input(f"Edit Goal {idx + 1}", value=g['goal'])
                edited_timeline = st.selectbox(f"Edit Timeline for Goal {idx + 1}", ["Short-term", "Long-term"], index=0 if g['timeline'] == "Short-term" else 1)
                if st.button(f"Save Edited Goal {idx + 1}"):
                    if edited_goal.strip():  # Check if the edited goal is not empty
                        goals[idx]['goal'] = edited_goal
                        goals[idx]['timeline'] = edited_timeline
                        save_data("goals.json", goals)
                        st.success("Goal updated!")
                        st.rerun()  # Refresh the page
                    else:
                        st.warning("Please enter a goal before saving.")

# Progress Tracker Page
elif page == "📊 Progress Tracker":
    st.header("Track Your Progress")
    st.write("Coming soon! This feature will allow you to visualize your progress over time.")

# Motivational Quotes Page
elif page == "💬 Motivational Quotes":
    st.header("💡 Motivational Quotes 💡")
    
    # Define the quotes as a list of strings
    quotes = [
        "1. Fear ALLAH ALMIGHTY and you will have no cause to fear any one. (Hazrat Ali (R.A))",
        "2. Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
        "3. Success is not an accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing. – Pelé",
        "4. Coding like poetry should be short and concise. ― Santosh Kalwar",
        "5. Code is like humor. When you have to explain it, it’s bad. – Cory House"
    ]
    
    # Loop through the quotes and display them one by one
    for quote in quotes:
        st.write(f"**{quote}**")