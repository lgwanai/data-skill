import argparse
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

def generate_chart(config):
    """
    通用图表生成器
    config = {
        "db_path": "workspace.db",
        "query": "SELECT category, SUM(value) as val FROM table GROUP BY category",
        "chart_type": "bar" | "pie" | "line" | "scatter",
        "x_col": "category", # 对应 SQL 结果中的列名
        "y_col": "val",      # 对应 SQL 结果中的列名
        "title": "图表标题",
        "xlabel": "X轴标签",
        "ylabel": "Y轴标签",
        "output_path": "tmp/chart.png",
        "show_labels": True  # 是否显示数据标签
    }
    """
    db_path = config.get("db_path", "workspace.db")
    query = config.get("query")
    if not query:
        raise ValueError("Missing SQL query in config")
        
    # 1. 提取数据
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    if df.empty:
        print("Warning: The query returned no data.")
        return None
        
    print(f"Data fetched successfully: {len(df)} rows.")
    
    # 2. 准备绘图
    plt.figure(figsize=(10, 6))
    chart_type = config.get("chart_type", "bar").lower()
    x_col = config.get("x_col")
    y_col = config.get("y_col")
    title = config.get("title", f"{chart_type.capitalize()} Chart")
    show_labels = config.get("show_labels", True)
    
    # 3. 绘制不同类型的图表
    if chart_type == "bar":
        ax = sns.barplot(x=x_col, y=y_col, data=df, hue=x_col, legend=False, palette='viridis')
        if show_labels:
            for p in ax.patches:
                ax.annotate(f'{p.get_height():.2f}', 
                            (p.get_x() + p.get_width() / 2., p.get_height()), 
                            ha='center', va='bottom', 
                            xytext=(0, 5), textcoords='offset points')
                            
    elif chart_type == "pie":
        # 饼图不需要 sns，直接用 plt.pie
        plt.pie(df[y_col], labels=df[x_col], autopct='%1.1f%%', startangle=140, 
                colors=sns.color_palette('viridis', len(df)))
        # 饼图通常不需要 xy label，但保持长宽比为1
        plt.axis('equal') 
        
    elif chart_type == "line":
        ax = sns.lineplot(x=x_col, y=y_col, data=df, marker='o', linewidth=2)
        if show_labels:
            for x, y in zip(df[x_col], df[y_col]):
                plt.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=9)
                
    elif chart_type == "scatter":
        sns.scatterplot(x=x_col, y=y_col, data=df, s=100, alpha=0.7)
        
    else:
        raise ValueError(f"Unsupported chart_type: {chart_type}")
        
    # 4. 设置标题和标签
    plt.title(title, fontsize=16)
    if chart_type != "pie":
        if config.get("xlabel"):
            plt.xlabel(config.get("xlabel"), fontsize=12)
        if config.get("ylabel"):
            plt.ylabel(config.get("ylabel"), fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
    # 5. 调整布局并保存
    plt.tight_layout()
    output_path = config.get("output_path", "tmp/output_chart.png")
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    plt.savefig(output_path, dpi=300)
    print(f"✅ 图表已生成并保存至: {output_path}")
    plt.close()
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Universal Chart Generator from SQLite")
    parser.add_argument("--config", required=True, help="JSON string or path to JSON file containing chart configuration")
    
    args = parser.parse_args()
    
    try:
        # 尝试将输入解析为文件路径或直接的 JSON 字符串
        if os.path.isfile(args.config):
            with open(args.config, 'r', encoding='utf-8') as f:
                config = json.load(f)
        else:
            config = json.loads(args.config)
            
        generate_chart(config)
    except Exception as e:
        print(f"ERROR generating chart: {e}")
