## 图表类型：对数回归（使用统计插件） (Logarithmic Regression)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// See https://github.com/ecomfe/echarts-stat
echarts.registerTransform(ecStat.transform.regression);
option = {
  dataset: [
    {
      source: [ /* 请使用用户的真实数据数组替换此处 */ ]
    },
    {
      transform: {
        type: 'filter',
        config: { dimension: 4, eq: 1990 }
      }
    },
    {
      transform: {
        type: 'filter',
        config: { dimension: 4, eq: 2015 }
      }
    },
    {
      transform: {
        type: 'ecStat:regression',
        config: {
          method: 'logarithmic'
        }
      }
    }
  ],
  title: {
    text: '1990 and 2015 per capita life expectancy and GDP',
    subtext: 'By ecStat.regression',
    sublink: 'https://github.com/ecomfe/echarts-stat',
    left: 'center'
  },
  legend: {
    data: ['1990', '2015'],
    bottom: 10
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross'
    }
  },
  xAxis: {
    type: 'value',
    splitLine: {
      lineStyle: {
        type: 'dashed'
      }
    }
  },
  yAxis: {
    type: 'value',
    splitLine: {
      lineStyle: {
        type: 'dashed'
      }
    }
  },
  visualMap: {
    show: false,
    dimension: 2,
    min: 20000,
    max: 1500000000,
    seriesIndex: [0, 1],
    inRange: {
      symbolSize: [10, 70]
    }
  },
  series: [
    {
      name: '1990',
      type: 'scatter',
      datasetIndex: 1
    },
    {
      name: '2015',
      type: 'scatter',
      datasetIndex: 2
    },
    {
      name: 'line',
      type: 'line',
      smooth: true,
      datasetIndex: 3,
      symbolSize: 0.1,
      symbol: 'circle',
      label: { show: true, fontSize: 16 },
      labelLayout: { dx: -20 },
      encode: { label: 2, tooltip: 1 }
    }
  ]
};
```

