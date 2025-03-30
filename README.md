# Gym Workout AI Tracker

This repository contains a project for tracking gym workouts using AI. The system is designed to analyze workout videos and provide insights into form, posture, and performance for various exercises.

## Project Structure

The workspace is organized as follows:

- *Diagonal Left and Right Dumbell Bicep Curl Standing Test #1/*  
  Contains test videos for bicep curls, divided into:
  - Diag Left/: Videos for the left side.
  - Diag Right/: Videos for the right side.

- *Diagonal Left and Right Dumbell Front Lateral Raises Test #1/*  
  Contains test videos for front lateral raises, divided into:
  - Diag Left/: Videos for the left side.
  - Diag Right/: Videos for the right side.

- *Diagonal Left and Right Dumbell Lateral Raises Test #1/*  
  Contains test videos for lateral raises, divided into:
  - Diag Left/: Videos for the left side.
  - Diag Right/: Videos for the right side.

- *Diagonal Left and Right Dumbell Shoulder Press Test #1/*  
  Contains test videos for shoulder presses.

- *Diagonal Left and Right Squats Hands Clumped Against Chest Test #1/*  
  Contains test videos for squats with hands clumped against the chest.

- *Diagonal Left and Right Squats Hands Front Raised Test #1/*  
  Contains test videos for squats with hands raised in front.

- *gym_tracker-ai/*  
  The main directory for the AI tracking system, including code and models.

- *Test Videos/*  
  A collection of raw test videos for various exercises.

- *Test Videos Premiere Pro Projects/*  
  Premiere Pro project files for editing and processing test videos.

- *Videos/*  
  Processed and finalized videos for analysis.

## Features

- *AI-Powered Analysis*: Tracks and evaluates workout form and posture.
- *Exercise-Specific Insights*: Provides detailed feedback for exercises like bicep curls, lateral raises, shoulder presses, and squats.
- *Video Processing*: Supports raw video input and integrates with Premiere Pro for editing.

## How to Use

1. *Prepare Videos*: Place your workout videos in the appropriate directories under Test Videos/.
2. *Run the AI Tracker*: Use the scripts in the gym_tracker-ai/ directory to analyze the videos.
3. *Review Results*: Check the output for insights and feedback on your workout performance.

## Requirements

- Python 3.8+
- TensorFlow or PyTorch (depending on the AI model used)
- OpenCV for video processing
- Premiere Pro (optional, for video editing)

## Installation

1. Clone the repository:
   sh
   git clone <repository-url>
   cd gym_tracker-ai
   

2. Install dependencies:
   sh
   pip install -r requirements.txt
   

3. Run the AI tracker:
   sh
   python main.py
   
## Contact

For questions or support, please contact [vedantkbhole@gmail.com].
