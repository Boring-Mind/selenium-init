# selenium-init
Basic setup of Selenium for headless Chrome

#### Step 1. Install Chrome WebDriver

How to install Chrome WebDriver:
https://christopher.su/2015/selenium-chromedriver-ubuntu/

#### Step 2. Setup python environment:
```
sudo apt-get install python3-pip -y
sudo apt-get install python3-venv -y

python3 -m venv seleniumtest
cd seleniumtest
. bin/activate

pip install selenium
```

#### Step 3. Clone project:
```
mkdir src
cd src
git clone https://github.com/Boring-Mind/selenium-init .
```
