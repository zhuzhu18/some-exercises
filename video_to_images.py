import cv2

video_path = '/home/zhuzhu/视频/vlc-record-2019-05-22-19h01m58s-AlphaPose_together.avi-.mp4'
img_dir = '/media/zhuzhu/ec114170-f406-444f-bee7-a3dc0a86cfa2/关键点数据/raw'
frq = 10

def extract_frames(video_path, img_dir, frq):
    cap = cv2.VideoCapture()

    if not cap.open(video_path):
        print('can not open the video')
        exit(1)

    count = 1
    index = 0

    while(True):

        ret, frame = cap.read()
        if not ret:
            break
        if count % frq == 0:
            path = "{}/{}.jpg".format(img_dir, index)
            cv2.imwrite(path, frame)
            index += 1
        count += 1
    cap.release()
    print('Total save {:d} images'.format(index))


if __name__ == '__main__':
    extract_frames(video_path, img_dir, frq)
