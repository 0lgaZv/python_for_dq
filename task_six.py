#iImporting libraries
import sys
from datetime import datetime
import re
import os
from task_four import normalize_letter_cases_return_list as case_for_list
from task_four import create_commas_separated_text_from_list as final_text

# Main class for the news feed
class Category:
    def __init__(self, name='News Feed'):
        self.name = name

        
    def case_normalisation(self, text):
        self.text=text
        self.changed_case = final_text(case_for_list (self.text))
        return self.changed_case

    def add_text(self, text):
        self.text = text
        self.norm_text = self.case_normalisation(self.text)
        # Adding text to the news feed
        with open("news_feed.txt", "a") as myfile:
            myfile.write(self.norm_text)

    def feed_refresh(self):
        # Option to clear the file and start from an empty one
        while True:
            self.feed_refresh_choice = input('''
Welcome! Would you like to refresh the feed?
Please type 'y' for yes and 'n' for no
''').lower()
            if self.feed_refresh_choice == 'y':
                with open("news_feed.txt", "w") as myfile:
                    myfile.write('''
NEWS FEED:
                     
''')
                break
            elif self.feed_refresh_choice == 'n':
                break
            else:
                print(f"You wrote '{self.feed_refresh_choice}'? I don't know what to do with it. Please try again")  # Retry if input is invalid

    def get_category(self):
        # Method for choosing category
        while True:
            self.user_category = input('''
                 Please select the option:
                 "N" for News
                 "P" for Private ad
                 "R" for Random Pie
                 "F" to import text file
                 "E" to exit the program          
                                       
                 
                 Your choice: ''').upper()
            if self.user_category in ('N', 'P', 'R', 'E', 'F'):
                return self.user_category
            print(f"You wrote '{self.user_category}'? I don't know what to do with it. Please try again")  # Retry if input is invalid


    def get_datetime(self):
        # Getting current time and date in the needed format
        self.date_time = datetime.now()
        self.current_date_and_time = self.date_time.strftime("%d-%m-%Y, %H:%M:%S")
        return self.current_date_and_time
    
    def get_user_text(self):
        # Getting the name of the news/content that should be published
        self.user_text = input('''
Print the text you would like to add to the news feed: 
''')
        return self.user_text

        



# Child class for adding text in News category
class News(Category):
    def __init__(self, name='News'):
        super().__init__(name)
    
    def get_city(self):
        # Getting city for the news
        while True:
            self.user_city = input('''
Please add the city where it happened: 
''')
            # Ensure city name contains only valid characters
            city_name_pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ'’\-.,\s]+$"
            if re.match(city_name_pattern, self.user_city):
                return self.user_city
            print(f"You wrote '{self.user_city}'? I'm not sure it exists. Please try again")  # Retry if city name is invalid

    def add_news(self):
        # Adding news to the feed
        self.news_text = self.get_user_text()  # Get user text
        print('Great!')
        self.user_city = self.get_city()  # Get city
        print('I hope this city exists')
        self.datetime_str = self.get_datetime()  # Get date and time
        self.add_text(f'''
News:------------
{self.news_text}
{self.user_city}, {self.datetime_str}
''')  # Add news
        print('Your news is added. Check the result!')

# Child class for private ad
class Private_ad(Category):
    def __init__(self, name='Private advertisement'):
        super().__init__(name)

    def get_final_datetime(self):
        # Getting expiration date - day, month, year
        while True:
            try:
                self.final_day = int(input('''
Please add expiration date: 
        The day of the month: 
'''))
                self.final_month = int(input('''
        The number of the month: 
'''))
                self.final_year = int(input('''
        The year (4 digits): 
'''))

                # Validate date
                self.date_string = f'{self.final_day}-{self.final_month}-{self.final_year}'
                self.date_object = datetime.strptime(self.date_string, "%d-%m-%Y")
                if self.date_object > datetime.now():
                    return self.date_object
                print("Expiration date should be in the future. Please try again")  # Retry for past dates
            except ValueError:
                print("Something wrong with your date. Please try again")  # Retry if date is invalid
    
    def get_diff_in_days(self, last_date):
        # Time till expiration date
        self.delta = last_date - datetime.today()
        return self.delta.days
    
    def add_pr_adv(self):
        # Publishing private ad
        self.news_text = self.get_user_text()  # Getting ad text
        print('Great!')
        self.exp_date = self.get_final_datetime()  # Getting final expiration date
        self.days_left = self.get_diff_in_days(self.exp_date)  # Getting days left
        print(f'You have {self.days_left} day(s) for your ad.')
        self.add_text(f'''
Private Ad:------------
{self.news_text}
Actual until: {self.exp_date.strftime('%d-%m-%Y')}, {self.days_left} day(s) left
''')  # Add ad
        print('Your private ad is added. Check the result!')

