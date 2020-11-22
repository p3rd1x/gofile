"""
Gofile Upload
"""
from .utils import go_request

class GoUpload:
    def __init__(self, code = None, ac = None, files = []):
        """Init function
        """
        self.code = code
        self.ac = ac
        self.files = files
    
    def __repr__(self):
        """
        """
        r = "<Gofile File Data>\n"
        if self.code:
            r += f"Code: {self.code}\n"
        if self.ac:
            r += f"Admin Code: {self.ac}\n"
        if self.file:
            r += "File Infos:\n"
            for key, value in self.file.items():
                r += f"  {key}: {value}\n"
        return r
    @staticmethod
    def get_server():
        """
        Returns the best server available to receive uploads 
        """
    
        return go_request("get","https://apiv2.gofile.io/getServer")
    
    @classmethod
    def create(cls, files, ac=None, email=None, description=None, password=None, tags=None, expire=None, server="auto"):
        """
        Upload one file on a specific server
        """
        go_upload = cls(ac = ac)
        
        if server == "auto":
            server = cls.get_server()["server"]
        
        go_upload.server = server
        
        for file in files:
            go_upload._upload_single_file(file, email, description, password, tags, expire)

        
        return go_upload
    
    def _upload_single_file(self, file, email=None, description=None, password=None, tags=None, expire=None):
        """
        """
        file_data = {
            'file':         (file, open(file, 'rb')),
            'ac':           (None, self.ac),
            'email':        (None, email),
            'description':  (None, description),
            'password':     (None, password),
            'tags':         (None, tags),
            'expire':       (None, expire),
        }
        
        res = go_request("post",f"https://{self.server}.gofile.io/uploadFile", files = file_data)
        print(res)
        if self.ac == None:
            self.code = res["code"]
            self.ac = res["adminCode"]
            self.files += res["file"]
        else:
            self.files += res
        
    
    def get_download_link(self):
        """Get the download link of an upload
        """
        assert self.code != None
        return f"https://gofile.io/d/{self.code}"
    
    def delete(self):
        params = (
            ('ac', self.ac),
        )
                
        response = go_request("get",f"https://{self.server}.gofile.io/deleteUpload", params=params)
        
        print(response)