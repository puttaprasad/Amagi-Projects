import cv2

def analyze_video_for_black_blank_screens(video_path, threshold=1):
    """
    Analyzes the video and detects black blank screens.
    A black blank screen is defined as a frame with pixel values close to zero.
    
    :param video_path: Path to the video file.
    :param threshold: Pixel intensity threshold to consider a frame as black blank.
    :return: List of timestamps where black blank screens are detected.
    """
    cap = cv2.VideoCapture(video_path)
    black_blank_screens = []
    
    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Check if the frame is mostly black (based on the threshold)
        if cv2.mean(gray_frame)[0] < threshold:
            # Calculate the timestamp of the frame
            timestamp = frame_count / fps
            black_blank_screens.append(timestamp)
        
        frame_count += 1
    
    cap.release()
    
    return black_blank_screens
