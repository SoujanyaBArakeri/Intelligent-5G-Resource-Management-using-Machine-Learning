# 5G Network Slicing Access Control and Role-Based Automation using Machine Learning

## Project Overview
This project implements a 5G network management system using network slicing, role-based access control, and machine learning. It simulates network conditions and optimizes resource allocation and power usage.

## Objectives
- Implement network slicing for 5G systems
- Apply role-based access control
- Optimize transmission power using machine learning
- Improve Quality of Service (QoS)

## Features
- User authentication (Admin, Operator, User)
- Automatic network slice assignment (URLLC, eMBB, mMTC)
- Network simulation module
- Machine learning-based power optimization
- MySQL database integration

## Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Database: MySQL
- Machine Learning: Linear Regression

## Project Structure
Network_Mini_Project/
│
├── Backend/
│ ├── app.py
│ ├── db_config.py
│ ├── model.py
│
├── Frontend/
│ ├── login.html
│ ├── dashboard.html
│ ├── network.html
│ ├── optimize.html
│ ├── result.html
│ ├── css/style.css
│ ├── js/login.js
│ ├── js/network.js
│ ├── js/optimize.js
│ └── images/


## How It Works
1. User logs in.
2. Role is identified.
3. Network slice is assigned automatically.
4. Network parameters are entered.
5. Machine learning predicts optimized power.
6. Results are displayed.

## Inputs
- Bandwidth
- Latency
- Signal strength
- Number of users
- Distance

## Outputs
- Network priority
- Optimized transmission power

## Conclusion
The system provides automated network slicing and power optimization using machine learning, improving efficiency and performance in 5G networks.
