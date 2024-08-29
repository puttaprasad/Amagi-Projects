import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from utils.log_setup import setup_logging
from video_analysis.analyze import analyze_video_for_black_blank_screens


def test_blank_screen_detection():
    """
    Test the blank screen detection on the downloaded video.
    """
    # video_path = download_video
    video_url = 'data/video.mp4'
    blank_screens = analyze_video_for_black_blank_screens(video_url, threshold=15)
    logger = setup_logging(log_file_path='logs/logging.log')
    
    if blank_screens:
        print(f"Blank screens detected at timestamps: {blank_screens}")
        logger.info(f"Blank screens detected at timestamps: {blank_screens}")
        assert not blank_screens, f"Blank screens detected at timestamps: {blank_screens}"
    else:
        logger.info("No blank screens detected in the video.")
    
    
