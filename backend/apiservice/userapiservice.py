import os
from dotenv import load_dotenv, dotenv_values
import requests
import json

class UserAPiService:
    """
    file to process the user name based gists
    """    
    
    def processusergists(self, username, pagination=1):
        """
            get gists based on user name
            username will be passed from user
        
        """
        try:    
            load_dotenv()
            token=os.getenv("token")
            url = f"https://api.github.com/users/{username}/gists?per_page={pagination}"
            headers= {"Content-Type": "application/json", 
                    "Authorization": "Bearer " + token, 
                    "Accept": "application/vnd.github+json", 
                    "X-GitHub-Api-Version": "2022-11-28"}
            user_data = requests.get(url, headers=headers, timeout=15)
            user_data.raise_for_status()
            result = self.usergistresponse(usercontent=user_data.content)
            result["status_code"]=user_data.status_code
            return result
        except requests.exceptions.HTTPError as e:
            result={}
            result["error_message"]=e.args[0]
            return result
        
    
    def usergistresponse(self,usercontent):
        jsondata=json.loads(usercontent)
        result={}
        result["gists_url"] = jsondata[0]['owner']["gists_url"]
        return result