## 图表类型：指数回归（使用统计插件） (Exponential Regression)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// See https://github.com/ecomfe/echarts-stat
echarts.registerTransform(ecStat.transform.regression);
option = {
  dataset: [
    {
      source: [
        [1, 4862.4],
        [2, 5294.7],
        [3, 5934.5],
        [4, 7171.0],
        [5, 8964.4],
        [6, 10202.2],
        [7, 11962.5],
        [8, 14928.3],
        [9, 16909.2],
        [10, 18547.9],
        [11, 21617.8],
        [12, 26638.1],
        [13, 34634.4],
        [14, 46759.4],
        [15, 58478.1],
        [16, 67884.6],
        [17, 74462.6],
        [18, 79395.7]
      ]
    },
    {
      transform: {
        type: 'ecStat:regression',
        config: {
          method: 'exponential'
          // 'end' by default
          // formulaOn: 'start'
        }
      }
    }
  ],
  title: {
    text: '1981 - 1998 gross domestic product GDP (trillion yuan)',
    subtext: 'By ecStat.regression',
    sublink: 'https://github.com/ecomfe/echarts-stat',
    left: 'center'
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross'
    }
  },
  xAxis: {
    splitLine: {
      lineStyle: {
        type: 'dashed'
      }
    }
  },
  yAxis: {
    splitLine: {
      lineStyle: {
        type: 'dashed'
      }
    }
  },
  series: [
    {
      name: 'scatter',
      type: 'scatter',
      datasetIndex: 0
    },
    {
      name: 'line',
      type: 'line',
      smooth: true,
      datasetIndex: 1,
      symbolSize: 0.1,
      symbol: 'circle',
      label: { show: true, fontSize: 16 },
      labelLayout: { dx: -20 },
      encode: { label: 2, tooltip: 1 }
    }
  ]
};
```

