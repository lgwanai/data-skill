## 图表类型：桑基图节点自定义样式 (Specify ItemStyle for Each Node in Sankey)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  backgroundColor: '#fff',
  title: {
    subtext: 'Data From lisachristina1234 on GitHub',
    left: 'center'
  },
  series: [
    {
      type: 'sankey',
      left: 50.0,
      top: 20.0,
      right: 150.0,
      bottom: 25.0,
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      links: [ /* 请使用用户的真实数据数组替换此处 */ ],
      lineStyle: {
        color: 'source',
        curveness: 0.5
      },
      itemStyle: {
        color: '#1f77b4',
        borderColor: '#1f77b4'
      },
      label: {
        color: 'rgba(0,0,0,0.7)',
        fontFamily: 'Arial',
        fontSize: 10
      }
    }
  ],
  tooltip: {
    trigger: 'item'
  }
};
```

