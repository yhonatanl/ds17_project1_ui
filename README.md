# DS17 Course Project 1 - Weather App by Yehonatan Levi

## Introduction

Welcome to My First Project! 🎉
This project was created as part of the DS17 Course at Bar-Ilan University.

The app offers the following features:

Current Time and Date: Displays the time and date on the user's system.
City Time and Weather: Shows the time and weather for a selected city.
Key details:

A predefined list of five cities is available in the settings.json file, with the first city set as the default.
Users can select a city from the list or type the name of any other city to view its weather information.
After retrieving the data, users can optionally set the newly selected city as the default. This default city will be saved and displayed for the next user.
Bonus Feature:
The app also provides a brief summary of the selected location using Wikipedia's API, adding an informative touch to the experience.

## Installation and Usage

### Online Usage

The easiest way to run this app is by using the following link:

https://ds17project1ui-nvwfemsypwwhcxpu7axo5b.streamlit.app/

### Local Installation

To run this app locally, you will need Poetry. Poetry allows you to manage project dependencies and run the app without manually installing all the necessary libraries. Follow these steps:

1. **Clone the repository** to your local system using the GitHub Desktop app or the following command:
   ```sh
   git clone https://github.com/yhonatanl/ds17_project1_ui/
2. **Navigate to the project directory** on your computer using a terminal emulator (e.g., CMD, PowerShell, Terminal):
   ```sh
   cd path/to/project-directory
3. **Open a Poetry shell** with the following command:
   ```sh
   poetry shell
4. **Run the app** in the Poetry shell by typing:
   ```sh
   streamlit run main.py

