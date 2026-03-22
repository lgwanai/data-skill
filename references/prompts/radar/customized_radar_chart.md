## 图表类型：自定义雷达图 (Customized Radar Chart)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
  title: {
    text: 'Customized Radar Chart'
  },
  legend: {},
  radar: [
    {
      indicator: [
        { text: 'Indicator1' },
        { text: 'Indicator2' },
        { text: 'Indicator3' },
        { text: 'Indicator4' },
        { text: 'Indicator5' }
      ],
      center: ['25%', '50%'],
      radius: 120,
      startAngle: 90,
      splitNumber: 4,
      shape: 'circle',
      axisName: {
        formatter: '【{value}】',
        color: '#428BD4'
      },
      splitArea: {
        areaStyle: {
          color: ['#77EADF', '#26C3BE', '#64AFE9', '#428BD4'],
          shadowColor: 'rgba(0, 0, 0, 0.2)',
          shadowBlur: 10
        }
      },
      axisLine: {
        lineStyle: {
          color: 'rgba(211, 253, 250, 0.8)'
        }
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(211, 253, 250, 0.8)'
        }
      }
    },
    {
      indicator: [
        { text: 'Indicator1', max: 150 },
        { text: 'Indicator2', max: 150 },
        { text: 'Indicator3', max: 150 },
        { text: 'Indicator4', max: 120 },
        { text: 'Indicator5', max: 108 },
        { text: 'Indicator6', max: 72 }
      ],
      center: ['75%', '50%'],
      radius: 120,
      axisName: {
        color: '#fff',
        backgroundColor: '#666',
        borderRadius: 3,
        padding: [3, 5]
      }
    }
  ],
  series: [
    {
      type: 'radar',
      emphasis: {
        lineStyle: {
          width: 4
        }
      },
      data: [
        {
          value: [100, 8, 0.4, -80, 2000],
          name: 'Data A'
        },
        {
          value: [60, 5, 0.3, -100, 1500],
          name: 'Data B',
          areaStyle: {
            color: 'rgba(255, 228, 52, 0.6)'
          }
        }
      ]
    },
    {
      type: 'radar',
      radarIndex: 1,
      data: [
        {
          value: [ /* 请使用用户的真实数据数组替换此处 */ ],
          name: 'Data C',
          symbol: 'rect',
          symbolSize: 12,
          lineStyle: {
            type: 'dashed'
          },
          label: {
            show: true,
            formatter: function (params) {
              return params.value;
            }
          }
        },
        {
          value: [ /* 请使用用户的真实数据数组替换此处 */ ],
          name: 'Data D',
          areaStyle: {
            color: new echarts.graphic.RadialGradient(0.1, 0.6, 1, [
              {
                color: 'rgba(255, 145, 124, 0.1)',
                offset: 0
              },
              {
                color: 'rgba(255, 145, 124, 0.9)',
                offset: 1
              }
            ])
          }
        }
      ]
    }
  ]
};
```

