# 🎬 Netflix Titles Explorer

An interactive Streamlit dashboard for exploring 8,797 Netflix movies and TV shows: when titles were added, how they are rated, and how long the movies are.

**Live app:** _paste your Streamlit link here_

## What the app shows

- **3 charts:** titles added per year (movies vs TV shows), titles per rating, and a histogram of movie length.
- **3 key numbers:** titles shown, median movie length, and the most common rating.
- **Filters (sidebar):** type (Movie / TV Show), release year, and audience group (Kids, Family & Teens, Adults, Unrated).
- **Download button:** saves the currently filtered data as a CSV.

## About the data

The data is the public [`netflix_titles.csv` dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) (8,807 rows). It was cleaned in the VizLab notebook, and the result is saved as `netflix_clean.csv`. The cleaning steps were:

- Filled missing `director`, `cast` and `country` values with "Unknown".
- Dropped 10 rows with no `date_added`.
- Moved 3 movie lengths that were sitting in the `rating` column back into `duration`.
- Stripped stray spaces from dates and converted them to real dates.
- Added helper columns: `year_added`, `duration_min`, `seasons`, `audience`, `n_genres`, `n_countries` and `cast_size`.

No rows were removed as duplicates, because there were none.

## Project files

| File | What it is |
|---|---|
| `app.py` | The Streamlit app |
| `netflix_clean.csv` | The cleaned data the app reads |
| `requirements.txt` | Python packages needed |
| `README.md` | This file |
| `.gitignore` | Files Git should ignore |

## Run it on your computer

1. Make sure Python 3.9 or newer is installed.
2. Open a terminal in this folder and install the packages:
   ```
   pip install -r requirements.txt
   ```
3. Start the app:
   ```
   streamlit run app.py
   ```
4. Your browser opens at `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push this folder to a **public** GitHub repository (`netflix_clean.csv` must be included).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app**, choose your repository and the `main` branch, and set the main file path to `app.py`.
4. Click **Deploy**, wait about a minute, then copy the link into this README.

## Built with

Python, pandas, matplotlib, seaborn and Streamlit.
