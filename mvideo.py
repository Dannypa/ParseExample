import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome("../chromedriver.exe")

    # к примеру, холодильники
    link = "https://www.mvideo.ru/holodilniki-i-morozilniki-2687/holodilniki-i-morozilnye-kamery-159?page={}"
    for i in range(1, 69):
        print(link.format(i))
        driver.get(link.format(i))
        time.sleep(10)
        h = driver.execute_script("return document.body.scrollHeight;")
        driver.execute_script("""
        function sleep(ms) {
          return new Promise(resolve => setTimeout(resolve, ms));
        }
        async function main() {
          var x = document.body.scrollHeight;
        
          for (let i = 0; i <= x; i += 100) {
            window.scrollTo(0, i);
            await sleep(100);
          }
          window.scrollTo(0, x);
          await sleep(100);
        }
        
        main()
        """)
        for j in range(0, h, 100):
            time.sleep(0.1)
        time.sleep(0.2)
        els = driver.find_elements(by=By.CLASS_NAME, value="product-title__text")
        prices = driver.find_elements(by=By.CLASS_NAME, value="price__main-value")
        with open("data.txt", 'a+', encoding="utf-8") as f:
            for el, price in zip(els, prices):
                f.write(f"{el.text}, {price.text}\n")
        time.sleep(1)


if __name__ == '__main__':
    main()
