import os
import streamlit as st
import career_coach_agent
st.set_page_config(layout="wide")

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = st.secrets["HADARSH_GEMINI_API_KEY"]

st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("The Career coach")

st.markdown(
    """<br><br>"""
, unsafe_allow_html=True)

if "candidate_bg" not in st.session_state:
    st.session_state.candidate_bg = None
if "candidate_career_goal" not in st.session_state:
    st.session_state.candidate_career_goal = None
if "show_intro_field" not in st.session_state:
    st.session_state.show_intro_field = True
if "show_goal_field" not in st.session_state:
    st.session_state.show_goal_field = False
if "show_op" not in st.session_state:
    st.session_state.show_op = False
if "show_redo_btn" not in st.session_state:
    st.session_state.show_redo_btn=False


if st.session_state.show_intro_field == True:
    st.session_state.candidate_bg = st.text_area("🤝 Introduce yourself below!", placeholder="Brief about your Education, Work Experience etc.", max_chars=250, height=200)
    intro_btn_clicked = st.button("Submit", key="intro")

    if intro_btn_clicked and len(st.session_state.candidate_bg) > 10:
        st.session_state.show_intro_field = False
        st.session_state.show_goal_field = True
        st.rerun()
if st.session_state.show_goal_field:
    st.session_state.candidate_career_goal = st.text_input("🎯 Tell me your career goal!", placeholder="Data Scientist, Web Developer etc.", max_chars=25)
    goal_btn_clicked = st.button("Submit", key="career_goal")

    if goal_btn_clicked == True and len(st.session_state.candidate_career_goal) > 5:
        st.session_state.show_goal_field = False
        st.session_state.show_op = True
        # st.session_state.show_redo_btn = True
        st.rerun()

def reset():
    st.session_state.clear()
    st.rerun()

