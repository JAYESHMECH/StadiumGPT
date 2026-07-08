import streamlit as st
st.set_page_config(page_title="StadiumGPT", page_icon="🏟️")
st.title("🏟️ StadiumGPT")
q=st.text_input("Ask anything")
if q:
    q=q.lower()
    if "gate" in q: st.success("Recommended Gate: Gate B (Low Crowd)")
    elif "seat" in q: st.success("Your seat is Block A Level 2")
    elif "food" in q: st.success("Pizza Corner has the shortest queue (5 min).")
    elif "washroom" in q: st.success("Nearest washroom is 30 meters away.")
    elif "emergency" in q or "help" in q: st.error("Medical Team has been notified.")
    else: st.info("AI Recommendation: Follow the nearest stadium information board.")
