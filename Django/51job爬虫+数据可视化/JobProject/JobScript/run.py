from JobScript.spider import run as spider_run
from cleaning_data import run as clearing_run
from import_data import run as import_run


def run(cookie, search_job='+', start_page=1):
    print('开始获取数据')
    spider_run(search_job=search_job, start_page=start_page, max_count=200, cookie=cookie)
    print('开始清洗数据')
    clearing_run()
    print('开始入库')
    import_run()


if __name__ == '__main__':
    cookie = '_uab_collina=165184878215205617976495; guid=258301ecc190aa20c07e60f3103136b2; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%7Bsearch_job%7D%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; _ujz=MTkyNjE0MTIzMA%3D%3D; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20220506%26%7C%26; ps=needv%3D0; 51job=cuid%3D192614123%26%7C%26cusername%3DXbHr3rM6s3aljy5maUrJ7I8d2eeMfHCgOBuvsVkXZGs%253D%26%7C%26cpassword%3D%26%7C%26cname%3DvScdfZN%252B%252BS6DWGKe4Bi1LA%253D%253D%26%7C%26cemail%3DEeIFGEsj4AG6msAnR0YKorVe6zyc%252BOmAYxkuGsSgarI%253D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0JMFYV.tme2Y%26%7C%26cconfirmkey%3D18GxbVwRCiwpE%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D181BOuQbFOCKY%26%7C%26to%3D8a6ae130e5d18dbbac4fdac6be2ec2766275356a%26%7C%26; acw_tc=76b20ff416518487819155848e5ea1c3fd9f3776ee2ab53cf408899bd69cd0; acw_sc__v2=6275364d5c90b029576a01d45c0280c42533c430; ssxmod_itna=eqmxuDnDgDciv4BP8e5Dk7qDtA=BI6xPD7YI9jDBkGo4iNDnD8x7YDv+IZYwYQOi4mfGKjAB5dhm7hmE+d3W2jHPDHxY=DUOBWhYD4SKGwD0eG+DD4DWUx03DoxGYBGx0bSyuLvzQGRD0YDzqDgD7QVbqDEDG3D03=qYg4bbTtjYnNqxGtqmkGxbqDMD7tD/+xTLeDBt=ab0TtNxPGWWOQxPeGuDG6ehTdqx0P9nwt0Ac5eWhDe+A54bhxFQGqPiGeqU0OqW7DN/B+=YE+QK0Dq/GhNmA+fzKDAi0pzQiD==; ssxmod_itna2=eqmxuDnDgDciv4BP8e5Dk7qDtA=BI6xPD7YI9D8d17eGXxeIdGaCWAkaCrAoErBRGN8K9Bf9N=UDnRD+sznlgX1tozlyaKToRZSXd=oiWlcLIo5zQ6LsSfnp9vIEbTllCmW7izMvx1KOBc9iccKOXoB112nG/hKCniD438yDmYgrGpqHVleqZOv7w4TtQfKwpI3EiOS8N2WN63df6aqhQhLdm2nKQfcU8=k3DQFIDjKD+pEoNi8QKYD='
    run(cookie, search_job='Java', start_page=1)
