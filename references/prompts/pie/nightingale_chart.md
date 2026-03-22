## 图表类型：基础南丁格尔玫瑰图 (Nightingale Chart)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  legend: {
    top: 'bottom'
  },
  toolbox: {
    show: true,
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  series: [
    {
      name: 'Nightingale Chart',
      type: 'pie',
      radius: [50, 250],
      center: ['50%', '50%'],
      roseType: 'area',
      itemStyle: {
        borderRadius: 8
      },
      data: [
        { value: 40, name: 'rose 1' },
        { value: 38, name: 'rose 2' },
        { value: 32, name: 'rose 3' },
        { value: 30, name: 'rose 4' },
        { value: 28, name: 'rose 5' },
        { value: 26, name: 'rose 6' },
        { value: 22, name: 'rose 7' },
        { value: 18, name: 'rose 8' }
      ]
    }
  ]
};
```

