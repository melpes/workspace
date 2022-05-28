from gids import builder

config = {
    'driver_path': './chromedriver',
    'headless': True,
    'window-size': '720x480',
    'disable_gpu': False
}

first_item = {
    'keyword': 'pixiv オリジナル10000users入り イラスト 女の子',
    'limit': 1000, # The number of images
    'download_context': './pixiv',
    'path': 'illuall' # save in ./data/animal/img_01...10
}

second_item = {
    'keyword': 'pixiv オリジナル10000users入り',
    'limit': 1000, # The number of images
    'download_context': './pixiv',
    'path': 'illu1' # save in ./data/plant/img_01...10
}

third_item = {
    'keyword': 'イラスト 女の子',
    'limit': 1000, # The number of images
    'download_context': './pixiv',
    'path': 'illu2' # save in ./data/plant/img_01...10
}

items = [first_item, second_item]

downloader = builder.build(config)

downloader.download(items)