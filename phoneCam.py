
import requests
import ssl


def phone_cam():

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'http://172.18.46.198:8080/shot.jpg'

    r = requests.get(url)

    with open('picpic.jpg', 'wb') as f:
        f.write(r.content)


phone_cam()














"""def phone_cam():

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'http://172.18.46.198:8080/shot.jpg'

    while True:
        imgResp = requests.get(url)
        imgNp = np.array(bytearray(imgResp.content), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)
        cv2.imshow(img, cv2.resize(img, (600, 400)))
        q = cv2.waitKey(1)
        if q == ord("q"):
            break

    cv2.destroyAllWindows()"""
