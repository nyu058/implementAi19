import cv2
import numpy as np
import requests , json , time
import argparse
import os
from tqdm import tqdm
from math import ceil , floor
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
    # header = "Bearer {}".format(access_token)
    with open( img_path,'rb') as fp:
        files = {'media':  fp }
        test_annotated = requests.post(
            "https://api.wrnch.ai/v1/jobs",
            data={
                "work_type": key,
                "heads": True,
                "tracking": True},
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
    annoation_result , json_result = get_result(\
        img_annotation.json()['job_id']) , get_result(img_json.json()['job_id'])
    print("Done")
    return annoation_result , json_result

def run_video(video):
    img_json = request_wrnchAI(video,'json')
    print("Waiting for output ...", "\r")
    time.sleep(10)
    print("Done")
    return get_result(img_json.json()['job_id'])


class VideoProcessor:

    def __init__(self, input_video, output_video=None,\
                    width=0, height=0, count=False, \
                     json_job_id=None , annotated_job_id=None):
        self.input_video = input_video
        self.width = width
        self.height = height
        self.count = count
        self.json_content  = None
        if not output_video:
            name, ext = os.path.splitext(input_video)
            self.output_video = '{i}_compressed{e}'.format(i=name, e=ext)
        else:
            self.output_video = output_video

        if json_job_id: self.json_content = get_result(json_job_id).json()

    def read_video(self):
        images = []
        cap = cv2.VideoCapture(self.input_video)
        if not self.width:
            self.width = int(cap.get(3))

        if not self.height:
            self.height = int(cap.get(4))
        if (cap.isOpened()== False):
            print("Error opening video stream or file")
        while(cap.isOpened()):
            ret, frame = cap.read()
            if not ret: break
            images.append(frame)
        cap.release()
        return images

    def count_people(self, frames):
        persons_id = set()
        for frame in frames:
            persons = frame.get('persons', [])

            for person in persons:
                persons_id.add(person['id'])

        return len(persons_id)


    def write_video(self, frames):
        imgs = self.read_video()
        json_logs = {'nums_people_in_frame': []}
        out = cv2.VideoWriter(self.output_video,
            cv2.VideoWriter_fourcc(*'DIVX'), 30, (self.width, self.height))

        max_interval = self.get_time(10)
        json_logs['frame'] = 10
        json_logs['time_unit'] = 'min'

        for frame_indx, (img, frame) in tqdm(enumerate(zip(imgs , frames)), total=len(frames)):
            persons = frame.get('persons', [])
            if(len(persons) > 0):
                out.write(img)
            if (frame_indx + 1) % max_interval  == 0:
                json_logs['nums_people_in_frame'].append(
                    len(frame['persons']))
        print('There are {} people in the video'.\
                                            format(self.count_people(frames)))
        with open('%s.json' % (self.output_video), 'w') as outfile:
            json.dump(json_logs, outfile)
        out.release()

    def get_time(self, interval):
        tot_frames = len(self.json_content['frames'])
        video = cv2.VideoCapture(self.input_video)
        fps = video.get(cv2.CAP_PROP_FPS)

        ret_interval = ceil(tot_frames/fps)/(60*interval)
        # release vid
        video.release()
        return ret_interval # return the number of frames

    def run(self):
        if not (self.json_content):
            self.json_content = run_video(self.input_video)

        self.write_video(self.json_content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python program to compress '
                                                        'surveillance videos.')
    parser.add_argument('--input',
                        help='path to input video file',
                        )
    parser.add_argument('--output',
                        help='path to output video file',
                        )
    parser.add_argument('--count',
                        help='Count how many people are in the video'
                            ' and print the result',
                        action='store_true')
    parser.add_argument('--resolution',
                        help='resolution in output')
    parser.add_argument('--js_jobid',
                        help='Pre built json wrnch job for reading')
    parser.add_argument('--ann_jobid',
                        help='Pre built json wrnch job for reading')
    args = parser.parse_args()

    if args.resolution:
        w, h = args.resolution.split('x')
    else:
        w, h = None, None
    js_jobid , ann_jobid =None , None
    if args.js_jobid: js_jobid = args.js_jobid
    if args.ann_jobid: ann_jobid = args.ann_jobid


    vp = VideoProcessor(args.input, args.output, w, h, args.count ,
        json_job_id=js_jobid, annotated_job_id =ann_jobid)
    vp.write_video(vp.json_content['frames'])
    # annotation = run_video(args.input)

    # vp.write_video(annotation.json()['frames'])

