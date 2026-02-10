import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from extras import *
from players import *
from teams import *

class FIFACareerModeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FIFA Career Mode Generator")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a5f3d")
        
        # Initialize data dictionaries
        try:
            self.team_dict = readteams("allteams.xlsx")
            self.player_dict = readplayers()
        except Exception as e:
            messagebox.showerror("Error Loading Data", f"Could not load data files:\n{str(e)}\n\nPlease ensure all Excel files are in the directory.")
            self.team_dict = {}
            self.player_dict = {}
        
        # Season stats storage
        self.season_stats = []
        
        # Create main container
        main_frame = tk.Frame(root, bg="#1a5f3d")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="⚽ FIFA Career Mode Generator ⚽",
            font=("Arial", 24, "bold"),
            bg="#1a5f3d",
            fg="white"
        )
        title_label.pack(pady=10)
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create tabs
        self.create_team_tab()
        self.create_player_tab()
        self.create_wonderkid_tab()
        self.create_youth_tab()
        self.create_formation_tab()
        self.create_career_tab()
        self.create_stats_tab()
        
        # Style configuration
        self.configure_styles()
    
    def configure_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background="#1a5f3d", borderwidth=0)
        style.configure('TNotebook.Tab', padding=[20, 10], font=("Arial", 10, "bold"))
        style.map('TNotebook.Tab', background=[('selected', '#2d8659')], foreground=[('selected', 'white')])
    
    def create_team_tab(self):
        frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(frame, text="🏆 Random Team")
        
        # Content frame
        content = tk.Frame(frame, bg="white", padx=30, pady=30)
        content.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(content, text="Random Team Generator", font=("Arial", 18, "bold"), bg="white", fg="#1a5f3d").pack(pady=(0, 20))
        
        # Difficulty selection
        tk.Label(content, text="Select Difficulty:", font=("Arial", 12), bg="white").pack(anchor=tk.W, pady=(0, 5))
        
        self.difficulty_var = tk.StringVar(value="Easy")
        difficulty_frame = tk.Frame(content, bg="white")
        difficulty_frame.pack(fill=tk.X, pady=(0, 10))
        
        for diff in ["Easy", "Medium", "Hard"]:
            tk.Radiobutton(
                difficulty_frame, 
                text=f"{diff} (OVR {80-20*(diff!='Easy')*1-10*(diff=='Hard')}-{90-20*(diff!='Easy')*1-10*(diff=='Hard')})",
                variable=self.difficulty_var,
                value=diff,
                font=("Arial", 10),
                bg="white",
                fg="black"
            ).pack(anchor=tk.W, pady=2)
        
        # Generate button
        tk.Button(
            content,
            text="Generate Random Team",
            command=self.generate_team,
            font=("Arial", 12, "bold"),
            bg="#2d8659",
            fg="white",
            padx=30,
            pady=10,
            cursor="hand2"
        ).pack(pady=20)
        
        # Result area
        self.team_result = scrolledtext.ScrolledText(content, height=10, font=("Arial", 10), wrap=tk.WORD)
        self.team_result.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    def create_player_tab(self):
        frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(frame, text="👤 Find Player")
        
        content = tk.Frame(frame, bg="white", padx=30, pady=30)
        content.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(content, text="Find Random Player", font=("Arial", 18, "bold"), bg="white", fg="#1a5f3d").pack(pady=(0, 20))
        
        # Input frame
        input_frame = tk.Frame(content, bg="white")
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Position
        tk.Label(input_frame, text="Position:", font=("Arial", 10), bg="white").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.position_var = tk.StringVar(value="ST")
        positions = ['GK', 'CB', 'RB', 'LB', 'CDM', 'CM', 'CAM', 'RM', 'LM', 'RW', 'LW', 'RF', 'LF', 'ST']
        ttk.Combobox(input_frame, textvariable=self.position_var, values=positions, state="readonly", width=15).grid(row=0, column=1, pady=5, padx=5)
        
        # OVR Range
        tk.Label(input_frame, text="OVR Range:", font=("Arial", 10), bg="white").grid(row=1, column=0, sticky=tk.W, pady=5)
        ovr_frame = tk.Frame(input_frame, bg="white")
        ovr_frame.grid(row=1, column=1, pady=5, padx=5)
        self.ovr_min = tk.Spinbox(ovr_frame, from_=40, to=99, width=8)
        self.ovr_min.delete(0, tk.END)
        self.ovr_min.insert(0, "60")
        self.ovr_min.pack(side=tk.LEFT, padx=2)
        tk.Label(ovr_frame, text="to", bg="white").pack(side=tk.LEFT, padx=2)
        self.ovr_max = tk.Spinbox(ovr_frame, from_=40, to=99, width=8)
        self.ovr_max.delete(0, tk.END)
        self.ovr_max.insert(0, "90")
        self.ovr_max.pack(side=tk.LEFT, padx=2)
        
        # Age Range
        tk.Label(input_frame, text="Age Range:", font=("Arial", 10), bg="white").grid(row=2, column=0, sticky=tk.W, pady=5)
        age_frame = tk.Frame(input_frame, bg="white")
        age_frame.grid(row=2, column=1, pady=5, padx=5)
        self.age_min = tk.Spinbox(age_frame, from_=16, to=45, width=8)
        self.age_min.delete(0, tk.END)
        self.age_min.insert(0, "16")
        self.age_min.pack(side=tk.LEFT, padx=2)
        tk.Label(age_frame, text="to", bg="white").pack(side=tk.LEFT, padx=2)
        self.age_max = tk.Spinbox(age_frame, from_=16, to=45, width=8)
        self.age_max.delete(0, tk.END)
        self.age_max.insert(0, "40")
        self.age_max.pack(side=tk.LEFT, padx=2)
        
        # Potential Range
        tk.Label(input_frame, text="Potential Range:", font=("Arial", 10), bg="white").grid(row=3, column=0, sticky=tk.W, pady=5)
        pot_frame = tk.Frame(input_frame, bg="white")
        pot_frame.grid(row=3, column=1, pady=5, padx=5)
        self.pot_min = tk.Spinbox(pot_frame, from_=40, to=99, width=8)
        self.pot_min.delete(0, tk.END)
        self.pot_min.insert(0, "60")
        self.pot_min.pack(side=tk.LEFT, padx=2)
        tk.Label(pot_frame, text="to", bg="white").pack(side=tk.LEFT, padx=2)
        self.pot_max = tk.Spinbox(pot_frame, from_=40, to=99, width=8)
        self.pot_max.delete(0, tk.END)
        self.pot_max.insert(0, "90")
        self.pot_max.pack(side=tk.LEFT, padx=2)
        
        # Generate button
        tk.Button(
            content,
            text="Find Random Player",
            command=self.generate_player,
            font=("Arial", 12, "bold"),
            bg="#2d8659",
            fg="white",
            padx=30,
            pady=10,
            cursor="hand2"
        ).pack(pady=20)
        
        # Result area
        self.player_result = scrolledtext.ScrolledText(content, height=8, font=("Arial", 10), wrap=tk.WORD)
        self.player_result.pack(fill=tk.BOTH, expand=True)
    
    def create_wonderkid_tab(self):
        frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(frame, text="✨ Wonderkid")
        
        content = tk.Frame(frame, bg="white", padx=30, pady=30)
        content.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(content, text="Wonderkid Generator", font=("Arial", 18, "bold"), bg="white", fg="#1a5f3d").pack(pady=(0, 20))
        
        # Criteria info
        info_frame = tk.Frame(content, bg="#e8f5e9", relief=tk.RIDGE, bd=2)
        info_frame.pack(fill=tk.X, pady=(0, 20), padx=10, ipady=10)
        
        tk.Label(info_frame, text="Wonderkid Criteria:", font=("Arial", 12, "bold"), bg="#e8f5e9", fg="#1a5f3d").pack(pady=(10, 5))
        tk.Label(info_frame, text="• Age: 16-21 years old", font=("Arial", 10), bg="#e8f5e9", anchor=tk.W).pack(anchor=tk.W, padx=20)
        tk.Label(info_frame, text="• Potential: 82-90", font=("Arial", 10), bg="#e8f5e9", anchor=tk.W).pack(anchor=tk.W, padx=20)
        tk.Label(info_frame, text="• Current OVR: 60-80", font=("Arial", 10), bg="#e8f5e9", anchor=tk.W).pack(anchor=tk.W, padx=20, pady=(0, 10))
        
        # Generate button
        tk.Button(
            content,
            text="Find Random Wonderkid",
            command=self.generate_wonderkid,
            font=("Arial", 12, "bold"),
            bg="#2d8659",
            fg="white",
            padx=30,
            pady=10,
            cursor="hand2"
        ).pack(pady=20)
        
        # Result area
        self.wonderkid_result = scrolledtext.ScrolledText(content, height=10, font=("Arial", 10), wrap=tk.WORD)
        self.wonderkid_result.pack(fill=tk.BOTH, expand=True)
    
    def create_youth_tab(self):
        frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(frame, text="🎯 Youth Academy")
        
        content = tk.Frame(frame, bg="white", padx=30, pady=30)
        content.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(content, text="Youth Academy Scout", font=("Arial", 18, "bold"), bg="white", fg="#1a5f3d").pack(pady=(0, 20))
        
        # Continent selection
        tk.Label(content, text="Select Continent:", font=("Arial", 12), bg="white").pack(anchor=tk.W, pady=(0, 5))
        
        self.continent_var = tk.StringVar(value="Europe")
        continents = ['Europe', 'South America', 'North America', 'Africa', 'Asia', 'Oceania']
        ttk.Combobox(content, textvariable=self.continent_var, values=continents, state="readonly", width=20, font=("Arial", 10)).pack(anchor=tk.W, pady=(0, 10))
        
        # Info
        info_frame = tk.Frame(content, bg="#e3f2fd", relief=tk.RIDGE, bd=2)
        info_frame.pack(fill=tk.X, pady=(10, 20), padx=10, ipady=10)
        tk.Label(
            info_frame, 
            text="This will randomly select a position, country from the selected continent,\nand position speciality for your youth scout.",
            font=("Arial", 9),
            bg="#e3f2fd",
            justify=tk.LEFT
        ).pack(pady=10, padx=10)
        
        # Generate button
        tk.Button(
            content,
            text="Generate Youth Scout Instructions",
            command=self.generate_youth,
            font=("Arial", 12, "bold"),
            bg="#2d8659",
            fg="white",
            padx=30,
            pady=10,
            cursor="hand2"
        ).pack(pady=20)
        
        # Result area
        self.youth_result = scrolledtext.ScrolledText(content, height=10, font=("Arial", 10), wrap=tk.WORD)
        self.youth_result.pack(fill=tk.BOTH, expand=True)
    
    def create_formation_tab(self):
        frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(frame, text="🛡️ Formation")
        
        content = tk.Frame(frame, bg="white", padx=30, pady=30)
        content.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(content, text="Formation Generator", font=("Arial", 18, "bold"), bg="white", fg="#1a5f3d").pack(pady=(0, 20))
        
        # Defender count selection
        tk.Label(content, text="Number of Defenders:", font=("Arial", 12), bg="white").pack(anchor=tk.W, pady=(0, 5))
        
        self.defender_var = tk.IntVar(value=4)
        defender_frame = tk.Frame(content, bg="white")
        defender_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Radiobutton(defender_frame, text="3 Defenders (Attacking)", variable=self.defender_var, value=3, font=("Arial", 10), bg="white").pack(anchor=tk.W, pady=2)
        tk.Radiobutton(defender_frame, text="4 Defenders (Balanced)", variable=self.defender_var, value=4, font=("Arial", 10), bg="white").pack(anchor=tk.W, pady=2)
        tk.Radiobutton(defender_frame, text="5 Defenders (Defensive)", variable=self.defender_var, value=5, font=("Arial", 10), bg="white").pack(anchor=tk.W, pady=2)
        tk.Radiobutton(defender_frame, text="Random (Any)", variable=self.defender_var, value=0, font=("Arial", 10), bg="white").pack(anchor=tk.W, pady=2)
        
        # Generate button
        tk.Button(
            content,
            text="Generate Formation",
            command=self.generate_formation,
            font=("Arial", 12, "bold"),
            bg="#2d8659",
            fg="white",
            padx=30,
            pady=10,
            cursor="hand2"
        ).pack(pady=20)
        
        # Result area
        self.formation_result = scrolledtext.ScrolledText(content, height=10, font=("Arial", 10), wrap=tk.WORD)
        self.formation_result.pack(fill=tk.BOTH, expand=True)
    
    def create_career_tab(self):
        frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(frame, text="📈 Career Ideas")
        
        content = tk.Frame(frame, bg="white", padx=30, pady=30)
        content.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(content, text="Career Mode Ideas", font=("Arial", 18, "bold"), bg="white", fg="#1a5f3d").pack(pady=(0, 20))
        
        # Storyline selection
        tk.Label(content, text="Storyline Category:", font=("Arial", 12), bg="white").pack(anchor=tk.W, pady=(0, 5))
        
        self.storyline_var = tk.StringVar(value="Realistic")
        storylines = ['Realistic', 'Challenging', 'Fun', 'Creative', 'Specific']
        ttk.Combobox(content, textvariable=self.storyline_var, values=storylines, state="readonly", width=20, font=("Arial", 10)).pack(anchor=tk.W, pady=(0, 10))
        
        # Info about categories
        info_frame = tk.Frame(content, bg="#f3e5f5", relief=tk.RIDGE, bd=2)
        info_frame.pack(fill=tk.X, pady=(10, 20), padx=10, ipady=10)
        
        tk.Label(info_frame, text="Categories:", font=("Arial", 11, "bold"), bg="#f3e5f5", fg="#1a5f3d").pack(anchor=tk.W, padx=10, pady=(10, 5))
        categories_text = [
            "• Realistic: Grounded career paths",
            "• Challenging: Hardcore difficulty modes",
            "• Fun: Unique and entertaining concepts",
            "• Creative: Story-driven experiences",
            "• Specific: Niche scenarios"
        ]
        for cat in categories_text:
            tk.Label(info_frame, text=cat, font=("Arial", 9), bg="#f3e5f5", anchor=tk.W).pack(anchor=tk.W, padx=20)
        tk.Label(info_frame, text="", bg="#f3e5f5").pack(pady=5)
        
        # Generate button
        tk.Button(
            content,
            text="Generate Career Idea",
            command=self.generate_career,
            font=("Arial", 12, "bold"),
            bg="#2d8659",
            fg="white",
            padx=30,
            pady=10,
            cursor="hand2"
        ).pack(pady=20)
        
        # Result area
        self.career_result = scrolledtext.ScrolledText(content, height=8, font=("Arial", 10), wrap=tk.WORD)
        self.career_result.pack(fill=tk.BOTH, expand=True)
    
    def create_stats_tab(self):
        frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(frame, text="📊 Season Stats")
        
        content = tk.Frame(frame, bg="white", padx=30, pady=20)
        content.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(content, text="Season Stats Tracker", font=("Arial", 18, "bold"), bg="white", fg="#1a5f3d").pack(pady=(0, 15))
        
        # Team info
        info_frame = tk.Frame(content, bg="white")
        info_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(info_frame, text="Team Name:", font=("Arial", 10), bg="white").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.team_name_entry = tk.Entry(info_frame, font=("Arial", 10), width=25)
        self.team_name_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(info_frame, text="Season:", font=("Arial", 10), bg="white").grid(row=0, column=2, sticky=tk.W, padx=(20, 5))
        self.season_entry = tk.Entry(info_frame, font=("Arial", 10), width=15)
        self.season_entry.insert(0, "2024/2025")
        self.season_entry.grid(row=0, column=3, padx=5)
        
        # Player input frame
        player_frame = tk.LabelFrame(content, text="Add Player Stats", font=("Arial", 11, "bold"), bg="#f5f5f5", padx=15, pady=10)
        player_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Player name
        tk.Label(player_frame, text="Player Name:", font=("Arial", 9), bg="#f5f5f5").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.player_name_entry = tk.Entry(player_frame, font=("Arial", 9), width=20)
        self.player_name_entry.grid(row=0, column=1, columnspan=3, sticky=tk.W, pady=5, padx=5)
        
        # Stats inputs
        stats_labels = ["Goals:", "Assists:", "Appearances:", "Avg Rating:", "Clean Sheets:"]
        self.stats_entries = {}
        
        for i, label in enumerate(stats_labels):
            tk.Label(player_frame, text=label, font=("Arial", 9), bg="#f5f5f5").grid(row=1+i//3, column=(i%3)*2, sticky=tk.W, pady=3, padx=(0, 5))
            entry = tk.Entry(player_frame, font=("Arial", 9), width=10)
            entry.insert(0, "0")
            entry.grid(row=1+i//3, column=(i%3)*2+1, pady=3, padx=5)
            self.stats_entries[label.replace(":", "").lower().replace(" ", "_")] = entry
        
        # Add button
        tk.Button(
            player_frame,
            text="Add Player",
            command=self.add_player_stats,
            font=("Arial", 10, "bold"),
            bg="#1976d2",
            fg="white",
            cursor="hand2",
            padx=20,
            pady=5
        ).grid(row=3, column=0, columnspan=4, pady=10)
        
        # Stats display
        stats_display_frame = tk.Frame(content, bg="white")
        stats_display_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(stats_display_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.stats_text = tk.Text(stats_display_frame, height=10, font=("Courier", 9), yscrollcommand=scrollbar.set, wrap=tk.NONE)
        self.stats_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.stats_text.yview)
        
        # Buttons
        button_frame = tk.Frame(content, bg="white")
        button_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(
            button_frame,
            text="Clear All",
            command=self.clear_stats,
            font=("Arial", 10),
            bg="#d32f2f",
            fg="white",
            cursor="hand2",
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="View Charts",
            command=self.view_charts,
            font=("Arial", 10),
            bg="#2d8659",
            fg="white",
            cursor="hand2",
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Save to CSV",
            command=self.save_stats,
            font=("Arial", 10),
            bg="#ff9800",
            fg="white",
            cursor="hand2",
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
    
    # Generator Methods
    def generate_team(self):
        if not self.team_dict:
            messagebox.showerror("Error", "Team dictionary is empty. Please load allteams.xlsx")
            return
        
        try:
            difficulty = self.difficulty_var.get()
            team_name = get_random_team(self.team_dict, difficulty)
            
            # Get team details
            ovr = getovr(self.team_dict, team_name)
            att = getatt(self.team_dict, team_name)
            mid = getmid(self.team_dict, team_name)
            defense = getdef(self.team_dict, team_name)
            avg_age = getavgage(self.team_dict, team_name)
            budget = get_random_budget(self.team_dict, team_name, None)
            
            result = f"{'='*50}\n"
            result += f"RANDOM TEAM GENERATED\n"
            result += f"{'='*50}\n\n"
            result += f"Team: {team_name}\n"
            result += f"Difficulty: {difficulty}\n"
            result += f"Overall Rating: {ovr}\n"
            result += f"Attack: {att}\n"
            result += f"Midfield: {mid}\n"
            result += f"Defense: {defense}\n"
            result += f"Average Age: {avg_age}\n"
            result += f"Transfer Budget: £{budget/1000000:.1f}M\n"
            
            self.team_result.delete(1.0, tk.END)
            self.team_result.insert(1.0, result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not generate team:\n{str(e)}")
    
    def generate_player(self):
        if not self.player_dict:
            messagebox.showerror("Error", "Player dictionary is empty. Please load player files")
            return
        
        try:
            position = self.position_var.get()
            ovr_range = range(int(self.ovr_min.get()), int(self.ovr_max.get()) + 1)
            age_range = range(int(self.age_min.get()), int(self.age_max.get()) + 1)
            pot_range = range(int(self.pot_min.get()), int(self.pot_max.get()) + 1)
            
            player_name = get_random_player(self.player_dict, ovr_range, age_range, pot_range, position)
            
            # Get player details
            ovr = getplayerovr(self.player_dict, player_name)
            pot = getplayerpot(self.player_dict, player_name)
            age = getplayerage(self.player_dict, player_name)
            team = getplayerteam(self.player_dict, player_name)
            
            result = f"{'='*50}\n"
            result += f"PLAYER FOUND\n"
            result += f"{'='*50}\n\n"
            result += f"Name: {player_name}\n"
            result += f"Position: {position}\n"
            result += f"Current Team: {team}\n"
            result += f"Overall: {ovr}\n"
            result += f"Potential: {pot}\n"
            result += f"Age: {age}\n"
            
            self.player_result.delete(1.0, tk.END)
            self.player_result.insert(1.0, result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not find player:\n{str(e)}")
    
    def generate_wonderkid(self):
        if not self.player_dict:
            messagebox.showerror("Error", "Player dictionary is empty. Please load player files")
            return
        
        try:
            player_name = get_random_wonderkid(self.player_dict)
            
            # Get player details
            ovr = getplayerovr(self.player_dict, player_name)
            pot = getplayerpot(self.player_dict, player_name)
            age = getplayerage(self.player_dict, player_name)
            pos = getplayerpos(self.player_dict, player_name)
            team = getplayerteam(self.player_dict, player_name)
            
            result = f"{'='*50}\n"
            result += f"WONDERKID FOUND\n"
            result += f"{'='*50}\n\n"
            result += f"Name: {player_name}\n"
            result += f"Position: {pos}\n"
            result += f"Current Team: {team}\n"
            result += f"Age: {age} years old\n"
            result += f"Current Overall: {ovr}\n"
            result += f"Potential: {pot}\n"
            result += f"\nGrowth Potential: {pot - ovr} points\n"
            
            self.wonderkid_result.delete(1.0, tk.END)
            self.wonderkid_result.insert(1.0, result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not find wonderkid:\n{str(e)}")
    
    def generate_youth(self):
        try:
            continent = self.continent_var.get()
            position = get_youthacademypos()
            country = get_youthcountry(continent)
            speciality = getpositionspeciality(position)
            
            result = f"{'='*50}\n"
            result += f"YOUTH ACADEMY SCOUT INSTRUCTIONS\n"
            result += f"{'='*50}\n\n"
            result += f"Continent: {continent}\n"
            result += f"Country: {country}\n"
            result += f"Position: {position}\n"
            result += f"Speciality: {speciality}\n"
            result += f"\nSend your scout to {country} to find a {position}\n"
            result += f"with {speciality} playing style.\n"
            
            self.youth_result.delete(1.0, tk.END)
            self.youth_result.insert(1.0, result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not generate youth instructions:\n{str(e)}")
    
    def generate_formation(self):
        try:
            defender_count = self.defender_var.get()
            formation = get_random_formation(defender_count)
            
            style = "Balanced"
            if defender_count == 3:
                style = "Attacking"
            elif defender_count == 5:
                style = "Defensive"
            elif defender_count == 0:
                style = "Random"
            
            result = f"{'='*50}\n"
            result += f"FORMATION GENERATED\n"
            result += f"{'='*50}\n\n"
            result += f"Formation: {formation}\n"
            result += f"Defenders: {defender_count if defender_count > 0 else 'Random'}\n"
            result += f"Style: {style}\n"
            
            self.formation_result.delete(1.0, tk.END)
            self.formation_result.insert(1.0, result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not generate formation:\n{str(e)}")
    
    def generate_career(self):
        try:
            storyline = self.storyline_var.get()
            career_idea = getcareeridea(storyline)
            
            result = f"{'='*50}\n"
            result += f"CAREER MODE IDEA\n"
            result += f"{'='*50}\n\n"
            result += f"Category: {storyline}\n\n"
            result += f"{career_idea}\n"
            
            self.career_result.delete(1.0, tk.END)
            self.career_result.insert(1.0, result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not generate career idea:\n{str(e)}")
    
    def add_player_stats(self):
        try:
            player_name = self.player_name_entry.get().strip()
            if not player_name:
                messagebox.showwarning("Warning", "Please enter a player name")
                return
            
            goals = int(self.stats_entries['goals'].get())
            assists = int(self.stats_entries['assists'].get())
            appearances = int(self.stats_entries['appearances'].get())
            rating = float(self.stats_entries['avg_rating'].get())
            clean_sheets = int(self.stats_entries['clean_sheets'].get())
            
            # Validate
            if goals < 0 or assists < 0 or appearances < 0 or clean_sheets < 0:
                messagebox.showerror("Error", "Stats cannot be negative")
                return
            if rating < 0 or rating > 10:
                messagebox.showerror("Error", "Rating must be between 0 and 10")
                return
            
            player_stat = {
                'name': player_name,
                'goals': goals,
                'assists': assists,
                'appearances': appearances,
                'rating': rating,
                'clean_sheets': clean_sheets
            }
            
            self.season_stats.append(player_stat)
            self.update_stats_display()
            
            # Clear inputs
            self.player_name_entry.delete(0, tk.END)
            for entry in self.stats_entries.values():
                entry.delete(0, tk.END)
                entry.insert(0, "0")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for stats")
    
    def update_stats_display(self):
        self.stats_text.delete(1.0, tk.END)
        
        if not self.season_stats:
            self.stats_text.insert(1.0, "No players added yet.")
            return
        
        # Header
        header = f"{'Player':<20} {'Goals':<8} {'Assists':<8} {'Apps':<8} {'Rating':<8} {'CS':<8}\n"
        header += "="*70 + "\n"
        self.stats_text.insert(tk.END, header)
        
        # Player stats
        for stat in self.season_stats:
            line = f"{stat['name']:<20} {stat['goals']:<8} {stat['assists']:<8} {stat['appearances']:<8} {stat['rating']:<8.1f} {stat['clean_sheets']:<8}\n"
            self.stats_text.insert(tk.END, line)
    
    def clear_stats(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all player stats?"):
            self.season_stats = []
            self.update_stats_display()
    
    def view_charts(self):
        if not self.season_stats:
            messagebox.showwarning("Warning", "No player stats to visualize")
            return
        
        try:
            # Convert to dictionary format for plot_season_stats
            player_stats_dict = {}
            for stat in self.season_stats:
                player_stats_dict[stat['name']] = {
                    'Goals': stat['goals'],
                    'Assists': stat['assists'],
                    'Appearances': stat['appearances'],
                    'Average Rating': stat['rating'],
                    'Clean Sheets': stat['clean_sheets']
                }
            
            plot_season_stats(player_stats_dict)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not generate charts:\n{str(e)}")
    
    def save_stats(self):
        if not self.season_stats:
            messagebox.showwarning("Warning", "No player stats to save")
            return
        
        team_name = self.team_name_entry.get().strip()
        season_year = self.season_entry.get().strip()
        
        if not team_name or not season_year:
            messagebox.showwarning("Warning", "Please enter team name and season year")
            return
        
        try:
            # Convert to DataFrame
            df_data = {}
            for stat in self.season_stats:
                df_data[stat['name']] = {
                    'Goals': stat['goals'],
                    'Assists': stat['assists'],
                    'Clean Sheets': stat['clean_sheets'],
                    'Appearances': stat['appearances'],
                    'Average Rating': stat['rating']
                }
            
            df = pd.DataFrame(df_data).T
            safe_season_year = season_year.replace("/", "_")
            filename = f"{team_name}_{safe_season_year}_stats.csv"
            df.to_csv(filename, index_label="Player")
            
            messagebox.showinfo("Success", f"Stats saved to {filename}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not save stats:\n{str(e)}")


def main():
    root = tk.Tk()
    app = FIFACareerModeUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()