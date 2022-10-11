from shareplum import Site
from shareplum import Office365

authcookie = Office365('https://advantechgsenterprisesinc-my.sharepoint.com', username='njaurigue@advantechglobal.org', password='noahjaurigue2022$').GetCookies()
site = Site('https://advantechgsenterprisesinc.sharepoint.com/HR/TR/RESUMES%20%20INTERVIEWS', authcookie=authcookie)