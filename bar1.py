import matplotlib.pyplot as plt

listx = ['c','c++','c#','java','python']
listy = [45,28,38,32,50]
plt.bar(listx, listy, width=0.5, color='grykb')
plt.title("人工智慧課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" #也可設mingliu或DFKai-SB
plt.rcParams["axes.unicode_minus"] = False
plt.show()