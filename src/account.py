"""
Gofile Account 
"""
from .utils import go_request, FileSize

class GoAccount:
    """
    Class for handling Gofile Account Information
    """
    
    
    def __init__(self, token):
        """
        Create with the account token (from the profile page)
        """
        self.token = token


    def update_info(self):
        """
        Update account information from the gofile api
        """
        
        params = (
            ('token', self.token),
        )
        
        response = go_request("get",'https://apiv2.gofile.io/getAccountInfo', params=params)
        
        self._email = response["email"]
        self._account = response["account"]
        self._files_count = response["filesCount"]
        self._files_size = FileSize(response["filesSize"])
    
    
    def update_uploads_list(self):
        """
        Update  the uploads list from the gofile api
        """
        
        params = (
            ('token', self.token),
        )
        
        response = go_request("get", "https://apiv2.gofile.io/getUploadsList", params=params)
        
        return response
    
    
    def get_email(self):
        """
        Return the email, send a api request if not yet defined
        """
        if not hasattr(self,"_email"):
            self.update_info()
        return self._email
    
    email = property(get_email)
    
    
    def get_account(self):
        """
        Return the account type, send a api request if not yet defined
        """
        if not hasattr(self,"_account"):
            self.update_info()
        return self._account
    
    account = property(get_account)
    
    
    def get_files_count(self):
        """
        Return the files count, send a api request if not yet defined
        """
        if not hasattr(self,"_files_count"):
            self.update_info()
        return self._files_count
    
    files_count = property(get_files_count)
    
    
    def get_files_size(self):
        """
        Return the files size, send a api request if not yet defined
        """
        if not hasattr(self,"_files_size"):
            self.update_info()
        return self._files_size
    
    files_size = property(get_files_size)
    
