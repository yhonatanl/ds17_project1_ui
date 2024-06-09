# DS17 Course Project 1 - Weather App by Yehonatan Levi

## Introduction

Welcome to my first project :)
This projectis as part of the DS17 Course at Bar Ilan. 

This app provides users with the current time and date on their system, the time in a selected city, and the weather in that city.

A list of five cities is available in the `settings.json` file, with the first city set as the default. Users can select one of these cities or type the name of any city to get its weather information. After retrieving the information, users have the option to change the default city to the newly selected one. The new default city will be displayed to the next user who runs the app.

Additionally, as an extra feature, a brief summary of the selected location is provided using Wikipedia's API, making this project even more unique.

## Installation and Usage

### Online Usage

The easiest way to run this app is by using the following link:
[Streamlit App](https://ds17project1ui-nvwfemsypwwhcxpu7axo5b.streamlit.app/)

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

