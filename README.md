[workflow_diagram.pdf](https://github.com/user-attachments/files/24251488/workflow_diagram.pdf)
[anomaly_detection.py](https://github.com/user-attachments/files/24251476/anomaly_detection.py)
1. PROJECT TITLE
AI-Based Login Anomaly Detection Using Artificial Intelligence
2. PROJECT SUMMARY
This project focuses on detecting suspicious login activities using Artificial Intelligence techniques. The system analyzes user login behavior such as login time and failed login attempts to identify abnormal patterns. An unsupervised machine learning algorithm, Isolation Forest, is used to detect anomalies without requiring labeled attack data. The project demonstrates a practical application of AI in cyber security and is relevant to Security Operations Center (SOC) operations for threat detection and monitoring.
3. PROBLEM STATEMENT
Traditional rule-based security systems may fail to identify unusual login behavior that does not match predefined attack patterns. There is a need for an intelligent system that can automatically detect abnormal login activities to improve cyber security monitoring and reduce manual analysis efforts.
4. SOLUTION OVERVIEW
An AI-based login anomaly detection system is developed using the Isolation Forest algorithm. The system automatically analyzes login behavior and identifies suspicious activities by detecting deviations from normal login patterns. This approach enhances security monitoring by identifying potential threats at an early stage.
5. TECHNOLOGIES USED
Programming Language: Python
Libraries: Pandas, Scikit-learn
Algorithm: Isolation Forest
Platform: Windows
Tools: Command Prompt / VS Code
6. IMPLEMENTATION OVERVIEW
The implementation is carried out using Python programming language. The login dataset containing username, login time, and failed login attempts is loaded and preprocessed using the Pandas library. Relevant numerical features are selected and provided as input to the Isolation Forest algorithm. The model analyzes user login behavior and assigns anomaly labels, where “-1” indicates suspicious login activity and “1” indicates normal behavior. The detected anomalous login records are displayed as output for security analysis.
7. OUTPUT & RESULT
The system successfully identifies suspicious login activities based on abnormal login times and multiple failed login attempts. The output highlights anomalous login records, allowing security analysts to quickly identify potential security threats.
8. SOC RELEVANCE
This project is highly relevant to Security Operations Center operations as it automates the detection of abnormal login behavior. It helps in identifying unauthorized access attempts, supports threat monitoring, and reduces manual log analysis efforts using Artificial Intelligence techniques.
9. FUTURE ENHANCEMENTS
The project can be enhanced by integrating real-time log monitoring, IP address and geo-location analysis, and SIEM tool integration. Advanced machine learning and deep learning techniques can also be applied to improve detection accuracy.
10. AUTHOR DETAILS
Name: Jeyadharshni R
Role: AI Intern | Aspiring SOC Analyst
<img width="1914" height="1023" alt="png" src="https://github.com/user-attachments/assets/2ff59884-ceae-4665-9600-85aaa3073b34" />
[New Text Document.txt](https://github.com/user-attachments/files/24251411/New.Text.Document.txt)


