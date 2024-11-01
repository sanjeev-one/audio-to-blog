# Audio2Blog

Audio2Blog is a serverless microarchitecture built with Rust, AWS, and FastAPI. It automates the conversion of recorded conversations into AI-generated blog posts, which are then published to a blog platform. This application leverages AWS services like Step Functions, S3, Transcribe, Bedrock, and Lambda for a fully integrated serverless experience.

## Features

- **Audio Upload:** Upload an audio file through a FastAPI endpoint.
- **Transcription & Speaker Recognition:** AWS Transcribe processes the uploaded audio, providing speaker attribution.
- **AI-Powered Blog Generation:** Transcriptions are processed by AWS Bedrock to generate a blog post in an interview style.
- **Automated Publishing:** The final blog post is sent back to the web application and auto-published using GitHub’s API to the target blog platform.
- **Real-Time Status Updates:** Users can check the status of their file processing and blog generation.

## Architecture Overview

1. **File Upload (FastAPI):** The audio file is uploaded through an API endpoint, stored in an S3 bucket.
2. **AWS Step Function Orchestration:** An AWS Step Function workflow is triggered, managing the transcription, blog generation, and publishing tasks.
3. **AWS Transcribe:** Uses speaker recognition to convert audio to text with speaker labeling.
4. **AWS Bedrock (Blog Creation):** Generates a blog-style article based on the transcription.
5. **Custom Rust Lambda (Publishing):** A Lambda function written in Rust sends the blog back to the API and uses GitHub's API to post it.
6. **Status Tracking:** Processing status is tracked, and users can retrieve the status and result via API.

