<!-- GETTING STARTED -->

### Prerequisites
1. Python3
2. Virtualenv
3. Pip
4. If you want to book If you want to search the vaccines by district, you find your district code from https://www.cowin.gov.in as shown below and put it in config.py file:
<img src="image/cowin_ss.png" alt="Cowin_ss">

### Installation

1. Create virtualenv
  ```sh
  python3 -m venv venv
  ```
2. Activate env<br>
* For linux:

  ```sh
  source venv/bin/python3
  ```
*  For Windows:
   ```sh
   <Absolute path to venv>/bin/activate
   ```

3. Install pip packages
   ```sh
   pip3 install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage

1. Update src/config.py file with 
   
         a. MIN_AGE_LIMIT(18 or 45)
            
         b. For search using District --> DISTRICT_ID and SEARCH_BY = 'DISTRICT'
            
         c. For search using Pin code --> PINCODE and SEARCH_BY = 'PINCODE'
   
2. Run main.py

   ```sh
   python3 src/main.py
   ```
You will hear rooster alarm when the vaccine slots are available in your district.

Look at the output of the script which has details about the centres. 

#### Hurry up, go and book your slot.

PS: Special thanks to <a href='https://github.com/pankhuriagarwal94/'>Pankhuri</a> for providing the initial code