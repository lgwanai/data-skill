## 图表类型：未来一周气温变化 (Temperature Change in the Coming Week)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  title: {
    text: 'Temperature Change in the Coming Week'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {},
  toolbox: {
    show: true,
    feature: {
      dataZoom: {
        yAxisIndex: 'none'
      },
      dataView: { readOnly: false },
      magicType: { type: ['line', 'bar'] },
      restore: {},
      saveAsImage: {}
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: [ /* 请使用用户的真实数据数组替换此处 */ ]
  },
  yAxis: {
    type: 'value',
    axisLabel: {
      formatter: '{value} °C'
    }
  },
  series: [
    {
      name: 'Highest',
      type: 'line',
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
      name: 'Lowest',
      type: 'line',
      data: [ /* 请使用用户的真实数据数组替换此处 */ ],
      markPoint: {
        data: [{ name: '周最低', value: -2, xAxis: 1, yAxis: -1.5 }]
      },
      markLine: {
        data: [
          { type: 'average', name: 'Avg' },
          [
            {
              symbol: 'none',
              x: '90%',
              yAxis: 'max'
            },
            {
              symbol: 'circle',
              label: {
                position: 'start',
                formatter: 'Max'
              },
              type: 'max',
              name: '最高点'
            }
          ]
        ]
      }
    }
  ]
};
```

