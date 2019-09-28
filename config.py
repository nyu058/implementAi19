import cv2
import numpy as np
import requests , json , time

# login
log_req = requests.post(
    "https://api.wrnch.ai/v1/login",
    data={
        "username": "rliang",
        "password": "Monday6867123"})

access_token = json.loads(log_req.content)['access_token']


def get_result(jobid , access_token = access_token):
    return requests.get(
        "https://api.wrnch.ai/v1/jobs/%s"%(jobid),
        headers={"Authorization": "Bearer {}".format(access_token)})



def request_wrnchAI(img_path = '10.png',key="annotated_media"):
    header = "Bearer {}".format(access_token)
    files = {'media': open( img_path,'rb')}
    test_annotated = requests.post(
        "https://api.wrnch.ai/v1/jobs",
        data={
            "work_type":key,
            "heads":True},
        files=files,
        headers={"Authorization": "Bearer {}".format(access_token)}
        )
    print(test_annotated)
    return test_annotated

def show_img(img):
    cv2.imshow("image", img)
    k = cv2.waitKey(0)
    if k == ord('q'):
        cv2.destroyAllWindows()


def decode_img(img_str):
    parr = np.fromstring(img_str, np.uint8)
    img_np = cv2.imdecode(parr, 1)
    return img_np

def show_result(result_response):
    result_json = get_result(result_response.json()['job_id'])
    img = decode_img(result_json.content)
    show_img(img)

def run(img_path):
    img_annotation = request_wrnchAI(img_path)
    img_json = request_wrnchAI(img_path , "json")
    print("Waiting for output ...", "\r")
    time.sleep(4)
    annoation_result , json_result = get_result(img_annotation.json()['job_id']) \
        , get_result(img_json.json()['job_id'])
    print("Done")
    return annoation_result , json_result

if __name__ == "__main__":
    ann , json = run("./10.png")
    show_img(decode_img(ann.content))
    print(json.json)
