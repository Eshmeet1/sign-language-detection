# Sign Language and Alphabet Detection using Camera

## Overview

This project aims to develop a real-time system for detecting sign language and alphabet gestures using a camera. The system leverages computer vision and machine learning techniques to interpret hand gestures and convert them into corresponding alphabets or words.

## Features

- Real-time sign language detection
- Alphabet recognition
- User-friendly interface
- High accuracy and responsiveness

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.7+ (Recommended - 3.8.10)
- OpenCV
- TensorFlow
- Keras
- NumPy



## Installation

1. Clone the repository:
```bash
git clone https://github.com/eshmeetkohli/sign-language-detection.git
cd sign-language-detection
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. To start the sign language and alphabet detection, run the following command:
```bash
python main.py
```

2. A window will open displaying the 2 options for Alphabets & Gestures. Choose according to the usage.

3. Hold your hand in front of the camera to make a sign language gesture or an alphabet sign. The system will detect and display the recognized gesture on the screen.

## Project Structure

- `main.py`: Main script to run the detection system
- `gesture.py`: This file is responsible for running the hand gestures
- `letters.py`: This file is responsible for running the letters detection.
- `model/`: Directory containing the trained machine learning models
- `data/`: Directory containing sample data for training and testing
- `utils/`: Utility scripts for preprocessing and other helper functions

## Model Training

To train the model on your own dataset:


0. To take sample images, you need to run the file `collect_images.py`, this will capture the photos for alphabet detection. 
1. Collect images of hand gestures for different alphabets and signs.
2. Preprocess the images and split them into training and testing sets.
3. Train the model using the provided `train_model.py` script:
```bash
python train_model.py
```

## Contributing

We welcome contributions to improve this project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the contributors and the open-source community.
- Inspiration from various online resources and tutorials on computer vision and machine learning.

## Contact

For any inquiries or issues, please contact [kohlieshmeet@gmail.com@gmail.com](mailto:kohlieshmeet@gmail.com).
