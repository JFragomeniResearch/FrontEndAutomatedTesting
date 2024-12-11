"""
Frontend Automated Testing (FEAT) Configuration and Utilities
This module provides core configuration and utility functions for the frontend testing framework.
"""

import os
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

class FEATConfig:
    """Configuration class for Frontend Automated Testing Framework"""
    
    # Base configuration
    BASE_URL = os.getenv('TEST_BASE_URL', 'http://localhost:3000')
    BROWSER = os.getenv('TEST_BROWSER', 'chrome')
    IMPLICIT_WAIT = 10
    
    # Test data paths
    TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')
    REPORTS_DIR = os.path.join(os.path.dirname(__file__), 'reports')
    
    @staticmethod
    def setup_test_environment():
        """Initialize test environment and create necessary directories"""
        os.makedirs(FEATConfig.TEST_DATA_DIR, exist_ok=True)
        os.makedirs(FEATConfig.REPORTS_DIR, exist_ok=True)
        
    @staticmethod
    def get_selenium_library():
        """Get the SeleniumLibrary instance"""
        return BuiltIn().get_library_instance('SeleniumLibrary')

class FEATUtils:
    """Utility functions for Frontend Automated Testing Framework"""
    
    @staticmethod
    def wait_and_click(locator, timeout=10):
        """Wait for element to be clickable and click it"""
        selenium = FEATConfig.get_selenium_library()
        selenium.wait_until_element_is_visible(locator, timeout)
        selenium.click_element(locator)
    
    @staticmethod
    def wait_and_input_text(locator, text, timeout=10):
        """Wait for element to be visible and input text"""
        selenium = FEATConfig.get_selenium_library()
        selenium.wait_until_element_is_visible(locator, timeout)
        selenium.input_text(locator, text)
