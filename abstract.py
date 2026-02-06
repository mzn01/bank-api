
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Font for the header
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, 'PCECT402: Signals and Systems - Micro Project', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)  # Light blue background
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, body)
        self.ln(5)

    def draw_block_diagram(self):
        self.set_font('Arial', 'B', 10)
        
        # Define box dimensions
        w = 35
        h = 12
        y = self.get_y()
        
        # 1. Object
        self.rect(10, y, w, h)
        self.set_xy(10, y)
        self.cell(w, h, "Object", 0, 0, 'C')
        
        # Arrow
        self.set_xy(10+w, y)
        self.cell(10, h, "->", 0, 0, 'C')
        
        # 2. Sensor
        self.rect(10+w+10, y, w, h)
        self.set_xy(10+w+10, y)
        self.cell(w, h, "TCS3200", 0, 0, 'C')
        
        # Arrow
        self.set_xy(10+2*w+10, y)
        self.cell(10, h, "->", 0, 0, 'C')
        
        # 3. Arduino
        self.rect(10+2*w+20, y, w, h)
        self.set_xy(10+2*w+20, y)
        self.cell(w, h, "Arduino Uno", 0, 0, 'C')
        
        # Arrow
        self.set_xy(10+3*w+20, y)
        self.cell(10, h, "->", 0, 0, 'C')

        # 4. Servo
        self.rect(10+3*w+30, y, w, h)
        self.set_xy(10+3*w+30, y)
        self.cell(w, h, "Servo Motor", 0, 0, 'C')
        
        self.ln(20)

def generate_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # --- Title Section ---
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Intelligent Color Sorting System', 0, 1, 'C')
    pdf.set_font('Arial', 'I', 11)
    pdf.cell(0, 8, 'A Hardware + Software Integrated Project', 0, 1, 'C')
    pdf.ln(5)

    # --- Introduction ---
    pdf.chapter_title('1. Introduction')
    intro_text = (
        "In the field of industrial automation, the ability to classify objects based on physical signals "
        "is a critical task. This project, the Intelligent Color Sorting System, demonstrates a core "
        "concept of Signals and Systems: the classification of a signal vector based on its distance "
        "from a reference signal.\n\n"
        "The system automates sorting using a TCS3200 color sensor. The sensor reads reflected light "
        "intensity, converting it into a 3-dimensional signal vector [R, G, B]. By treating color as a "
        "signal vector, we apply the mathematical concept of Euclidean Distance to classify the object "
        "and actuate a Servo Motor for sorting."
    )
    pdf.chapter_body(intro_text)

    # --- Block Diagram ---
    pdf.chapter_title('2. Block Diagram')
    pdf.chapter_body("The system follows a closed-loop signal processing flow:")
    pdf.draw_block_diagram()
    
    # --- Implementation Details ---
    pdf.chapter_title('3. Implementation Details')
    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, "Hardware:", ln=True)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6, "- Controller: Arduino Uno\n- Sensor: TCS3200 (Light to Frequency)\n- Actuator: SG90 Servo Motor\n- Power: 5V DC Supply")
    pdf.ln(3)
    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, "Signal Processing Logic (Algorithm):", ln=True)
    pdf.set_font('Arial', '', 11)
    logic_text = (
        "1. Calibration: Record reference vectors for known objects (e.g., Ref_Red = [200, 50, 50]).\n"
        "2. Distance Calculation: For a new signal X = [r, g, b], calculate Euclidean distance (d):\n"
        "   d = sqrt( (r - Ref_R)^2 + (g - Ref_G)^2 + (b - Ref_B)^2 )\n"
        "3. Classification: The system selects the class with the minimum distance (Nearest Neighbor)."
    )
    pdf.multi_cell(0, 6, logic_text)
    pdf.ln(5)

    # --- Timeline ---
    pdf.chapter_title('4. Project Timeline')
    pdf.set_font('Arial', 'B', 10)
    
    # Table Header
    pdf.cell(90, 8, 'Activity', 1)
    pdf.cell(40, 8, 'Deadline', 1)
    pdf.cell(30, 8, 'Status', 1, 1)
    
    # Table Rows
    pdf.set_font('Arial', '', 10)
    data = [
        ("Group Formation & Details Update", "30-12-2025", "Completed"),
        ("Project Topic Details Update", "05-01-2026", "Completed"),
        ("Project Abstract Submission", "12-01-2026", "Completed"),
        ("Development & Integration", "Jan - Feb 2026", "In Progress"),
        ("Final Submission & Evaluation", "23-03-2026", "Upcoming"),
    ]
    
    for activity, date, status in data:
        pdf.cell(90, 8, activity, 1)
        pdf.cell(40, 8, date, 1)
        pdf.cell(30, 8, status, 1, 1)
    
    pdf.ln(8)

    # --- Group Members ---
    pdf.chapter_title('5. Group Members')
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 6, "1. ___________________________ (Roll No: _______)", ln=True)
    pdf.cell(0, 6, "2. ___________________________ (Roll No: _______)", ln=True)
    pdf.cell(0, 6, "3. ___________________________ (Roll No: _______)", ln=True)
    pdf.cell(0, 6, "4. ___________________________ (Roll No: _______)", ln=True)
    pdf.cell(0, 6, "5. ___________________________ (Roll No: _______)", ln=True)

    # Save
    pdf.output("Micro_Project_Proposal.pdf")
    print("PDF generated: Micro_Project_Proposal.pdf")

if __name__ == "__main__":
    generate_pdf()

