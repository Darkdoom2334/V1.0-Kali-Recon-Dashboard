# Darkdoom2334's V1.0-Kali-Recon-Dashboard
A fast, clean terminal-based network reconnaissance dashboard built with the help of **Bing Ai** **ChatGPT** **Python** and **Nmap**

This dashboard scans an entire subnet, detects open ports, evaluates host risk levels, displays it all in a nice dashboard format.

Best for: 
- Cybersecurity Fundimentals/Learning
- Home Lab Recon
- Future CTF Challenges
- Quick Scanning On Kali Linux

---
## Features
- Subnet scanning using Nmap
- Detects open ports on all active hosts
- Built in **risk vulnribility system**
- OS guesser
- Formated table
- Beginner friendly and easy to enhance. 

---

## Things needed/Requirments
Before runing the tool you need a to install:
### **Python Packages**
```bash
pip install python-nmap Rich
```
**Nmap** (if it has not been installed in your Kali
```bash
sudo apt install namp
``` 
# Installation Process
Clone the repostory:
```bash 
git clone https://github.com/Darkdoom2334/V1.0-Kali-Recon-Dashboard.git cd recon-dashboard
```
Make the script executable:
```bash
chmod +x recon_dashboard.py
```
## Usage
Open up the script and set **YOUR** subnet:
```python
target_subnet = "Replace with your subnet"
``` 
Then run the dashboard:
```bash
./recon_dashboard.py
```
or
```bash
python3 recon_dashboard.py
```
## Updates Coming up
* Adding Full OS Detection
* Adding Command-ling arguments
* Adding CVE (Common Vulnerabilities and Exposures) lookup for open ports
* Adding service verision detection

---

# Author
**Darkdoom Gamer**
* Cybersecurity & Computer Engineering Student
* Kali Linux/Python/Offensive and Defensive security Foucs

# **DISCLAIMER**
THIS TOOL IS USED FOR **EDUCATION AND AUTHORIZED TESTING ONLY!**
SCANNING NETWORKS WITHOUT PERMISSION IS ILLEGAL!
