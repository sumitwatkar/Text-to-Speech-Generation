# Text to Speech Generation using CICD

## Overview:

- The Text-to-Speech (TTS) project is a Python-based application that converts written text into clear and natural speech output. Supporting multiple languages, the application leverages the Google Text-to-Speech (GTTS) library to synthesize speech from text, making it suitable for a variety of use cases including assisting visually impaired users, language learners, and individuals who prefer to consume textual content in an auditory format.

- The project adopts continuous integration and continuous deployment (CICD) practices to streamline the development and deployment process, allowing for efficient testing and deployment of the application.

## Methodologies:

**1. Application Development**: Built the TTS application using Python and the GTTS library, optimizing the synthesis process for high-quality speech generation and implementing error handling for smooth user interactions.

**2. CICD Pipeline**: Integrated GitHub Actions for automated testing and deployment, including code linting, unit tests, and automated builds.

**3. Containerization**: Created Dockerfiles to containerize the application, ensuring consistent and efficient deployments.

**4. Infrastructure Management**: Managed deployment and infrastructure using AWS services, deploying Docker images to Amazon Elastic Container Registry (ECR) for seamless integration and hosting the application on AWS Amazon instances for scalability and flexibility.

## Tools and Technologies Used:

* **Libraries**: GTTS, numpy, pandas
* **Web Framework**: Flask
* **Version Control & CICD**: GitHub Actions
* **Containerization**: Docker
* **Deployment & Infrastructure**: Amazon EC2, Amazon ECR

## Outcomes:

**1. Streamlined Development**: The CICD pipeline automates code linting, testing, building, and deployment, offering a smooth development lifecycle.

**2. Efficient Deployment**: Automated deployment of the TTS application to Amazon EC2 instances ensures fast, consistent, and reliable deployments.

**3. Containerization**: Docker containers ensure consistent application behavior across different environments and easy deployment.

**4. Scalability**: Leverages AWS services for scalability and to handle real-time synthesis challenges.

**5. Enhanced Productivity**: CICD practices improve efficiency, reduce manual errors, and accelerate deployment cycles.
