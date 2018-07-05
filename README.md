# Notification-system-Testing-using-selenium
Collaborative community testing

1.) .env file : 
      PROJECT_PORT = 7000 (Not used anywhere.....)
      NOTIFICATION_USER = shubh,admin,raghav,ty
      NOTIFICATION_PASSWORD = shubh
      IP_ADDRESS= https://172.17.0.1:7000
      NOTIFICATION_ROLE = author,publisher,admin
      NOTIFICATION_GROUP_ROLE = author,publisher,group admin

2.) Order of testing is mentioned in the report of Notification system Report for system.

3.) Changes in id
    The bold <left-side> needs to be searched and insert id = “<right-side>”  
      Unsubscribe - Unsubscribe
      Yes - Yes
      Save Changes - savechanges
      transition.to_state.name- id =”publish” but at 212 line id = “Visible”
      Reject - reject
      Update - update
      Remove - remove
      
     The link for the comparison is : https://github.com/singhalshubh/hacker-1/pull/1/files
     
4.) 
