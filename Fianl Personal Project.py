from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data():
    global df
    df = pd.read_csv('C:\\Users\\willi\OneDrive\Documents\Combined_Clean.csv')
    df.fillna(df['Acre Value'].median(), inplace=True)

def show_graph(graph_type):
    if graph_type == "Land Values Over Time":
        sns.lineplot(x="Year", y="Acre Value", data=df)
        plt.show()

    elif graph_type == "Agriculture Acre Values":
        sns.histplot(data=df, x="Acre Value")
        plt.show()

    elif graph_type == "Land Values vs Acreage":
        sns.scatterplot(x="Region or State", y="Acre Value", data=df)
        plt.show()

    elif graph_type == "Average Acre Values by Year":
        avg_land_values = df.groupby("Year")["Acre Value"].mean().reset_index()
        sns.barplot(x="Year", y="Acre Value", data=avg_land_values)
        plt.xticks(rotation='vertical')
        plt.show()

    elif graph_type == "Categories Of Land":
        plt.figure(figsize=(10,5))
        plt.title("Categories Of Land")
        df["LandCategory"].value_counts().plot(kind="barh", color="g")
        plt.show()

    # New graph type: Average Acre Values by State
    elif graph_type == "Average Acre Values by State":
        avg_land_values_s = df.groupby("State")["Acre Value"].mean().reset_index()
        plt.figure(figsize=(12,5))
        plt.xticks(rotation='vertical')
        sns.barplot(data=avg_land_values_s, x="State", y="Acre Value")
        plt.show()

    # New graph type: Region Count
    elif graph_type == "Region Count":
        plt.figure(figsize=(10,10))
        sns.countplot(data=df, y='Region')
        plt.title('Regions Value')
        plt.ylabel('Regions', fontsize=15)
        plt.show()

    elif graph_type == "Time Series Trend":
        plt.figure(figsize=(12, 6))  # Set the figure size
        plt.title("Time Series Trend of Acre Value")

        # Plotting the actual Acre Values
        sns.lineplot(x="Year", y="Acre Value", data=df, label="Actual")

        # Calculating and plotting the rolling mean
        rolling_mean = df.groupby("Year")["Acre Value"].mean().rolling(window=5).mean()
        plt.plot(df['Year'].unique(), rolling_mean, label="5-Year Rolling Mean", color='orange')

        plt.legend()
        plt.xticks(rotation='vertical')
        plt.ylabel("Acre Value")
        plt.show()

def create_icon_button(frame, img_path, graph_type, title, row, column):
    """Creates a button with an image, title, and attaches it to a function that shows the graph."""
    pil_image = Image.open(img_path).resize((100, 100))  # open the image and resize it
    img = ImageTk.PhotoImage(pil_image)
    
    button = tk.Button(frame, image=img, command=lambda: show_graph(graph_type))
    button.image = img  # Store a reference to the image to prevent it from being garbage collected
    button.grid(row=row, column=column, padx=10, pady=10)
    
    label = tk.Label(frame, text=title)  # Create a label to display the title below the button
    label.grid(row=row+1, column=column, pady=5)  # Position the label below the button

# Add the load_and_clean_data() function definition here or import it if it's from another file.

load_and_clean_data()

root = tk.Tk()
root.title("Agriculture Data Visualization")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

# Create buttons with images and titles for each graph
create_icon_button(frame, 'C:\\Users\\willi\\OneDrive\\Documents\\Farm\\OIP (1).jfif', "Land Values Over Time", "Land Values Over Time", 0, 0)
create_icon_button(frame, 'C:\\Users\\willi\\OneDrive\\Documents\\Farm\\OIP.jfif', "Agriculture Acre Values", "Agriculture Acre Values", 0, 2)
create_icon_button(frame, 'C:\\Users\\willi\\OneDrive\\Documents\\Farm\\R (1).jfif', "Land Values vs Acreage", "Land Values vs Acreage", 0, 4)
create_icon_button(frame, 'C:\\Users\\willi\\OneDrive\\Documents\\Farm\\R (2).jfif', "Average Acre Values by Year", "Average Acre Values by Year", 0, 6)
create_icon_button(frame, 'C:\\Users\\willi\\OneDrive\\Documents\\Farm\\R.jfif', "Categories Of Land", "Categories Of Land", 2, 0)
create_icon_button(frame, 'C:\\Users\\willi\\OneDrive\\Documents\\Farm\\R (2).jfif', "Average Acre Values by State", "Average Acre Values by State", 4, 0)
create_icon_button(frame, 'C:\\Users\\willi\\OneDrive\\Documents\\Farm\\R.jfif', "Region Count", "Region Count", 6, 0)
create_icon_button(frame, 'C:\\Users\\willi\\OneDrive\\Documents\\Farm\\OIP (1).jfif', "Time Series Trend", "Time Series Trend", 2, 2)

root.mainloop()