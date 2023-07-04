from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time



def login():
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element(By.LINK_TEXT, "亲，请登录"):
        browser.find_element(By.LINK_TEXT, "亲，请登录").click()
        print("======请在20秒内完成登录======")
        #time.sleep(30)
        start_time = time.strftime('%y-%m-%d %H:%M:%S', time.localtime())
        print(start_time)
        for i in range(20, 0, -1):
            print(f'\r登录剩余时间：{i}秒', end='')
            time.sleep(1)
        browser.get("https://cart.taobao.com")
    now = datetime.datetime.now()
    print('\n======login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
def buy(times, choose):
    if choose == 2:
        print("======仅购买选中的商品=====")
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > times:
            if choose == 1:
                while True:
                    try:
                         if browser.find_element(By.ID, "J_SelectAll1"):
                             browser.find_element(By.ID, "J_SelectAll1").click()
                             print("====全选成功====")
                             break
                    except:
                        print("======找不到全选按钮======")

            while True:
                try:
                    if browser.find_element(By.ID, "J_SmallSubmit"):
                        browser.find_element(By.ID, "J_SmallSubmit").click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("****抢购成功****\n成功时间：%s" % now1)
                        print("成功抢到商品，请及时支付订单")
                        break
                except:
                    print("====结算失败===")

            while True:
                try:
                    if browser.find_element(By.CLASS_NAME, "go-btn"):
                        browser.find_element(By.CLASS_NAME, "go-btn").click()
                        now2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("======抢购成功\n成功时间：%s" % now2)
                        pass
                except:
                    print("====恭喜您，购买成功===="
                          "\n本次服务到此结束。")


            time.sleep(0.01)

if __name__ == "__main__":
    endtimes = times = input("**********欢迎大家学习交流**********"
                             "\n1.本脚本仅限个人学习使用，请勿用于商业行为。"
                             "\n2.本脚本鲁棒性欠缺，出现BUG实属无奈之举。"
                             "\n3.为了响应国家号召，我们坚决遵守国家网络法，坚决反对使用脚本，坚决不使用脚本。"
                             "\n*******授之以鱼不如授之以渔*******"
                             "\n1.请提前打开手机淘宝APP扫码登陆页面。\n2.请输入抢购时间，格式如(2023-01-01 12:30:00):")
    #times = "2023-06-01 12:28:00.0000"
    browser = webdriver.Edge()
    browser.maximize_window()
    login()
    choose = int(input("***温馨提示***"
                       "\n1.非常抱歉，本脚本暂不支持到点全选快速抢购，仅可用于手动选中后抢购。"
                       "\n2.清空购物车请输入“1”(此项暂时不可用)，请在勾选需要购买的商品后，输入“2”并按下回车："))
    endtimes = datetime.datetime.strptime(endtimes, "%Y-%m-%d %H:%M:%S")
    while True:
        # 当前时间
        current_date = datetime.datetime.now()
        # 计算时间差
        delta = endtimes - current_date
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print("\r", "\r距抢购时间仅剩：{}天{}小时{}分钟{}秒".format(days, hours, minutes, seconds), end="", flush=True)
        # 判断是否到达目标时间
        if delta.total_seconds() <= 0:
            print("\n秒杀开始，GO！")
            break
        # 格式化输出时间差
        time.sleep(0.000001)
    buy(times, choose)



