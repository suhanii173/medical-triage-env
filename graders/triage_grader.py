def grade_action(predicted, correct):
    if predicted == correct:
        score = 0.9
    elif predicted == "high" and correct == "emergency":
        score = 0.6
    elif predicted == "medium" and correct == "high":
        score = 0.6
    else:
        score = 0.2

    return score


# 🔴 THIS FUNCTION IS THE KEY (FINAL SCORE)
def grade_episode(trajectory, info=None):
    """
    trajectory = list of steps
    each step contains action + metadata
    """

    scores = []

    for step in trajectory:
        action = step.get("action", {})
        correct = step.get("info", {}).get("correct")

        predicted = action.get("triage_level")

        # safe fallback
        if correct is None:
            score = 0.2
        else:
            score = grade_action(predicted, "emergency")  # since env uses fixed correct

        scores.append(score)

    if not scores:
        final_score = 0.2
    else:
        final_score = sum(scores) / len(scores)

    # 🔥 CRITICAL HARD CLAMP
    if final_score <= 0:
        final_score = 0.05
    elif final_score >= 1:
        final_score = 0.95

    return final_score
