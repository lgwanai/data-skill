## 图表类型：折线图的渐变 (Line Gradient)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// prettier-ignore
const data = [ /* 请使用用户的真实数据数组替换此处 */ ];
const dateList = data.map(function (item) {
  return item[0];
});
const valueList = data.map(function (item) {
  return item[1];
});
option = {
  // Make gradient line here
  visualMap: [
    {
      show: false,
      type: 'continuous',
      seriesIndex: 0,
      min: 0,
      max: 400
    },
    {
      show: false,
      type: 'continuous',
      seriesIndex: 1,
      dimension: 0,
      min: 0,
      max: dateList.length - 1
    }
  ],
  title: [
    {
      left: 'center',
      text: 'Gradient along the y axis'
    },
    {
      top: '55%',
      left: 'center',
      text: 'Gradient along the x axis'
    }
  ],
  tooltip: {
    trigger: 'axis'
  },
  xAxis: [
    {
      data: dateList
    },
    {
      data: dateList,
      gridIndex: 1
    }
  ],
  yAxis: [
    {},
    {
      gridIndex: 1
    }
  ],
  grid: [
    {
      bottom: '60%'
    },
    {
      top: '60%'
    }
  ],
  series: [
    {
      type: 'line',
      showSymbol: false,
      data: valueList
    },
    {
      type: 'line',
      showSymbol: false,
      data: valueList,
      xAxisIndex: 1,
      yAxisIndex: 1
    }
  ]
};
```

