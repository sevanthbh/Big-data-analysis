import streamlit as st
import dask.dataframe as dd
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Set page config with dark theme
st.set_page_config(page_title="Big Data Analysis", page_icon="📊", layout="wide")

# Custom Dark Theme CSS
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stTextInput>div>div>input {
            background-color: #1E1E1E;
            color: white;
        }
        .stButton>button {
            background-color: #BB86FC;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("📊 Big Data Analysis Dashboard")

# Sidebar for User Input
st.sidebar.title("⚙️ Settings")
data_size = st.sidebar.slider("Select Dataset Size (rows)", 1000, 5000000, 100000)

# Generate Large Data using Dask
st.sidebar.write("Generating dataset... ⏳")
start_time = time.time()
df = dd.from_pandas(pd.DataFrame(np.random.rand(data_size, 10), columns=[f"col_{i}" for i in range(10)]), npartitions=10)
end_time = time.time()
st.sidebar.success(f"✅ Dataset Created in {round(end_time - start_time, 2)}s!")

# Show Data Sample
if st.checkbox("📜 Show Sample Data"):
    st.write(df.compute().head(10))

# Perform Analysis
st.subheader("📊 Data Analysis")
st.write("Mean of each column:")

mean_values = df.mean().compute()
st.write(mean_values)

# Visualization with Line Graph
st.subheader("📈 Data Distribution (Line Chart)")

fig, ax = plt.subplots(figsize=(10, 5))
mean_values.plot(kind="line", marker="o", color="cyan", ax=ax)
ax.set_title("Mean Value of Each Column", fontsize=14, color="white")
ax.set_facecolor("#121212")
ax.grid(color="gray", linestyle="--", linewidth=0.5)
ax.tick_params(axis="x", colors="white")
ax.tick_params(axis="y", colors="white")

st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("🚀 **Powered by Dask & Streamlit** | Made with ❤️ by Sevanth")
