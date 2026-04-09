def grade_action(predicted, correct):
    if predicted == correct:
        score = 0.95
    elif predicted == "high" and correct == "emergency":
        score = 0.5
    elif predicted == "medium" and correct == "high":
        score = 0.5
    else:
        score = 0.05

    # clamp
    score = max(0.01, min(score, 0.99))
    return score



def grade_episode(actions, correct_actions):
    scores = []

    for pred, corr in zip(actions, correct_actions):
        scores.append(grade_action(pred, corr))

    if not scores:
        return 0.1

    final_score = sum(scores) / len(scores)

    
    final_score = max(0.01, min(final_score, 0.99))

    return final_score
