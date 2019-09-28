import requests , json

# login
log_req = requests.post(
    "https://api.wrnch.ai/v1/login",
    data={
        "username": "rliang",
        "password": "Monday6867123"})

access_token = json.loads(log_req.content)['access_token']
print(access_token)


# req = requests.post(
#     "https://api.wrnch.ai/v1/jobs"
#     ,
# )
# curl https://api.wrnch.ai/v1/jobs \
#   -H "Authorization: Bearer < access_token >" \
#   -F "work_type=annotated_media" \
#   -F "heads=true" \
#   -F "media=@/path/to/file" \
#   -X POST

def get_result(jobid , access_token = access_token):
    return requests.get(
        "https://api.wrnch.ai/v1/jobs/%s"%(jobid),
        headers={"Authorization": "Bearer {}".format(access_token)})



def test_annotated_media():
    header = "Bearer {}".format(access_token)
    files = {'media': open('10.png','rb')}
    print(header)
    test_annotated = requests.post(
        "https://api.wrnch.ai/v1/jobs",
        data={
            "work_type":"annotated_media",
            "heads":True},
        files=files,
        headers={"Authorization": "Bearer {}".format(access_token)}
        )
    print(test_annotated)
    return test_annotated

test = test_annotated_media()

result = get_result(json.loads(test.content)['job_id'])
