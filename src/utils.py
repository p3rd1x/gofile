"""
Utility Functions for the Gofile Package
"""

import requests
from .error import GofileResponseError


def go_request(method, url, **kwargs):
    """Helper function to send a request to gofile
    """
    response = getattr(requests,method)(url,**kwargs).json()
    
    if response["status"] != "ok":
        raise GofileResponseError(response["status"])
        
    return response["data"]


class FileSize:
    """
    Class for storing a filesize and return a pretty formated string
    """
    def __init__(self, value):
        """Set the value; unit is bytes"""
        self.value = value
        
        
    def as_kilo(self):
        """Get the filesize in kilobytes"""
        return self.value * 1e-3
    
    
    def as_mega(self):
        """Get the filesize in megabytes"""
        return self.value * 1e-6
    
    
    def as_giga(self):
        """Get the filesize in gigabytes"""
        return self.value * 1e-9
    
    
    def as_terra(self):
        """Get the filesize in terrabytes"""
        return self.value * 1e-12
    
    
    def __repr__(self):
        """
        Return a pretty formated string in appropriate unit
        """
        if self.value < 1e3:
            return f"{self.value} B"
        
        elif self.value < 1e6:
            return f"{self.as_kilo():.1f} KB"
        
        elif self.value < 1e9:
            return f"{self.as_mega():.1f} MB"
        
        elif self.value < 1e12:
            return f"{self.as_giga():.1f} GB"
        
        else:
            return f"{self.as_terra():.1f} TB"