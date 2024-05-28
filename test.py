import requests
import datetime

# Replace this with your current authorization token.
auth_token = "eyJraWQiOiI5YlN2a0JiUjlGWWxmaU02b2I5c2FGMElva2NXczh2S29SY0lCbnl6M1VvPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiamp6NW5OOGprdFFmTTJ0M0xqZ0JIdyIsInN1YiI6IjM1N2NkMjBiLTI2NmMtNGM0NC05YzcxLTU2ZTdjYTgzODVmYiIsIndlYnNpdGUiOiJTYW5qZWV2Lm9uZSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwcm9maWxlIjoiaHR0cHM6XC9cL2dpdGh1Yi5jb21cL3NhbmplZXYtb25lIiwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfNmFoaVNoU1VjIiwiY29nbml0bzp1c2VybmFtZSI6IkdpdEh1Yl82NzAzODcwOSIsInByZWZlcnJlZF91c2VybmFtZSI6InNhbmplZXYtb25lIiwicGljdHVyZSI6Imh0dHBzOlwvXC9hdmF0YXJzLmdpdGh1YnVzZXJjb250ZW50LmNvbVwvdVwvNjcwMzg3MDk_dj00IiwiYXVkIjoiNWI4Zm1odjFnMzVrYnVoODN2ZGJhdWRybmgiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiI2NzAzODcwOSIsInByb3ZpZGVyTmFtZSI6IkdpdEh1YiIsInByb3ZpZGVyVHlwZSI6Ik9JREMiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNzA2MTM5OTMyMjkwIn1dLCJ1cGRhdGVkX2F0IjoxNzEzNzU3MTk0LCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTcxMzc1NTgwMiwibmFtZSI6IlNhbmplZXYiLCJleHAiOjE3MTQ2MjM2MjUsImlhdCI6MTcxNDYyMDAyNSwiZW1haWwiOiJub3RmYWtlZWxlY3Ryb25pY21haWxzZXJ2aWNlQGdtYWlsLmNvbSJ9.sBc3e6YNjCBbMCMP6pAyCFbmmzc2L1rTxjuV2KCDlgRWXxcD0Rq2YRG7Sz4jsh8xvGiD7M5XgGYDs1ziwkocRnCUJFBjQtslnIiDPaaUnqdW9oQHPqaunCWej6EoYliyTm_idpJnbltkgfdSyQne2L591PVhOIM4OqXD7qvyEx7Fp08WzYSLU1cwS-kLZ9ETanBUl-KPRz5BJAYSwVmSDhc_Zl-P6OxM0d_scZ1if6i9tfp7fJGDUpRo-ARJBvs_WPsYhtqJn_Wiy8Xh-jnFN3s3QiRDL3nkS6JTb4Br-JRTVmcPwz-V2LCXiq1DcgTMmCeVZsd0k0t8kkLyUvcFQA"

# URL for the API endpoint.
url = "https://content.tinajs.io/1.4/content/6e46ffe5-3716-48fe-add7-0caa118ce277/github/main"

# Headers for the request.
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Content-Type": "application/json",
    "Accept": "*/*",
}

# Prepare today's date in ISO format.
today_date = datetime.datetime.now().isoformat()

# JSON payload with the new blog post details.
payload = {
    "query": "#graphql\nmutation($collection: String!, $relativePath: String!, $params: DocumentMutation!) {\ncreateDocument(\ncollection: $collection,\nrelativePath: $relativePath,\nparams: $params\n){__typename}\n}",
    "variables": {
        "collection": "post",
        "relativePath": "/new-blog-post.mdx",
        "params": {
            "post": {
                "heroImage": "https://yourimageurl.com/image.jpg",
                "category": "Tech",  # Replace with relevant category.
                "description": "A new tech blog post.",
                "pubDate": today_date,
                "tags": ["tech", "programming"],
                "title": "New Tech Blog",
                "SButton": {
                    "type": "root",
                    "children": [
                        {
                            "type": "p",
                            "children": [{"type": "text", "text": "Blog post content goes here..."}]
                        }
                    ]
                }
            }
        }
    }
}

# Make the request.
response = requests.post(url, headers=headers, json=payload)

# Check the response.
if response.status_code == 200:
    print("Blog post created successfully! ")
else:
    print(f"Failed to create blog post: {response.status_code} - {response.text}")
