def grade_action(predicted, correct):
    if predicted == correct:
        return 1.0
    elif predicted == "high" and correct == "emergency":
        return 0.5
    elif predicted == "medium" and correct == "high":
        return 0.5
    else:
        return 0.0