# Child class for a random pie recipe
class Recipe(Category):
    def __init__(self, name='Random Pie'):
        super().__init__(name)

    def get_portion_number(self):
        # Getting the number of portions
        while True:
            try:
                self.portion_number = int(input('''
Please choose the number of portions: 
'''))
                if self.portion_number > 0:
                    return self.portion_number
                print("Number of portions should be positive. Please try again")  # Retry for invalid portion numbers
            except ValueError:
                print("I gon't know how to cook it. Please try again with integer")  # Retry for non-integer values

    def get_random_ingr(self): 
        # Getting a random ingredient
        self.fruits = ['Apple', 'Banana', 'Cherry', 'Orange', 'Grape', 'Mango', 'Pineapple', 'Peach', 'Strawberry', 'Watermelon', 'Lemon']
        while True:
            try:
                self.random_ingr = int(input('''
Please choose a number from 0 to 10 to get a random ingredient: 
'''))
                if 0 <= self.random_ingr < len(self.fruits):
                    return self.fruits[self.random_ingr]
                print("I gon't know how to cook it. Please try again with  number between 0 and 10")  # Retry for out-of-range values
            except ValueError:
                print("I gon't know how to cook it. Please try again with integer")  # Retry for non-integer values
    
    def add_random_pie(self):
        # Adding recipe
        self.random_inrg = self.get_random_ingr()  # Get random ingredient
        print("Let's see what you will have...")
        self.portion_number = self.get_portion_number()  # Get portion number

        self.ingredients = {
            "all_purpose_flour": 50,
            "granulated_sugar": 20,
            "baking_powder": 2,
            "salt": 1,  
            "unsalted_butter_melted": 15,
            "milk": 15,
            "egg": 1, 
            "ground_cinnamon": 1,
            "random": 50
        }
        for key in self.ingredients:
            self.ingredients[key] *= self.portion_number #adjusting ingredients quantity

        self.bake_time = 20 + self.portion_number * 5  # Calculate baking time

        self.add_text(f'''
Random {self.random_inrg} Pie------------
Ingredients for {self.portion_number} portions:
All-purpose flour: {self.ingredients["all_purpose_flour"]} g
Granulated sugar: {self.ingredients["granulated_sugar"]} g
Baking powder: {self.ingredients["baking_powder"]} g
Salt: {self.ingredients["salt"]/2} g
{self.random_inrg}: {self.ingredients["random"]} g
Unsalted butter (melted): {self.ingredients["unsalted_butter_melted"]} g
Milk: {self.ingredients["milk"]} g
Egg: {self.ingredients["egg"]}
Ground cinnamon: {self.ingredients["ground_cinnamon"]} g (optional, for flavor)

Instructions:

Prepare the dough:
In a bowl, mix the flour, sugar, baking powder, salt, and cinnamon (if using).
Add {self.random_inrg.lower()} and mix to combine.
Stir in the melted butter, milk, and egg (if using) to form a soft and slightly sticky dough.

Shape the 'pie':
Grease a small ramekin, pie dish, or ovenproof mug lightly with butter.
Pour or press the dough into the dish, spreading it evenly with a spoon.

Bake:
Preheat your oven to 180°C (350°F).
Bake for {self.bake_time} minutes, or until the top is golden and a toothpick inserted into the center comes out clean.

''')  # Add recipe
        print('Your recipe is published. Check the result!')


# Child class for using text from file
class Text_file(Category):
    def __init__(self, name='Text file'):
        super().__init__(name)

    def choosing_folder(self):
        #choosing the folder for the file
        self.default_folder = os.path.join(os.getcwd(),'news_feed')
        while True:
            try:
                self.user_folder = input('''
    Please provide the path to the folder for the file, or press enter to skip and use default: 
    ''')
                # Ensure folder path contains only valid characters
                folder_pattern = r'^\/(?:[a-zA-Z0-9_\-\.]+\/?)*$'
                if re.match(folder_pattern, self.user_folder):
                    return self.user_folder
                elif self.user_folder == '': #default folder
                    return os.path.join(os.getcwd(),'news_feed')
                print(f"You wrote '{self.user_folder}'? I'm not sure I get it. Please try again")  # Retry if file path is invalid
            except:
                print ('Something is wrong')
    
    def get_file_path(self):
        # Getting path of the file
        self.file_folder = self.choosing_folder()
        while True:
            try:
                self.user_file_name = input('''
    I will add everything written in file (txt, please) to the news feed. 
    Make sure it looks the way you want it (without 'NEWS FEED' head, for example).                                   
    Please provide name of the file: 
    ''')
                # Ensure file path contains only valid characters
                file_name_pattern = r'^[a-zA-Z0-9_\-\.\/]+\.txt$'
                if re.match(file_name_pattern, self.user_file_name):
                    return os.path.join(self.file_folder, self.user_file_name)
                print(f"You wrote '{self.user_file_path}'? I'm not sure I get it. Please try again")  # Retry if file path is invalid
            except:
                print ('Something is wrong')



    def add_from_file(self):
        # Adding text to the feed
        self.file_path = self.get_file_path()
        try:
        # Ensure source file exists
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"The source file '{self.file_path}' does not exist.")

            with open(self.file_path, "r") as source_file:
                self.add_text('\n\n')
                for content in source_file:
                        self.add_text(content)
            print('Your content is added. I will remove the source file')
            os.remove(self.file_path)
        
        except FileNotFoundError as fnf_error:
            print(f"Error: {fnf_error}")

        except PermissionError as perm_error:
            print(f"Permission Error: {perm_error}")

        except IOError as io_error:
            print(f"IO Error: {io_error}")

        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")


def publish_news():
    # Method for publishing news based on user choice
    category = Category()
    while True:
        user_category_choice = category.get_category()
        if user_category_choice == 'N':
            News().add_news()
        elif user_category_choice == 'P':
            Private_ad().add_pr_adv()
        elif user_category_choice == 'R':
            Recipe().add_random_pie()
        elif user_category_choice == 'F':
            Text_file().add_from_file()
        else:
            sys.exit()



# Create class instance and publish news

def main():
    news_feed = Category()
    news_feed.feed_refresh()
    publish_news()

if __name__ == "__main__":
    main()
