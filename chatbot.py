from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Creating ChatBot Instance
CB = ChatBot('ChatBot')
 # Training with Personal Ques & Ans
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "You're welcome.",
    "who Developed you",
    "I am Dveloped by SUK"

# ================= SOFTWARE DEVELOPER =================
"resume for software developer",
"A strong software developer resume should include programming languages like Java, Python, or C++. Highlight data structures, algorithms, problem-solving, and software development lifecycle. Add projects like web apps, APIs, or systems. Mention tools like Git, Docker, and cloud platforms.",

# ================= WEB DEVELOPER =================
"resume for web developer",
"A web developer resume should include HTML, CSS, JavaScript, React, Node.js, and databases. Show ability to build responsive websites, REST APIs, and full-stack applications. Include GitHub links and live project demos.",

# ================= FRONTEND =================
"resume for frontend developer",
"A frontend resume should highlight HTML5, CSS3, JavaScript, React.js, UI/UX basics, and responsive design. Mention API integration, performance optimization, and user-friendly interfaces.",

# ================= BACKEND =================
"resume for backend developer",
"A backend resume should include Node.js, Python, Java, databases (MySQL, MongoDB), REST APIs, authentication, and server-side logic. Mention scalable systems and API development.",

# ================= FULL STACK =================
"resume for full stack developer",
"A full stack resume should include frontend (React, HTML, CSS) and backend (Node.js, databases). Highlight complete project development, API integration, deployment, and system design.",

# ================= DATA ANALYST =================
"resume for data analyst",
"A data analyst resume should include Excel, SQL, Python, Power BI, Tableau, and data visualization. Show dashboards, reports, and business insights generated from data.",

# ================= DATA SCIENTIST =================
"resume for data scientist",
"A data scientist resume should include Python, machine learning, statistics, Pandas, NumPy, Scikit-learn. Add projects like prediction models and data analysis.",

# ================= DATA ENGINEER =================
"resume for data engineer",
"A data engineer resume should include SQL, Python, ETL pipelines, big data tools, and data warehousing. Highlight handling large-scale data systems.",

# ================= AI ML =================
"resume for ai ml engineer",
"An AI/ML resume should include Python, machine learning, deep learning, TensorFlow, PyTorch, NLP, and model deployment. Add real-world datasets and prediction systems.",

# ================= CYBERSECURITY =================
"resume for cybersecurity",
"A cybersecurity resume should include network security, ethical hacking, penetration testing, Kali Linux, Wireshark, and threat analysis. Show security projects.",

# ================= CLOUD =================
"resume for cloud engineer",
"A cloud engineer resume should include AWS, Azure, or Google Cloud. Highlight deployment, scaling, cloud security, and DevOps practices.",

# ================= DEVOPS =================
"resume for devops",
"A DevOps resume should include Docker, Kubernetes, CI/CD pipelines, Linux, and automation tools. Show deployment pipelines and monitoring systems.",

# ================= ANDROID =================
"resume for android developer",
"An Android resume should include Java/Kotlin, Android Studio, API integration, Firebase, and UI design. Show mobile apps with features and performance.",

# ================= IOS =================
"resume for ios developer",
"An iOS resume should include Swift, Xcode, UIKit/SwiftUI, API integration, and mobile UI design. Show apps published or developed.",

# ================= QA =================
"resume for software tester",
"A QA tester resume should include manual testing, automation testing, Selenium, test cases, bug tracking tools, and SDLC knowledge.",

# ================= UI UX =================
"resume for ui ux designer",
"A UI/UX resume should include Figma, Adobe XD, wireframing, prototyping, and user research. Show design case studies.",

# ================= DBA =================
"resume for database administrator",
"A DBA resume should include SQL, database design, performance tuning, backup, recovery, MySQL, Oracle, and database security.",

# ================= NETWORK =================
"resume for network engineer",
"A network engineer resume should include routing, switching, LAN/WAN, TCP/IP, troubleshooting, and network security.",

# ================= IT SUPPORT =================
"resume for it support",
"An IT support resume should include troubleshooting, hardware/software support, networking basics, and communication skills.",

# ================= BUSINESS ANALYST =================
"resume for business analyst",
"A business analyst resume should include requirement gathering, SQL, Excel, data analysis, and communication skills. Show business solutions.",

# ================= NEW ADDED ROLES =================
"resume for blockchain developer",
"A blockchain resume should include Solidity, Ethereum, smart contracts, Web3.js, and decentralized applications.",

"resume for game developer",
"A game developer resume should include Unity, Unreal Engine, C#, C++, game physics, and graphics programming.",

"resume for embedded systems",
"An embedded systems resume should include C, C++, microcontrollers, IoT, and hardware-software integration.",

"resume for fresher",
"A fresher resume should focus on skills, projects, internships, certifications, and problem-solving abilities. Projects are very important for freshers.",

"resume for internship",
"An internship resume should highlight academic projects, skills, certifications, and willingness to learn. Keep it simple and focused.",

# ================= FINAL =================
"final tips",
"Use simple format, include exact job keywords, highlight projects with technologies, quantify achievements, and always customize your resume for each job role."
]
trainer = ListTrainer(CB)
trainer.train(conversation)
# # Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train('chatterbot.corpus.english')
