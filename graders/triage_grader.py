def grade_action(predicted, correct):
    if predicted == correct:
        score = 0.95
    elif predicted == "high" and correct == "emergency":
        score = 0.5
    elif predicted == "medium" and correct == "high":
        score = 0.5
    else:
        score = 0.05

    
    score = max(0.01, min(score, 0.99))
    return score
