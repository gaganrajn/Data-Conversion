# SimpFileConv
In this minor project, CSV to JSON conversion is offered alongside an easily understandable Graphical User Interface.

Follow these steps
```bash
git clone https://github.com/gaganrajn.git
```
Now, open the folder
```bash
cd SimpFileConv
```
# Primary Implementation
Run the Python File

```bash
python primary.py
```
If you are a Linux user with python3, enter the below command
```bash
python3 primary.py
```
Now the program asks for the location of the required CSV File

```bash
Sample.csv
```
Note: Manual location of the CSV file present in the system can also be given.

The converted JSON format is displayed in the console with the total time taken for conversion.
# Secondary Implementation
This is another implementation where user can convert using a GUI. This is a demonstration of large scale implementation of file conversions.

Installation

The necessary libraries\modules to be installed are specified in requirements.txt. Run the below command to install them
```bash
pip install -r requirements.txt
```
Run

Executing the below command launches a GUI
```bash
python secondary.py
```
For Linux users:
```bash
sudo apt-get install python3-tk
```
Then
```bash
python3 secondary.py
```
Import a CSV file from your system by using 'Import CSV'.

Then select Convert 'CSV to JSON' and give a name to the output file in the desired location.

The converted file will be present in the pre-specified directory.
