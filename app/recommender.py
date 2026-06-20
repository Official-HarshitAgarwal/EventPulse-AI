def generate_recommendation(event: dict, predicted_priority: str):

    impact_score = 0

    # ==========================
    # Impact Score Calculation
    # ==========================

    if predicted_priority == "High":
        impact_score += 40

    if event["requires_road_closure"]:
        impact_score += 25

    if event["is_peak_hour"]:
        impact_score += 20

    if event["event_type"] == "unplanned":
        impact_score += 10

    if event["event_category"] in ["Infrastructure", "Natural"]:
        impact_score += 5

    if event["is_weekend"]:
        impact_score -= 5

    impact_score = max(0, min(impact_score, 100))

    # ==========================
    # Impact Level
    # ==========================

    if impact_score >= 70:

        impact_level = "High"

        officers = 8
        barricades = 6
        diversion = True

        actions = [
            "Deploy traffic police immediately.",
            "Dispatch emergency response vehicle.",
            "Install temporary barricades.",
            "Activate traffic diversion routes.",
            "Send live traffic alerts to commuters.",
            "Monitor congestion continuously.",
            "Coordinate with nearby police station."
        ]

    elif impact_score >= 40:

        impact_level = "Medium"

        officers = 4
        barricades = 4
        diversion = False

        actions = [
            "Deploy traffic response team.",
            "Monitor vehicle movement.",
            "Place warning barricades.",
            "Keep emergency vehicle on standby.",
            "Inform nearby traffic control room."
        ]

    else:

        impact_level = "Low"

        officers = 2
        barricades = 2
        diversion = False

        actions = [
            "Monitor the incident.",
            "Minimal traffic intervention required.",
            "Clear the incident after inspection."
        ]

    # ==========================
    # Estimated Clearance Time
    # ==========================

    if impact_level == "High":
        clearance_time = "45-60 Minutes"

    elif impact_level == "Medium":
        clearance_time = "20-30 Minutes"

    else:
        clearance_time = "10-15 Minutes"

    # ==========================
    # Emergency Status
    # ==========================

    if predicted_priority == "High":
        emergency = "Immediate Response Required"

    elif impact_level == "Medium":
        emergency = "Response Recommended"

    else:
        emergency = "Monitor Situation"

    # ==========================
    # Return Recommendation
    # ==========================

    return {
        "impact_score": impact_score,
        "impact_level": impact_level,
        "officers_required": officers,
        "barricades_required": barricades,
        "diversion_required": diversion,
        "estimated_clearance_time": clearance_time,
        "emergency_status": emergency,
        "actions": actions
    }