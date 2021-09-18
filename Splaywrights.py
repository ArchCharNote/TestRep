import time

from playwright.sync_api import sync_playwright
def checkMusic():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://donateall.online/#/add-song?user=medoed")
    page.wait_for_load_state("networkidle")
    content = page.inner_text('a.ng-tns-c3-1')
    # print(page.eval_on_selector_all('"a[href]").href'))
    browser.close()
    playwright.stop()
    return content
couter = 0

while 1:
    content = checkMusic()
    with open("music.txt", "r", encoding="utf-8") as musicFile:
        lastMusic = musicFile.readlines()[-1]
        if lastMusic[0:-1] != content:
            with open("music.txt", "a", encoding="utf-8") as musicFile:
                musicFile.write(content + "\n")
    time.sleep(10)
    couter += 1
    print('Итерация №',couter)
