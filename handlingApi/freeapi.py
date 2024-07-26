import requests

def fetch_random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()
    
    if data['success'] and "data" in data:
        user_data=data["data"]
        username=user_data['login']['username']
        country=user_data['location']['country']
        return username,country
    else:
        raise Exception("Failed to fetch user data")
    
def fetch_random_jokes():
    response=requests.get('https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1')
    data=response.json()
    
    if data['success'] and 'data' in data and 'data' in data['data']:
        jokes_data=data['data']['data'] 
        for joke in jokes_data:
            print(joke['content'])
        # print(jokes_data)
    else:
        raise Exception("Failed to fetch user data")
def main():
    try:
        username ,country=fetch_random_user()
        print(f'Username: {username} \n  Country: {country}')
        fetch_random_jokes()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()