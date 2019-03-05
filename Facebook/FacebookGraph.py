import facebook


class FacebookGraph :

    def __init__(self, userToken) :
        """
        """
        self.accessToken = userToken


    def Auth(self) :
        """
        """
        return facebook.GraphAPI(access_token=self.accessToken, version="2.10")




if __name__ == '__main__':
    """
    """
    fb    = FacebookGraph("EAAJCpp858KMBAMIOjnR9l19pWqW1ymtfLf2NGvpeo2VoYcqjsfk7QNdQhrTdDmTZCE20knsR7QKwsM0IM1HHp0SN4GIA8a6rAohVCvznSyHerZCPsO892NCKReclGXAGc5dgY1uAzukgUIEbE8249eEZArNmWHnllgcsPoDtgI1z8mUzJyZCnbViffrdp54ZD")
    graph = fb.Auth()

    #Recuperation des infos de mon compte
    post = graph.get_object(id="2222234994505668", fields='created_time')
    print("Date de creation :", post['created_time'])

    #Liste de mes amis
    friends = graph.get_connections(id='2252420504820450', connection_name='friends')
    print(friends.values())
