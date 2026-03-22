## 图表类型：阶段速度仪表盘 (Stage Speed Gauge)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  series: [
    {
      type: 'gauge',
      axisLine: {
        lineStyle: {
          width: 30,
          color: [
            [0.3, '#67e0e3'],
            [0.7, '#37a2da'],
            [1, '#fd666d']
          ]
        }
      },
      pointer: {
        itemStyle: {
          color: 'auto'
        }
      },
      axisTick: {
        distance: -30,
        length: 8,
        lineStyle: {
          color: '#fff',
          width: 2
        }
      },
      splitLine: {
        distance: -30,
        length: 30,
        lineStyle: {
          color: '#fff',
          width: 4
        }
      },
      axisLabel: {
        color: 'inherit',
        distance: 40,
        fontSize: 20
      },
      detail: {
        valueAnimation: true,
        formatter: '{value} km/h',
        color: 'inherit'
      },
      data: [
        {
          value: 70
        }
      ]
    }
  ]
};
setInterval(function () {
  myChart.setOption({
    series: [
      {
        data: [
          {
            value: +(Math.random() * 100).toFixed(2)
          }
        ]
      }
    ]
  });
}, 2000);
```