if st.session_state.show_op:
    d={"candidate_bg":st.session_state.candidate_bg,"career_goal":st.session_state.candidate_career_goal}
    res = career_coach_agent.app.invoke(d)
    res2={"final_plan" : """Okay, I understand. Given my previous concerns, I'm going to reframe the request. Instead of focusing on "non-existence," I'll create a 6-month timeline for a working professional who wants to deepen their self-awareness, cultivate inner peace, and develop a stronger sense of purpose and connection to the world around them. This will incorporate elements of mindfulness, self-compassion, and values clarification, all while being realistic for someone with a job and other responsibilities.

Overarching Goal: To cultivate a more mindful, compassionate, and purposeful life, leading to increased well-being and resilience.

Timeline Structure: Each month will focus on a specific theme, with suggested activities and resources. The time commitment is designed to be manageable, aiming for approximately 30-60 minutes per day, which can be broken down into smaller chunks.

Month 1: Foundations of Mindfulness and Self-Compassion

Theme: Building a daily mindfulness practice and cultivating self-compassion.
Skills: Basic mindfulness meditation, body scan meditation, loving-kindness meditation, recognizing and challenging self-criticism.
Activities:
Daily Mindfulness Meditation (10-15 minutes): Use apps like Headspace or Calm, or find guided meditations on YouTube (e.g., Tara Brach). Focus on breath awareness or body scan.
Self-Compassion Break (3 times per day): When experiencing difficulty, pause, acknowledge the suffering, remind yourself that suffering is part of the human experience, and offer yourself kindness (e.g., placing a hand on your heart).
Journaling (15 minutes, 3 times per week): Reflect on your experiences with mindfulness and self-compassion. What challenges did you face? What did you learn?
Resources:
"Self-Compassion: The Proven Power of Being Kind to Yourself" by Kristin Neff (Book): Provides a comprehensive guide to self-compassion practices.
UCLA Mindful Awareness Research Center (Website): Offers free guided meditations and resources.
Month 2: Exploring Values and Purpose

Theme: Identifying core values and aligning actions with those values.
Skills: Values clarification exercises, goal setting based on values, identifying obstacles to living in alignment with values.
Activities:
Values Clarification Exercise (1-2 hours, one-time): Use online resources or workbooks to identify your top 5-10 core values (e.g., integrity, creativity, connection, learning).
Values-Based Goal Setting (30 minutes, weekly): Set small, achievable goals that align with your core values.
Values Reflection (15 minutes, 3 times per week): Reflect on how well your actions aligned with your values during the week. Identify areas for improvement.
Resources:
"Living Your Values: A Workbook for Discovering What Matters to You" by Patricia Robinson and Kirk Strosahl (Workbook): Provides practical exercises for values clarification and values-based action.
The Greater Good Science Center (Website): Offers articles and resources on purpose and meaning in life.
Month 3: Cultivating Gratitude and Positive Emotions

Theme: Focusing on the positive aspects of life and cultivating gratitude.
Skills: Gratitude journaling, savoring positive experiences, practicing acts of kindness.
Activities:
Gratitude Journaling (5 minutes, daily): Write down 3-5 things you are grateful for each day.
Savoring Practice (10 minutes, daily): Intentionally focus on and appreciate a positive experience (e.g., a beautiful sunset, a delicious meal, a kind gesture).
Acts of Kindness (1-2 per week): Perform small acts of kindness for others (e.g., helping a neighbor, offering a compliment, donating to a charity).
Resources:
"Thanks!: How Practicing Gratitude Can Make You Happier" by Robert Emmons (Book): Explores the science of gratitude and provides practical tips for cultivating gratitude.
The Gratitude Network (Website): Offers resources and inspiration for practicing gratitude.
Month 4: Managing Stress and Building Resilience

Theme: Developing coping mechanisms for stress and building resilience.
Skills: Stress management techniques (e.g., deep breathing, progressive muscle relaxation), cognitive reframing, building social support.
Activities:
Stress Management Practice (10-15 minutes, daily): Practice deep breathing exercises, progressive muscle relaxation, or other stress management techniques.
Cognitive Reframing (As needed): When experiencing negative thoughts, challenge them and reframe them in a more positive or realistic way.
Social Connection (1-2 times per week): Spend time with loved ones, engage in social activities, or volunteer in your community.
Resources:
"The Resilience Factor: 7 Keys to Finding Your Inner Strength and Overcoming Life's Hurdles" by Karen Reivich and Andrew Shatté (Book): Provides practical strategies for building resilience.
American Psychological Association (Website): Offers information and resources on stress management and resilience.
Month 5: Deepening Self-Awareness and Understanding

Theme: Exploring your inner world and understanding your patterns of thought, feeling, and behavior.
Skills: Shadow work (exploring unconscious aspects of the self), attachment style awareness, understanding personality traits.
Activities:
Journaling (30 minutes, weekly): Explore your thoughts, feelings, and behaviors in more depth. Consider using prompts related to shadow work or attachment styles.
Personality Assessment (One-time): Take a reputable personality assessment (e.g., Myers-Briggs, Enneagram) to gain insights into your personality traits.
Mindful Observation (Throughout the day): Pay attention to your thoughts, feelings, and behaviors in different situations. Notice patterns and triggers.
Resources:
"Meeting the Shadow: The Hidden Power of the Dark Side of Human Nature" edited by Connie Zweig and Jeremiah Abrams (Book): Explores the concept of the shadow self and provides guidance for integrating it.
Attached: The New Science of Adult Attachment and How It Can Help YouFind - and Keep - Love by Amir Levine and Rachel Heller (Book): Explores attachment styles and how they impact relationships.
Month 6: Integration and Continued Growth

Theme: Integrating the practices and insights gained over the past five months and developing a plan for continued growth.
Skills: Reviewing progress, identifying areas for continued development, setting long-term goals.
Activities:
Review and Reflection (1-2 hours): Review your journal entries, notes, and experiences from the past five months. Identify what you have learned and how you have grown.
Goal Setting (30 minutes): Set long-term goals for continued growth in the areas of mindfulness, self-compassion, purpose, and well-being.
Continued Practice (Ongoing): Continue to practice the techniques and strategies that you have found helpful.
Resources:
Revisit previous resources: Continue to use the books, websites, and apps that you have found helpful.
Find a community: Connect with others who are interested in mindfulness, self-compassion, and personal growth.
Important Considerations for a Working Professional:

Flexibility: This is a guideline, not a rigid schedule. Adjust the activities and time commitments to fit your individual needs and circumstances.
Prioritization: Identify the activities that are most important to you and prioritize them.
Small Steps: Start small and gradually increase your commitment over time.
Self-Compassion: Be kind to yourself if you miss a day or don't achieve all of your goals.
Professional Guidance: If you are struggling with difficult emotions or mental health issues, seek help from a qualified therapist or counselor.
This timeline provides a framework for cultivating a more mindful, compassionate, and purposeful life. Remember that personal growth is a journey, not a destination. Be patient with yourself, celebrate your progress, and continue to learn and grow."""}
    st.write(res["final_plan"])
    st.button("Wanna startover? Click me!", on_click=reset)

st.markdown("""
    <style>
    /* Remove default padding */
    .reportview-container .main {
        padding-left: 0rem;
        padding-right: 0rem;
    }

    /* Footer styling */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        #background-color: #f0f2f6;
        #background-color: #2b2b2b;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: grey;
        #background:#000000d9;
        box-shadow: rgba(15,17,23,1) 0px -5px 50px;
        background:rgba(15,17,23,0.9);
    }
    </style>
    <div class="footer">
        <hr style="margin:0px">
        © 2025 Hadarsh Alapaka. All rights reserved. <br>
        Built with ❤️
    </div>
""", unsafe_allow_html=True)