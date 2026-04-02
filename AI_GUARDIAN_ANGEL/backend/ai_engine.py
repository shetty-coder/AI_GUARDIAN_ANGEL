def generate_suggestion(score):

    if score < 50:
        return "🚨 Emergency risk detected! Please contact caregiver immediately."

    elif score > 85:
        return "Great! Keep maintaining your healthy routine."

    elif score > 65:
        return "Good, but try to improve activity and hydration."

    else:
        return "Low independence detected. Stay active and monitor health."