import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_mock_data(num_records=1000):
    np.random.seed(42)
    random.seed(42)
    
    # 基础数据池
    provinces_cities = [
        ("广东省", "深圳市"), ("广东省", "广州市"), ("广东省", "东莞市"),
        ("江苏省", "苏州市"), ("江苏省", "无锡市"), ("江苏省", "南京市"),
        ("浙江省", "杭州市"), ("浙江省", "宁波市"), ("浙江省", "温州市"),
        ("上海市", "上海市"), ("北京市", "北京市"), ("山东省", "杭州市")
    ]
    
    companies = [
        "迈瑞医疗", "大疆创新", "比亚迪", "富士康", "立讯精密", 
        "歌尔股份", "蓝思科技", "汇川技术", "宁德时代", "伟创力",
        "联影医疗", "先导智能", "大族激光", "中芯国际", "京东方"
    ]
    
    products = [
        "高精度五轴数控机床", "工业机器人机械臂", "激光切割机", 
        "精密注塑模具", "半导体检测设备", "自动化装配线", 
        "伺服电机组件", "精密减速器", "3D视觉传感器"
    ]
    
    contract_status = ["已签", "洽谈中", "已签", "已签", "已作废"] # 增加"已签"的权重
    production_status = ["未开始", "生产中", "已发货", "已交付", "售后维保"]
    
    # 生成时间范围 (2024-01-01 到 2026-12-31)
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2026, 12, 31)
    date_range = (end_date - start_date).days
    
    data = []
    for i in range(num_records):
        # 随机选择省市
        prov, city = random.choice(provinces_cities)
        
        # 生成随机公司名 (基础名 + 后缀)
        company = random.choice(companies) + random.choice(["科技有限公司", "股份有限公司", "工业制造厂", "精密设备公司"])
        
        # 随机日期
        random_days = random.randint(0, date_range)
        deal_date = start_date + timedelta(days=random_days)
        deal_month = deal_date.strftime("%Y-%m")
        
        # 随机金额 (根据产品类型设定基准金额区间)
        product = random.choice(products)
        if "机床" in product or "线" in product:
            amount = round(random.uniform(150.0, 500.0), 2) # 150万 - 500万
        elif "机器人" in product or "设备" in product:
            amount = round(random.uniform(50.0, 200.0), 2)  # 50万 - 200万
        else:
            amount = round(random.uniform(5.0, 80.0), 2)    # 5万 - 80万
            
        c_status = random.choice(contract_status)
        
        # 根据合同状态推导生产状态，使其符合逻辑
        if c_status != "已签":
            p_status = "未开始"
        else:
            # 如果是2024年的单，大多已交付或售后；2026年的单大多未开始或生产中
            if deal_date.year == 2024:
                p_status = random.choice(["已交付", "已交付", "售后维保"])
            elif deal_date.year == 2026:
                p_status = random.choice(["未开始", "生产中", "生产中"])
            else:
                p_status = random.choice(production_status)
                
        data.append({
            "客户公司名称": company,
            "所在省份": prov,
            "所在城市": city,
            "购买产品": product,
            "成交月份": deal_month,
            "销售金额(万元)": amount,
            "合同状态": c_status,
            "生产状态": p_status
        })
        
    df = pd.DataFrame(data)
    
    # 故意制造一些"脏数据"（模拟真实情况）
    # 1. 制造一些空值
    df.loc[np.random.choice(df.index, 10), '所在城市'] = np.nan
    df.loc[np.random.choice(df.index, 5), '销售金额(万元)'] = np.nan
    
    # 2. 制造一些重复行
    df = pd.concat([df, df.sample(n=15)], ignore_index=True)
    
    # 保存为 Excel 和 CSV
    df.to_excel("tmp/mock_sales_data.xlsx", index=False)
    df.to_csv("tmp/mock_sales_data.csv", index=False, encoding='utf-8-sig')
    print(f"✅ 成功生成 {len(df)} 条模拟测试数据，已保存至 tmp/ 目录。")

if __name__ == "__main__":
    generate_mock_data(1000)
