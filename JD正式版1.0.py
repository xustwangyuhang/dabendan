from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time


def login():
    browser.get("https://www.jd.com")
    time.sleep(3)
    if browser.find_element(By.LINK_TEXT, "你好，请登录"):
        browser.find_element(By.LINK_TEXT, "你好，请登录").click()
        print("======请在20秒内完成登录")
        #time.sleep(30)
        #start_time = time.strftime('%y-%m-%d %H:%M:%S', time.localtime())
        #print(start_time)
        for i in range(20, 0, -1):
            print(f'\r登陆剩余时间：{i}秒', end='')
            time.sleep(1)
        browser.get("https://cart.jd.com")
    time.sleep(3)
    now = datetime.datetime.now()
    print('\n======login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)

def buy(times, choose):
    if choose == 2:
        print("===仅抢购选中的商品===")
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > times:
            if choose == 1:
                while True:
                    try:
                        if browser.find_element(By.CLASS_NAME, "jdcheckbox"):
                            browser.find_element(By.CLASS_NAME, "jdcheckbox").click()
                    except:
                        print("======找不到全选按钮")

            while True:
                try:
                    if browser.find_element(By.LINK_TEXT, "去结算"):
                        browser.find_element(By.LINK_TEXT, "去结算").click()
                        print("====结算成功====")
                        break
                except:
                    print("再结算的路上马不停蹄")

            while True:
                try:
                    if browser.find_element(By.ID, "order-submit"):
                        browser.find_element(By.ID, "order-submit").click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("====抢购成功====\n成功时间：%s" % now1)
                except:
                    print("=====恭喜您购买成功，请尽快支付====="
                          "\n====有缘我们江湖再见===")
            time.sleep(0.01)

if __name__ == "__main__":
    A = times = input("*******欢迎大家前来学习*******"
                      "\n1.本脚本仅限个人学习使用，请勿用于商业行为。"
                      "\n2.本脚本鲁棒性欠缺，出现BUG实为无奈之举。"
                      "\n3.为了响应国家号召，我们坚决遵守国家网络法，坚决反对使用脚本，坚决不使用脚本。"
                      "\n*******授之以鱼不如授之以渔*******"
                      "\n1.使用本脚本前，请提前打开手机京东APP扫码界面。"
                      "\n2.请输入抢购时间，格式如(2023-06-01 12:12:00):")

    #times = "2023-06-01 12:28:00.0000"
    browser = webdriver.Edge()
    browser.maximize_window()
    login()
    choose = int(input("***温馨提示***"
                       "\n1.非常抱歉，本脚本暂不支持到点全选快速抢购，仅可用于手动选中后抢购。"
                       "\n2.清空购物车请输入“1”(此项暂时不可用)，请在勾选需要购买的商品后，输入“2”并按下回车："))
    A = datetime.datetime.strptime(A, "%Y-%m-%d %H:%M:%S")
    while True:
        # 当前时间
        current_date = datetime.datetime.now()
        # 计算时间差
        delta = A - current_date
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print("\r", "\r距抢购时间仅剩：{}天{}小时{}分钟{}秒". format(days, hours, minutes, seconds), end="", flush=True)
        # 判断是否到达目标时间
        if delta.total_seconds() <= 0:
            print("\n秒杀开始，GO！")
            break
        # 格式化输出时间差
        time.sleep(0.000001)
    buy(times, choose)


