import requests


"""
    返回json字符串特定内容
    :param path: https://www.minorpatch.com/index.jsonhttps://www.minorpatch.com/index.json
    :return: json列表的title, uri
    """
def get_json(json_url):
    # 获取json内容
    r = requests.get(json_url)
    json = r.json()
    # 打印title和uri

    for i in json:
        title = i['title']
        date = i['date']
        uri = i['uri']
        url = "https://www.minorpatch.com" + i['uri']
        # if url[-1] != "#":  # 排除链接末尾是#的链接
        # 排除uri中包含skills的链接
        if "skills" not in uri:
            if "solutions" not in uri:
                if "#" not in uri:
                    # 去掉title里的Crack
                    if "Crack" in title:
                        title = title.replace("Crack", "")
                        # print("AppName: " + title + " " + "Updated Date: " + date + " " + "URL: " + url)
                        # 字典数据追加写入excel文件
                        data = {'AppName': title, 'UpdatedDate': date, 'URL': url}
                        # print(data)

                        # 追加写入 README.md 文件
                        with open('README.md', 'a') as filename:
                            filename.write('| ' + title + ' | ' + date + ' | ' + url + ' |\n')



def write_mdfile():
    md_file = 'minorpatch.md'  # 在当前py文件所在路径下的new文件中创建txt
    filename = open(md_file, 'a')
    # 在file中写入表格内容
    filename.write('| AppName | Updated Date | URL |\n')
    filename.write('| --- | --- | --- |\n')
    get_json(json_url)
    filename.close()





json_url = 'https://www.minorpatch.com/index.json';

if __name__ == '__main__':
    write_mdfile()














