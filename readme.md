<!-- GETTING STARTED -->

### Prerequisites
1. Python3
2. Virtualenv
3. Pip

### Installation

1. Create virtualenv
  ```sh
  virtualenv cowin_env
  ```
2. Activate env
  ```sh
  source cowin_env/bin/python3
  ```
3. Install pip packages
```sh
  pip3 install -r requirements.txt
  ```


<!-- USAGE EXAMPLES -->
## Usage

1. Update config.py file with 
   
a. MIN_AGE_LIMIT
   
b. For search using District --> DISTRICT_ID and SEARCH_BY = 'DISTRICT'
   
c. For search using Pin code --> PINCODE and SEARCH_BY = 'PINCODE'
   
2. Run main.py

   ```sh
   python3 src/main.py
   ```
You will hear rooster alarm when the vaccine slots are available in your district.

Look at the output of the script which has details about the centres. 

#### Hurry up, go and book your slot.