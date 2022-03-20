import urllib.request
import os

def download_img(img_url, api_token, folder, x):
    header = {"Authorization": "Bearer " + api_token} # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        img_name = "img" + str(x) + ".png"
        filename = folder+ img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        return "failed"


for i in range(10,20):
    folder = os.getcwd() + "\\pic" + str(i) + "\\"
    if not os.path.exists(folder):
        os.makedirs(folder)
    for j in range(0, 100):
        if __name__ == '__main__':
            # img_url = "https://api.ixiaowai.cn/api/api.php"
            img_url = "https://api.nmb.show/1985acg.php?12143"
            api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"
            download_img(img_url, api_token, folder, j)
            print(i,j)
