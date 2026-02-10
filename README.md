⚽ FIFA Career Mode Assistant
============================

A comprehensive desktop application designed to enhance the FIFA Career Mode experience. This tool helps players discover teams based on difficulty, find hidden gems and "wonderkids," manage youth academy scouting, and track seasonal performance stats with visual analytics.

🚀 Features
-----------

-   **Smart Team Generator**: Get a random team to manage based on your desired challenge level (Easy, Medium, Hard). It even calculates a realistic transfer budget based on the team's prestige.

-   **Deep Player Search**: Filter through a massive database by position, age, current rating, and potential to find the perfect signing.

-   **Wonderkid Finder**: Instantly identify high-growth players (aged 16-21) with potential ratings up to 90.

-   **Youth Academy Scout**: Generates specific scouting instructions, including country, position, and playstyle specialities (e.g., "Ball-Playing Defender" or "False 9").

-   **Formation Randomizer**: Stuck in a tactical rut? Generate random formations based on your preferred number of defenders.

-   **Season Stats Tracker**: Input player performance (goals, assists, ratings) and generate histograms to visualize your squad's contribution over a season.

-   **Career Storylines**: Get creative prompts and "Career Ideas" (Realistic, Challenging, or Fun) to keep your saves fresh.

📊 The Data
-----------

The power of this assistant comes from its extensive, real-world dataset:

-   **27,000+ Players**: A massive database compiled to ensure you can find every player from the top leagues to the lower divisions.

-   **100+ Teams**: Detailed stats for over a hundred clubs, including their Attack, Midfield, Defense, and Average Age.

-   **Web Scraped Accuracy**: All data was meticulously **scraped from leading football databases** to ensure ratings and potentials are as accurate as possible.

🛠️ Technical Stack
-------------------

-   **Language**: Python 3.x

-   **GUI Framework**: Tkinter (for a clean, native desktop experience)

-   **Data Handling**: Pandas & NumPy

-   **Visualization**: Matplotlib (for season stats charts)

-   **Data Source**: Excel (`.xlsx`) and Text (`.txt`) files

📂 File Structure
-----------------

-   `fifa_assistant.py`: The main entry point containing the Tkinter GUI logic.

-   `players.py`: Logic for reading and filtering the player database.

-   `teams.py`: Logic for team statistics and selection.

-   `extras.py`: Supporting functions for randomizations, career ideas, and scouting.

⚙️ Installation & Usage
-----------------------

1.  **Clone the repository**:

    Bash

    ```
    git clone https://github.com/yourusername/fifa-career-assistant.git

    ```

2.  **Install dependencies**:

    Bash

    ```
    pip install pandas numpy matplotlib openpyxl

    ```

3.  **Run the application**:

    Bash

    ```
    python fifa_assistant.py

    ```

> **Note**: Ensure that `allteams.xlsx`, `players.xlsx`, `players1.xlsx`, `formations.xlsx`, and `ideas.xlsx` are in the root directory for the app to load data correctly.
