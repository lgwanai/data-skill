## 图表类型：雨量蒸发量关系图 (Rainfall vs Evaporation)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// prettier-ignore
let timeData = [ /* 请使用用户的真实数据数组替换此处 */ ];
timeData = timeData.map(function (str) {
  return str.replace('2009/', '');
});
option = {
  title: {
    text: 'Rainfall vs Evaporation',
    left: 'center'
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      animation: false
    }
  },
  legend: {
    data: ['Evaporation', 'Rainfall'],
    left: 10
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
  axisPointer: {
    link: [
      {
        xAxisIndex: 'all'
      }
    ]
  },
  dataZoom: [
    {
      show: true,
      realtime: true,
      start: 30,
      end: 70,
      xAxisIndex: [0, 1]
    },
    {
      type: 'inside',
      realtime: true,
      start: 30,
      end: 70,
      xAxisIndex: [0, 1]
    }
  ],
  grid: [
    {
      left: 60,
      right: 50,
      height: '35%'
    },
    {
      left: 60,
      right: 50,
      top: '55%',
      height: '35%'
    }
  ],
  xAxis: [
    {
      type: 'category',
      boundaryGap: false,
      axisLine: { onZero: true },
      data: timeData
    },
    {
      gridIndex: 1,
      type: 'category',
      boundaryGap: false,
      axisLine: { onZero: true },
      data: timeData,
      position: 'top'
    }
  ],
  yAxis: [
    {
      name: 'Evaporation(m³/s)',
      type: 'value',
      max: 500
    },
    {
      gridIndex: 1,
      name: 'Rainfall(mm)',
      type: 'value',
      inverse: true
    }
  ],
  series: [
    {
      name: 'Evaporation',
      type: 'line',
      symbolSize: 8,
      // prettier-ignore
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    {
      name: 'Rainfall',
      type: 'line',
      xAxisIndex: 1,
      yAxisIndex: 1,
      symbolSize: 8,
      // prettier-ignore
      data: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  ]
};
```

