## 图表类型：雨量流量关系图 (Rainfall)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  title: {
    text: 'Rainfall and Flow Relationship',
    left: 'center'
  },
  grid: {
    bottom: 80
  },
  toolbox: {
    feature: {
      dataZoom: {
        yAxisIndex: 'none'
      },
      restore: {},
      saveAsImage: {}
    }
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross',
      animation: false,
      label: {
        backgroundColor: '#505765'
      }
    }
  },
  legend: {
    data: ['Flow', 'Rainfall'],
    left: 10
  },
  dataZoom: [
    {
      show: true,
      realtime: true,
      start: 65,
      end: 85
    },
    {
      type: 'inside',
      realtime: true,
      start: 65,
      end: 85
    }
  ],
  xAxis: [
    {
      type: 'category',
      boundaryGap: false,
      axisLine: { onZero: false },
      // prettier-ignore
      data: [ /* 请使用用户的真实数据数组替换此处 */ ].map(function (str) {
                return str.replace(' ', '\n');
            })
    }
  ],
  yAxis: [
    {
      name: 'Flow(m³/s)',
      type: 'value'
    },
    {
      name: 'Rainfall(mm)',
      nameLocation: 'start',
      alignTicks: true,
      type: 'value',
      inverse: true
    }
  ],
  series: [
    {
      name: 'Flow',
      type: 'line',
      areaStyle: {},
      lineStyle: {
        width: 1
      },
      emphasis: {
        focus: 'series'
      },
      markArea: {
        silent: true,
        itemStyle: {
          opacity: 0.3
        },
        data: [
          [
            {
              xAxis: '2009/9/12\n7:00'
            },
            {
              xAxis: '2009/9/22\n7:00'
            }
          ]
        ]
      },
      // prettier-ignore
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    {
      name: 'Rainfall',
      type: 'line',
      yAxisIndex: 1,
      areaStyle: {},
      lineStyle: {
        width: 1
      },
      emphasis: {
        focus: 'series'
      },
      markArea: {
        silent: true,
        itemStyle: {
          opacity: 0.3
        },
        data: [
          [
            {
              xAxis: '2009/9/10\n7:00'
            },
            {
              xAxis: '2009/9/20\n7:00'
            }
          ]
        ]
      },
      // prettier-ignore
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  ]
};
```

