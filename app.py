import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Netflix Titles Explorer", page_icon="🎬", layout="wide")

RED, DARK = "#E50914", "#221F1F"
sns.set_theme(style="whitegrid")


@st.cache_data
def load_data():
    return pd.read_csv("netflix_clean.csv", parse_dates=["date_added"])


df = load_data()

st.title("🎬 Netflix Titles Explorer")
st.caption("Explore 8,797 Netflix movies and TV shows. Use the filters on the left.")

# ---------- Filters ----------
st.sidebar.header("Filters")

types = st.sidebar.multiselect("Type", sorted(df["type"].unique()), default=sorted(df["type"].unique()))

year_min, year_max = int(df["release_year"].min()), int(df["release_year"].max())
years = st.sidebar.slider("Release year", year_min, year_max, (year_min, year_max))

audience_options = ["Kids", "Family & Teens", "Adults", "Unrated"]
audiences = st.sidebar.multiselect("Audience", audience_options, default=audience_options)

filtered = df[
    df["type"].isin(types)
    & df["release_year"].between(years[0], years[1])
    & df["audience"].isin(audiences)
]

if filtered.empty:
    st.warning("No titles match these filters. Try widening them.")
    st.stop()

# ---------- Key numbers ----------
movies = filtered[filtered["type"] == "Movie"]

c1, c2, c3 = st.columns(3)
c1.metric("Titles shown", f"{len(filtered):,}")
c2.metric("Median movie length", f"{movies['duration_min'].median():.0f} min" if len(movies) else "n/a")
c3.metric("Most common rating", filtered["rating"].value_counts().index[0])

st.divider()

# ---------- Chart 1: trend ----------
st.subheader("Titles added to Netflix each year")
per_year = filtered.groupby(["year_added", "type"]).size().unstack(fill_value=0)
fig1, ax1 = plt.subplots(figsize=(10, 4))
for col, color in [("Movie", RED), ("TV Show", DARK)]:
    if col in per_year:
        ax1.plot(per_year.index, per_year[col], marker="o", color=color, label=col)
ax1.set_xlabel("Year added")
ax1.set_ylabel("Number of titles")
ax1.legend()
st.pyplot(fig1)

left, right = st.columns(2)

# ---------- Chart 2: ratings ----------
with left:
    st.subheader("Titles per rating")
    counts = filtered["rating"].value_counts().sort_values()
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    ax2.barh(counts.index, counts.values, color=RED)
    ax2.set_xlabel("Number of titles")
    ax2.set_ylabel("Rating")
    st.pyplot(fig2)

# ---------- Chart 3: movie length ----------
with right:
    st.subheader("How long are the movies?")
    if len(movies):
        fig3, ax3 = plt.subplots(figsize=(6, 5))
        sns.histplot(movies["duration_min"], bins=30, color=RED, ax=ax3)
        ax3.set_xlabel("Movie length (minutes)")
        ax3.set_ylabel("Number of movies")
        st.pyplot(fig3)
    else:
        st.info("No movies in the current selection.")

# ---------- Bonus: download ----------
st.download_button(
    "Download filtered clean data (CSV)",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="netflix_filtered.csv",
    mime="text/csv",
)
