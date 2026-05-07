def simple_evaluator(answer, context):
    score = 0
    
    if len(answer) > 50:
        score += 1
    if "not found" not in answer.lower():
        score += 1

    return {
        "score": score,
        "feedback": "Good" if score == 2 else "Needs Improvement"
    }