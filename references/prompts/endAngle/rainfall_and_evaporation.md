## 图表类型：某地区蒸发量和降水量 (Rainfall and Evaporation)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  title: {
    text: 'Rainfall vs Evaporation',
    subtext: 'Fake Data'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['Rainfall', 'Evaporation']
  },
  toolbox: {
    show: true,
    feature: {
      dataView: { show: true, readOnly: false },
      magicType: { show: true, type: ['line', 'bar'] },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  calculable: true,
  xAxis: [
    {
      type: 'category',
      // prettier-ignore
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  ],
  yAxis: [
    {
      type: 'value'
    }
  ],
  series: [
    {
      name: 'Rainfall',
      type: 'bar',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
    },
    {
      name: 'Evaporation',
      type: 'bar',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      markPoint: {
        data: [
          { name: 'Max', value: 182.2, xAxis: 7, yAxis: 183 },
          { name: 'Min', value: 2.3, xAxis: 11, yAxis: 3 }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
    }
  ]
};
```

