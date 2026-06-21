import streamlit as st
import requests
import pandas as pd
import os

# Backend URL: reads from environment variable on Render, falls back to localhost for local dev
backend_url = os.environ.get("https://eventpulse-ai-5iie.onrender.com", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="EventPulse-AI",
    page_icon="🚦",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: 'Segoe UI', sans-serif;
}

.main{
    background-color:#0E1117;
}

.block-container{
    padding-top:1.5rem;
    padding-bottom:2rem;
}

.title{
    font-size:42px;
    font-weight:700;
    color:#00E5FF;
}

.subtitle{
    color:#B0BEC5;
    font-size:18px;
    margin-bottom:10px;
}

.section{
    background:#161B22;
    padding:20px;
    border-radius:15px;
    border:1px solid #30363D;
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:#888;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="title">
🚦 EventPulse-AI
</div>

<div class="subtitle">
Predict. Prepare. Prevent.
</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("📥 Incident Details")

left,right=st.columns(2)

with left:

    latitude=st.number_input(
        "Latitude",
        value=12.9328703
    )

    longitude=st.number_input(
        "Longitude",
        value=77.4879814
    )

    event_type=st.selectbox(
        "Event Type",
        [
            "planned",
            "unplanned"
        ]
    )

    event_cause=st.selectbox(
        "Event Cause",
        [
            "vehicle_breakdown",
            "accident",
            "road_damage",
            "traffic_jam"
        ]
    )

    veh_type=st.selectbox(
        "Vehicle Type",
        [
            "bmtc_bus",
            "car",
            "truck",
            "bike"
        ]
    )

with right:

    police_station=st.selectbox(
        "Police Station",
        [
            "Kengeri",
            "Whitefield",
            "Electronic City",
            "Unknown"
        ]
    )

    zone=st.text_input(
        "Zone",
        value="Unknown"
    )

    junction=st.text_input(
        "Junction",
        value="Unknown"
    )

    corridor=st.selectbox(
        "Corridor",
        [
            "Non-corridor",
            "Corridor"
        ]
    )

    road_closure=st.checkbox(
        "Requires Road Closure"
    )

st.divider()

analyze=st.button(
    "🚀 Analyze Incident",
    use_container_width=True
)

if analyze:

    payload={

        "latitude":latitude,
        "longitude":longitude,

        "event_type":event_type,
        "event_cause":event_cause,

        "authenticated":"yes",
        "veh_type":veh_type,

        "police_station":police_station,
        "zone":zone,
        "junction":junction,
        "corridor":corridor,

        "requires_road_closure":road_closure,

        "hour":7,
        "day_of_week":"Tuesday",
        "month":"January",

        "is_weekend":False,
        "is_peak_hour":True,

        "event_category":"Incident"

    }

    with st.spinner("Analyzing incident..."):

        response=requests.post(
            f"{backend_url}/predict",
            json=payload
        )

    result=response.json()

    rec=result["recommendation"]
    resources=result["resources"]

    st.divider()

    if result["predicted_priority"]=="High":
        st.error("🚨 CRITICAL INCIDENT • Immediate Response Required")
    else:
        st.success("🟢 LOW PRIORITY INCIDENT")

    c1,c2,c3=st.columns(3)

    c1.metric(
        "🎯 Confidence",
        f"{result['confidence']}%"
    )

    c2.metric(
        "📊 Impact Score",
        f"{rec['impact_score']}/100"
    )

    c3.metric(
        "🚦 Impact",
        rec["impact_level"]
    )

    st.subheader("🔥 Incident Severity")

    st.progress(rec["impact_score"]/100)

    if rec["impact_level"]=="High":
        st.error("🔴 HIGH IMPACT")

    elif rec["impact_level"]=="Medium":
        st.warning("🟠 MEDIUM IMPACT")

    else:
        st.success("🟢 LOW IMPACT")
    
    st.divider()

    # ================= AI SUMMARY =================

    st.subheader("🧠 AI Incident Summary")

    summary = f"""
A **{result['predicted_priority']} Priority** incident has been detected.

• **Impact Level:** {rec['impact_level']}
• **Emergency Status:** {rec['emergency_status']}
• **Estimated Clearance Time:** {rec['estimated_clearance_time']}

The AI recommends immediate allocation of available traffic resources
based on the predicted severity and expected congestion.
"""

    st.info(summary)

    # ================= RESPONSE PLAN =================

    st.subheader("🤖 AI Response Plan")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👮 Officers",
            rec["officers_required"]
        )

    with col2:
        st.metric(
            "🚧 Barricades",
            rec["barricades_required"]
        )

    with col3:
        st.metric(
            "🔀 Diversion",
            "YES" if rec["diversion_required"] else "NO"
        )

    st.info(
        f"⏱ Estimated Clearance Time: {rec['estimated_clearance_time']}"
    )

    st.write("### ✅ Recommended Actions")

    for action in rec["actions"]:
        st.success(action)

    st.divider()

    # ================= LOCATION =================

    st.subheader("📍 Incident Location")

    st.success(
        result["location"]["formatted_address"]
    )

    st.divider()

    # ================= EMERGENCY RESOURCES =================

    st.subheader("🚓 Emergency Resource Allocation")

    p, h, f = st.columns(3)

    with p:
        st.info("🚓 Police Station")
        st.write(resources["police"])

    with h:
        st.info("🏥 Hospital")
        st.write(resources["hospital"])

    with f:
        st.info("🚒 Fire Station")
        st.write(resources["fire_station"])

    st.divider()

    # ================= TIMELINE =================

    st.subheader("🕒 AI Response Timeline")

    timeline = [
        "🚨 Incident Reported",
        "🤖 AI Prediction Completed",
        "📍 Location Identified",
        "👮 Emergency Resources Allocated",
        "🚧 Traffic Diversion Recommended"
    ]

    for step in timeline:
        st.success(step)

    st.divider()

    # ================= MAP =================

    st.subheader("🗺 Incident Map")

    st.map(
        pd.DataFrame(
            {
                "lat": [latitude],
                "lon": [longitude]
            }
        )
    )

    st.divider()

    # ================= FOOTER =================

    st.markdown(
        """
---
### 🚦 EventPulse-AI

**Predict. Prepare. Prevent.**

Powered by:

- 🤖 Random Forest Machine Learning
- ⚡ FastAPI
- 🎨 Streamlit
- 🗺 Mappls API
- 📍 Reverse Geocoding
- 🚓 AI Resource Recommendation Engine

**Version 1.0 | Hackathon Prototype**
"""
    )
