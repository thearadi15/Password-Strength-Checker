import tkinter as tk
from tkinter import ttk, font as tkfont
import re

# ARHACX Security Color Scheme
BG_COLOR = "#0a0a12"
TEXT_COLOR = "#00ff88"
ACCENT_COLOR = "#00cc77"
ERROR_COLOR = "#ff5555"
FONT = ("Consolas", 12)
HEADER_FONT = ("Consolas", 16, "bold")

class ARHACXPasswordAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("ARHACX STEALTH ANALYZER v3.0")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("620x600")
        self.root.resizable(False, False)
        
        # Password visibility state
        self.show_password = False
        
        # Header
        self.header = tk.Label(
            root,
            text="ARHACX STEALTH ANALYZER v3.0",
            font=HEADER_FONT,
            fg=ACCENT_COLOR,
            bg=BG_COLOR
        )
        self.header.pack(pady=(20, 15))
        
        # Password Input Frame
        input_frame = tk.Frame(root, bg=BG_COLOR)
        input_frame.pack(pady=10)
        
        tk.Label(
            input_frame,
            text="ENTER PASSWORD:",
            font=FONT,
            fg=TEXT_COLOR,
            bg=BG_COLOR
        ).pack(side=tk.LEFT)
        
        # Password Entry (with toggleable visibility)
        self.entry = tk.Entry(
            input_frame,
            show="•",  # Default to bullet points
            font=FONT,
            width=25,
            bg="#11111a",
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground=ACCENT_COLOR
        )
        self.entry.pack(side=tk.LEFT, padx=10)
        self.entry.bind("<Return>", self.analyze_password)
        
        # Show/Hide Password Toggle
        self.visibility_btn = ttk.Button(
            input_frame,
            text="👁️",
            command=self.toggle_password_visibility,
            style="Visibility.TButton",
            width=3
        )
        self.visibility_btn.pack(side=tk.LEFT)
        
        # Button Style
        self.style = ttk.Style()
        self.style.configure(
            "Visibility.TButton",
            background=BG_COLOR,
            foreground=TEXT_COLOR,
            font=("Segoe UI Emoji", 10),
            borderwidth=0
        )
        
        # Analyze Button
        self.analyze_btn = tk.Button(
            root,
            text="ANALYZE PASSWORD SECURITY",
            command=self.analyze_password,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT,
            relief=tk.FLAT,
            borderwidth=0,
            highlightthickness=2,
            highlightbackground=ACCENT_COLOR
        )
        self.analyze_btn.pack(pady=15)
        
        # Security Meter
        self.meter = ttk.Progressbar(
            root,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.meter.pack(pady=5)
        
        # Strength Label
        self.strength_label = tk.Label(
            root,
            text="STRENGTH: UNKNOWN",
            font=FONT,
            fg="#555577",
            bg=BG_COLOR
        )
        self.strength_label.pack()
        
        # Detailed Analysis Report
        self.result = tk.Text(
            root,
            height=15,
            width=70,
            bg="#11111a",
            fg=TEXT_COLOR,
            font=FONT,
            wrap=tk.WORD,
            padx=15,
            pady=15,
            borderwidth=0
        )
        self.result.pack(pady=10)
        
        # Configure tags for colored text
        self.result.tag_config("strong", foreground="#00ff88")
        self.result.tag_config("moderate", foreground="#ffff00")
        self.result.tag_config("weak", foreground=ERROR_COLOR)
        self.result.tag_config("critical", foreground=ERROR_COLOR, font=("Consolas", 12, "bold"))
        
        # Footer
        tk.Label(
            root,
            text="© 2025 ARHACX SECURITY SYSTEMS | ALL RIGHTS RESERVED",
            font=("Consolas", 8),
            fg="#555577",
            bg=BG_COLOR
        ).pack(side=tk.BOTTOM, pady=5)
        
        # Initialize with instructions
        self.result.insert(tk.END, "> SYSTEM READY\n> Enter password to begin security analysis\n\n", "strong")
    
    def toggle_password_visibility(self):
        """Toggle between showing password text and bullets"""
        self.show_password = not self.show_password
        self.entry.config(show="" if self.show_password else "•")
        self.visibility_btn.config(text="🔒" if self.show_password else "👁️")
    
    def analyze_password(self, event=None):
        password = self.entry.get()
        self.result.delete(1.0, tk.END)
        
        if not password:
            self.result.insert(tk.END, "> ERROR: No password entered\n", "critical")
            self.meter["value"] = 0
            self.strength_label.config(text="STRENGTH: N/A", fg="#555577")
            return
        
        # Password analysis criteria
        length = len(password)
        has_upper = re.search(r'[A-Z]', password) is not None
        has_lower = re.search(r'[a-z]', password) is not None
        has_digit = re.search(r'[0-9]', password) is not None
        has_special = re.search(r'[^A-Za-z0-9]', password) is not None
        is_common = password.lower() in self.load_common_passwords()
        
        # Calculate strength (0-100)
        strength = 0
        if length >= 12: strength += 25
        if has_upper: strength += 15
        if has_lower: strength += 15
        if has_digit: strength += 20
        if has_special: strength += 25
        if is_common: strength = max(0, strength - 30)  # Penalty for common passwords
        
        # Update UI
        self.meter["value"] = strength
        self.generate_report(password, strength, {
            "length": length,
            "has_upper": has_upper,
            "has_lower": has_lower,
            "has_digit": has_digit,
            "has_special": has_special,
            "is_common": is_common
        })
        
        # Reset password visibility to hidden after analysis
        if self.show_password:
            self.toggle_password_visibility()
    
    def generate_report(self, password, strength, criteria):
        """Generate detailed security report"""
        self.result.insert(tk.END, "=== ARHACX SECURITY ANALYSIS REPORT ===\n\n", "strong")
        
        # Basic info (hidden password)
        hidden_pw = "•" * len(password)
        self.result.insert(tk.END, f"• Password: {hidden_pw}\n")
        self.result.insert(tk.END, f"• Length: {criteria['length']} characters\n")
        
        # Criteria breakdown
        self.result.insert(tk.END, "\n=== CRITERIA ANALYSIS ===\n")
        self.result.insert(tk.END, f"• Uppercase letters: {'✓' if criteria['has_upper'] else '✗'}\n")
        self.result.insert(tk.END, f"• Lowercase letters: {'✓' if criteria['has_lower'] else '✗'}\n")
        self.result.insert(tk.END, f"• Numbers: {'✓' if criteria['has_digit'] else '✗'}\n")
        self.result.insert(tk.END, f"• Special characters: {'✓' if criteria['has_special'] else '✗'}\n")
        self.result.insert(tk.END, f"• Common password: {'✗ (WEAK)' if criteria['is_common'] else '✓ (UNIQUE)'}\n")
        
        # Strength assessment
        self.result.insert(tk.END, "\n=== FINAL ASSESSMENT ===\n")
        if strength >= 80:
            self.result.insert(tk.END, "> STATUS: MAXIMUM SECURITY\n", "strong")
            self.strength_label.config(text="STRENGTH: EXCELLENT", fg="#00ff88")
        elif strength >= 60:
            self.result.insert(tk.END, "> STATUS: STRONG\n", "strong")
            self.strength_label.config(text="STRENGTH: GOOD", fg="#00cc77")
        elif strength >= 40:
            self.result.insert(tk.END, "> STATUS: MODERATE\n", "moderate")
            self.strength_label.config(text="STRENGTH: MODERATE", fg="#ffff00")
        else:
            self.result.insert(tk.END, "> STATUS: CRITICAL WEAKNESS\n", "critical")
            self.strength_label.config(text="STRENGTH: WEAK", fg=ERROR_COLOR)
        
        # Recommendations
        self.result.insert(tk.END, "\n=== RECOMMENDATIONS ===\n")
        if criteria['length'] < 12:
            self.result.insert(tk.END, "• Use longer passwords (12+ characters)\n")
        if not criteria['has_special']:
            self.result.insert(tk.END, "• Add special characters (!@#$ etc.)\n")
        if criteria['is_common']:
            self.result.insert(tk.END, "• Avoid common dictionary words\n")
    
    def load_common_passwords(self):
        """Load common passwords (in real app, use a file)"""
        return [
            "password", "123456", "qwerty", "letmein", "admin", 
            "welcome", "monkey", "sunshine", "password1"
        ]

if __name__ == "__main__":
    root = tk.Tk()
    app = ARHACXPasswordAnalyzer(root)
    root.mainloop()