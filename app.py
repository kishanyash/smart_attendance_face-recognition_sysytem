import streamlit as st
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Set page config
st.set_page_config(
    page_title="Smart Attendance Dashboard",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Title and subheader
st.title("📋 Smart Attendance Dashboard")
st.subheader("Live Attendance Records")
st.markdown("---")

# Auto-refresh every 2 seconds
count = st_autorefresh(interval=20000, limit=None, key="attendance_refresh")

# Fun refresh counter
if count == 0:
    st.info("⏳ Waiting for first refresh...")
elif count % 3 == 0 and count % 5 == 0:
    st.success("FizzBuzz! 🎉")
elif count % 3 == 0:
    st.info("Fizz ⚡")
elif count % 5 == 0:
    st.warning("Buzz 🔔")
else:
    st.write(f"🔄 Refresh count: {count}")

# Get current date
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
file_path = f"Attendance/Attendance_{date}.csv"

try:
    # Load today's attendance file
    df = pd.read_csv(file_path)

    # Style and display DataFrame
    st.dataframe(
        df.style.highlight_max(axis=0).set_properties(**{
            'background-color': '#f0f8ff',
            'color': 'black',
            'border-color': 'gray'
        }),
        use_container_width=True
    )

    # Show summary stats
    st.markdown("### 📊 Attendance Summary")
    st.write(f"**Total Entries:** {len(df)}")
    st.write(f"**Last Entry:** {df.iloc[-1, 0]} at {df.iloc[-1, 1]}")

except FileNotFoundError:
    st.error(f"⚠ No attendance file found for {date}.")
    st.info("Make sure to take attendance first.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Kishan")
