## 图表类型：直方图（自定义系列） (Histogram with Custom Series)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// See https://github.com/ecomfe/echarts-stat
echarts.registerTransform(ecStat.transform.histogram);
option = {
  dataset: [
    {
      source: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    {
      transform: {
        type: 'ecStat:histogram',
        config: {}
      }
    },
    {
      transform: {
        type: 'ecStat:histogram',
        // print: true,
        config: { dimensions: [1] }
      }
    }
  ],
  tooltip: {},
  grid: [
    {
      top: '50%',
      right: '50%'
    },
    {
      bottom: '52%',
      right: '50%'
    },
    {
      top: '50%',
      left: '52%'
    }
  ],
  xAxis: [
    {
      scale: true,
      gridIndex: 0
    },
    {
      type: 'category',
      scale: true,
      axisTick: { show: false },
      axisLabel: { show: false },
      axisLine: { show: false },
      gridIndex: 1
    },
    {
      scale: true,
      gridIndex: 2
    }
  ],
  yAxis: [
    {
      gridIndex: 0
    },
    {
      gridIndex: 1
    },
    {
      type: 'category',
      axisTick: { show: false },
      axisLabel: { show: false },
      axisLine: { show: false },
      gridIndex: 2
    }
  ],
  series: [
    {
      name: 'origianl scatter',
      type: 'scatter',
      xAxisIndex: 0,
      yAxisIndex: 0,
      encode: { tooltip: [0, 1] },
      datasetIndex: 0
    },
    {
      name: 'histogram',
      type: 'bar',
      xAxisIndex: 1,
      yAxisIndex: 1,
      barWidth: '99.3%',
      label: {
        show: true,
        position: 'top'
      },
      encode: { x: 0, y: 1, itemName: 4 },
      datasetIndex: 1
    },
    {
      name: 'histogram',
      type: 'bar',
      xAxisIndex: 2,
      yAxisIndex: 2,
      barWidth: '99.3%',
      label: {
        show: true,
        position: 'right'
      },
      encode: { x: 1, y: 0, itemName: 4 },
      datasetIndex: 2
    }
  ]
};
```

