# 生成六位数字的所有排列
with open('boy.txt', 'w') as file:
    for i in range(1, 32):  # 前两位数字从01到31
        for j in range(0, 100):  # 后两位数字从00到99
            for odd in range(1, 10, 2):  # 全为奇数的最后一位（1, 3, 5, 7, 9）
                for last_digit in [str(x) for x in range(10)] + ['x']:  # 最后一位从0-9和x
                    # 格式化并生成六位数
                    number = f"{i:02}{j:02}{odd}{last_digit}"
                    file.write(number + '\n')

print("生成完毕，已保存到 boy.txt 文件中。")
