# 生成六位数字的所有排列
with open('girl.txt', 'w') as file:
    for i in range(1, 32):  # 前两位数字从01到31
        for j in range(0, 100):  # 后两位数字从00到99
            for even in range(0, 10, 2):  # 全为偶数的倒数第二位（0, 2, 4, 6, 8）
                for last_digit in [str(x) for x in range(10)] + ['x']:  # 最后一位从0-9和x
                    # 格式化并生成六位数
                    number = f"{i:02}{j:02}{even}{last_digit}"
                    file.write(number + '\n')

print("生成完毕，已保存到 girl.txt 文件中。")
