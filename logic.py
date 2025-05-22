from openai import OpenAI
import os
from dotenv import load_dotenv
from supplement_data import supplements, get_supplements_for_goal
import streamlit as st

load_dotenv()
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

def get_recommendation(user_profile):
    """
    Generate personalized supplement recommendations based on user profile
    """
    name = user_profile["name"]
    age = user_profile["age"]
    gender = user_profile["gender"]
    health_goal = user_profile["health_goal"]

    # relevant supplements for the health goal
    relevant_supplements = get_supplements_for_goal(health_goal)

    if not relevant_supplements:
        return f"Sorry {name}, I couldn't find suitable supplements for that specific goal. Please try selecting a different health goal."

    # prompt
    prompt = f"""
    You are a knowledgeable supplement advisor. Please provide personalized supplement recommendations for:

    **User Profile:**
    - Name: {name}
    - Age Group: {age}
    - Gender: {gender}
    - Health Goal: {health_goal}

    **Available Supplements:**
    """

    for supplement in relevant_supplements:
        prompt += f"- **{supplement['name']}**: {supplement['description']}\n"
        prompt += f"  - Benefits: {supplement['benefits']}\n"
        prompt += f"  - Dosage: {supplement['dosage']}\n"
        prompt += f"  - Best for: {supplement['target_demographic']}\n\n"

    prompt += f"""
    **Instructions:**
    1. Recommend exactly 3 supplements that would be most beneficial for {name}'s profile
    2. Consider their age group ({age}) and gender ({gender}) when making recommendations
    3. Ensure the supplements work well together (check for compatibility)
    4. Provide specific reasons why each supplement is suitable for their profile
    5. Include any age or gender-specific considerations
    6. Format your response in a clear, organized manner with:
       - A personalized greeting using their name
       - Each supplement recommendation with explanation
       - Compatibility notes
       - Any relevant warnings or considerations

    **Important:** Focus on supplements that are specifically beneficial for their demographic and health goal.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Sorry {name}, I encountered an error while generating your recommendations. Please try again later. Error: {str(e)}"

def check_supplement_compatibility(supplements_list):
    """
    Check if the recommended supplements are compatible with each other
    """

    compatibility_notes = []

    supplement_names = [supp.lower() for supp in supplements_list]

    # compatibility checks
    if 'caffeine' in ' '.join(supplement_names) and 'magnesium' in ' '.join(supplement_names):
        compatibility_notes.append("Take caffeine and magnesium at different times of day for optimal absorption.")

    if 'iron' in ' '.join(supplement_names) and 'calcium' in ' '.join(supplement_names):
        compatibility_notes.append("Iron and calcium should be taken separately as they can interfere with each other's absorption.")

    return compatibility_notes


def get_followup_response(user_question, chat_history, user_profile):
    """
    Generate brief responses to follow-up questions using chat history context
    """
    # Extract previous recommendations from chat history
    previous_context = ""
    for msg in chat_history:
        if msg["role"] == "assistant" and msg.get("type") == "recommendation":
            previous_context = msg["content"]
            break

    # context-aware prompt
    prompt = f"""
    You are a supplement advisor. A user named {user_profile.get('name', 'User')} 
    (Age: {user_profile.get('age', 'N/A')}, Gender: {user_profile.get('gender', 'N/A')}, 
    Goal: {user_profile.get('health_goal', 'N/A')}) has a follow-up question about their supplement recommendations.

    **Previous Recommendation:**
    {previous_context}

    **User's Follow-up Question:**
    {user_question}

    **Instructions:**
    - Provide a brief, helpful response (2-3 sentences max)
    - Reference their previous recommendations when relevant
    - Keep it conversational and personalized using their name
    - If the question is unrelated to supplements, politely redirect to supplement topics
    - Be concise but informative
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200  # Keep responses brief
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Sorry, I encountered an error answering your question. Please try again."