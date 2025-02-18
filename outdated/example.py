from datetime import datetime

class DateFormatter:
    def __init__(self, date_str: str):
        self.date_str = date_str.strip()
    
    def format_date(self):
        if "/" in self.date_str:
            return self._format_numeric_date()
        return self._format_written_date()
    
    def _format_numeric_date(self):
        """Convert MM/DD/YYYY format to YYYY MM DD."""
        try:
            dt = datetime.strptime(self.date_str, "%m/%d/%Y")
            return dt.strftime("%Y %m %d")
        except ValueError:
            return None  # Invalid date format
    
    def _format_written_date(self):
        """Convert 'Month Day, Year' format to YYYY MM DD."""
        months = {
            "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
            "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
        }

        try:
            month_str, rest = self.date_str.split(" ", 1)  # Split month from the rest
            day, year = rest.split(",")  # Split day and year
            month = months.get(month_str.capitalize().strip())  # Convert month name to number
            
            if not month:
                return None  # Invalid month

            date_str = f"{month}/{day.strip()}/{year.strip()}"  # Format for validation
            dt = datetime.strptime(date_str, "%m/%d/%Y")
            return dt.strftime("%Y %m %d")
        except (ValueError, KeyError, IndexError):
            return None  # Invalid format

if __name__ == "__main__":
    date_input = input("Enter your date of birth (e.g., January 5, 2023 or mm/dd/yyyy): ")
    formatter = DateFormatter(date_input)
    formatted_date = formatter.format_date()
    print(formatted_date if formatted_date else "Invalid date format.")
class DataForm:
    def __init__(self):
        self.name = ""
        self.date_of_birth = ""
    
    def collect_data(self):
        self.name = input("Enter your name: ")
        
        formatter = DateFormatter(date_input)
        self.date_of_birth = formatter.format_date()
        
        if not self.date_of_birth:
            print("Invalid date format. Please try again.")
            return False
        return True

    def display_data(self):
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.date_of_birth}")
        
# Example usage
form = DataForm()
if form.collect_data():
    form.display_data()
